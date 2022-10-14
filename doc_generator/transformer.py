import subprocess
import json
from copy import deepcopy


from yattag import indent
from lxml import etree as ET, objectify

xslt_remove_ns = ET.fromstring("""
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output indent="yes"/>
  <xsl:strip-space elements="*"/>

  <xsl:template match="node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="*" priority="1">
    <xsl:element name="{local-name()}" namespace="">
      <xsl:apply-templates select="@*|node()"/>
    </xsl:element>
  </xsl:template>

  <xsl:template match="@*">
    <xsl:attribute name="{local-name()}" namespace="">
      <xsl:value-of select="."/>
    </xsl:attribute>
  </xsl:template>

</xsl:stylesheet>
""")


def body_to_chapters(body):
    def base_process(root):
        for elem in root:
            if elem.tag == 'list':
                elem.tag = 'ul'
            elif elem.tag == 'item':
                elem.tag = 'li'
            elif elem.tag == 'lb':
                elem.tag = 'br'
            elif elem.tag == 'hi':
                elem.tag = 'span'
            elif elem.tag == 'ref':
                elem.tag = 'a'
                elem.set('href', elem.get('target').strip())
                elem.attrib.pop('target')
                elem.text = elem.text.strip()
            elif elem.tag == 'graphic':
                elem.tag = 'img'
                elem.set('src', elem.get('url'))
                if elem.get('height') is not None:
                    elem.set('style', f'max-height:{elem.get("height")};')
            elif elem.tag == 'figure':
                elem.tag = 'div'
                elem.set('class', 'figure')
            elif elem.tag == 'gi':
                elem.tag = 'a'
                elem.set('href', '/MPM/docs#' + elem.text.strip())
                elem.set('class', 'gi')
                elem.text = elem.text.strip()
            elif elem.tag == 'att':
                elem.tag = 'span'
                elem.set('class', 'att')
                elem.text = elem.text.strip()
            elif elem.tag == 'label':
                elem.tag = 'span'
                elem.set('class', 'label')
            base_process(elem)

    base_process(body)

    for chapter in body.xpath('./div[@type="chapter"]'):
        for subchapter in chapter.xpath('./div[@type="chapter"]'):
            head = subchapter.xpath('./head')[0]
            head.tag = 'h2'
            subchapter.set('class', 'subchapter')

            new = ET.Element('div')
            new.set('class', 'content')
            for e in subchapter:
                if e.tag == 'h2': continue
                new.append(e)
            subchapter.append(new)

        new = ET.Element('div')
        new.set('class', 'content')
        for e in chapter:
            if e.tag == 'head': continue
            new.append(e)
        chapter.append(new)

        head = chapter.xpath('./head')[0]
        head.tag = 'h1'
        chapter.set('class', 'chapter')

    chapters = [ET.tostring(chapter).decode('utf-8').strip() for chapter in body.xpath('./div[@type="chapter"]')]
    return chapters


def element_to_string(root):
    def base_process(root):
        if root.tag == 'desc':
            root.tag = 'p'

        for child in root:
            if child.tag == 'gi':
                child.tag = 'a'
                child.set('href', '#' + child.text.strip())
                child.set('class', 'gi')
                child.text = child.text.strip()
            elif child.tag == 'att':
                child.tag = 'span'
                child.set('class', 'att')
                child.text = child.text.strip()
            elif child.tag == 'head':
                child.tag = 'h2'
            elif child.tag == 'list':
                child.tag = 'ul'
            elif child.tag == 'item':
                child.tag = 'li'
            elif child.tag == 'lb':
                child.tag = 'br'
            elif child.tag == 'hi':
                child.tag = 'span'
            elif child.tag == 'ref':
                child.tag = 'a'
                child.set('href', '#' + child.get('target').strip())
                child.text = child.text.strip()

            base_process(child)

    # Go recursively through elements (operations are in place)
    base_process(root)

    for elem in root.xpath('//egXML'):
        for e in elem.iter('*'):
            if e.text is not None:
                e.text = e.text.strip()
            if e.tail is not None:
                e.tail = e.tail.strip()

        lines = ET.tostring(elem, pretty_print=True).decode('utf-8').split('\n')[1:-2]
        #lines = [l.strip() for l in lines]
        line = ''.join(lines).strip()

        if len(line) == 0:
            continue
        
        line = indent(line, indent_text = True)
        
        elem.clear()
        elem.tag = 'pre'
        elem.set('class', 'code-example')
        elem.text = line
        

    return ET.tostring(root, pretty_print=True).decode('utf-8').strip()


if __name__ == '__main__':
    parser = ET.XMLParser(remove_blank_text=True)
    input_xml = ET.parse('mpm-monolithic.odd', parser=parser)
    root = input_xml.xslt(xslt_remove_ns).getroot()
    objectify.deannotate(root, cleanup_namespaces=True, xsi_nil=True)

    version = root.xpath('//edition')[0].get('n')

    items = []

    specs = root.xpath('//*[name()="classSpec" or name()="elementSpec"]')
    contained_by = {}
    for spec in specs:
        item = {}
        item['base'] = spec.get('base')
        item['ident'] = spec.get('ident')
        item['type'] = spec.get('type') or 'element'
        item['module'] = spec.get('module')
        item['gloss'] = spec.xpath('./gloss[1]/text()')
        item['desc'] = element_to_string(spec.xpath('./desc[1]')[0])
        item['examples'] = [element_to_string(e) for e in spec.xpath('./exemplum/*')]
        item['memberOf'] = spec.xpath('./classes/memberOf/@key')
        item['remarks'] = [element_to_string(e) for e in spec.xpath('./remarks/*')]


        # item['constraint'] = element_to_string(spec.xpath('./')[0])

        def get_attributes(spec, collection):
            # Check recursively for nested attributes
            member_ofs = spec.xpath('./classes/memberOf/@key')
            for key in member_ofs:
                get_attributes(root.xpath(f'//*[@ident="{key}"]')[0], collection)

            # Add attribute definitions to collections dict
            att_defs = spec.xpath(f'./attList/attDef')
            for att_def in att_defs:
                ident = att_def.get('ident')

                # Description
                desc = att_def.xpath('./desc')
                if len(desc) > 0:
                    text = element_to_string(deepcopy(desc[0]))
                elif ident in collection:
                    text = collection[ident]['text']
                else:
                    text = ''

                # Type
                att_type = att_def.xpath('./datatype/dataRef/@name')
                att_val_items = att_def.xpath('./valList/valItem/@ident')
                if len(att_type) > 0:
                    att_type = att_type[0]
                elif len(att_val_items) > 0:
                    att_val_items = [f'"{v}"' for v in att_val_items]
                    att_type = f"values: {', '.join(att_val_items)}"
                elif ident in collection:
                    att_type = collection[ident]['type']
                else:
                    att_type = ''

                # Double restrictions ("Facet")
                att_facets = att_def.xpath('./datatype/dataRef/dataFacet')
                if len(att_facets) > 0:
                    if len(att_facets) == 1:
                        if att_facets[0].get('name') == 'minInclusive':
                            att_facet = 'value ≥ ' + att_facets[0].get('value')
                        elif att_facets[0].get('name') == 'minExclusive':
                            att_facet = 'value > ' + att_facets[0].get('value')
                        elif att_facets[0].get('name') == 'maxInclusive':
                            att_facet = 'value ≤ ' + att_facets[0].get('value')
                        elif att_facets[0].get('name') == 'maxExclusive':
                            att_facet = 'value < ' + att_facets[0].get('value')
                    elif len(att_facets) == 2:
                        min_value = att_facets[0].get('value')
                        max_value = att_facets[1].get('value')
                        operator1 = '<' if 'Exclusive' in att_facets[0].get('name') else '≤'
                        operator2 = '<' if 'Exclusive' in att_facets[1].get('name') else '≤'
                        att_facet = f"{min_value} {operator1} value {operator2} {max_value}"
                elif ident in collection:
                    att_facet = collection[ident]['facet']
                else:
                    att_facet = ''

                # Usage
                usage = att_def.get('usage')
                if ident in collection and usage is None:
                    usage = collection[ident]['usage']
                elif ident not in collection and usage is None:
                    usage = 'opt'

                if usage == 'req':
                    usage = 'Required'
                elif usage == 'rec':
                    usage = 'Recommended'
                else:
                    usage = 'Optional'

                collection[ident] = {
                    'text': text,
                    'type': att_type,
                    'facet': att_facet,
                    'usage': usage,
                    #'contraint': ''
                }

            return collection


        collection = {}
        item['attributes'] = get_attributes(spec, collection)

        item['mayContain'] = set(spec.xpath('.//elementRef/@key'))
        class_ref_keys = spec.xpath('.//classRef/@key')
        for key in class_ref_keys:
            item['mayContain'].update(root.xpath(f'//*[name()="classSpec" or name()="elementSpec"]/classes/memberOf[@key="{key}"]/../../@ident'))
        item['mayContain'] = sorted(list(item['mayContain']))

        for ident in item['mayContain']:
            if ident not in contained_by:
                contained_by[ident] = []
            contained_by[ident].append(spec.get('ident'))

        items.append(item)

    for item in items:
        if item['ident'] in contained_by:
            item['containedBy'] = sorted(contained_by[item['ident']])
        else:
            item['containedBy'] = []

    sort_order = {
        'element': 0,
        'atts': 1,
        'model': 2
    }
    items = sorted(items, key=lambda item: item['ident'])
    items = sorted(items, key=lambda item: sort_order[item['type']])

    data = {
        'items': items,
        'version': version,
        'chapters': body_to_chapters(root.xpath('/TEI/text/body')[0])
    }

    with open(r'doc_generator/assets/data.json', 'w') as fp:
        json.dump(data, fp, indent=2)

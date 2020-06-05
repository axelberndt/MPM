<template>
  <div>
    <div class="cursor-pointer" @click.prevent="onClick">
      <div
        class="relative flex items-start px-5 py-3 border-t border-gray-300 hover:bg-gray-100"
        :class="{ 'shadow-md': isOpen }"
      >
        <svg
          v-if="!isOpen"
          xmlns="http://www.w3.org/2000/svg"
          class="w-6 h-6 mt-3"
          aria-hidden="true"
          data-icon="chevron-right"
          data-prefix="fal"
          viewBox="0 0 256 512"
        >
          <path
            fill="currentColor"
            d="M17.525 36.465l-7.071 7.07c-4.686 4.686-4.686 12.284 0 16.971L205.947 256 10.454 451.494c-4.686 4.686-4.686 12.284 0 16.971l7.071 7.07c4.686 4.686 12.284 4.686 16.97 0l211.051-211.05c4.686-4.686 4.686-12.284 0-16.971L34.495 36.465c-4.686-4.687-12.284-4.687-16.97 0z"
          />
        </svg>
        <svg
          v-else
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
          class="w-6 h-6 mt-3"
          data-icon="chevron-down"
          data-prefix="fal"
          viewBox="0 0 448 512"
        >
          <path
            fill="currentColor"
            d="M443.5 162.6l-7.1-7.1c-4.7-4.7-12.3-4.7-17 0L224 351 28.5 155.5c-4.7-4.7-12.3-4.7-17 0l-7.1 7.1c-4.7 4.7-4.7 12.3 0 17l211 211.1c4.7 4.7 12.3 4.7 17 0l211-211.1c4.8-4.7 4.8-12.3.1-17z"
          />
        </svg>
        <div
          class="flex items-center justify-center flex-shrink-0 w-12 h-12 ml-5 rounded-full"
          :class="{
            'bg-green-200 text-green-900': data.type == 'element',
            'bg-red-200 text-red-900': data.type == 'model',
            'bg-blue-200 text-blue-900': data.type == 'atts'
          }"
        >
          <svg
            v-if="data.type == 'element'"
            aria-hidden="true"
            focusable="false"
            data-prefix="fal"
            data-icon="code"
            class="w-6 h-6"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 576 512"
          >
            <path
              fill="currentColor"
              d="M228.5 511.8l-25-7.1c-3.2-.9-5-4.2-4.1-7.4L340.1 4.4c.9-3.2 4.2-5 7.4-4.1l25 7.1c3.2.9 5 4.2 4.1 7.4L235.9 507.6c-.9 3.2-4.3 5.1-7.4 4.2zm-75.6-125.3l18.5-20.9c1.9-2.1 1.6-5.3-.5-7.1L49.9 256l121-102.5c2.1-1.8 2.4-5 .5-7.1l-18.5-20.9c-1.8-2.1-5-2.3-7.1-.4L1.7 252.3c-2.3 2-2.3 5.5 0 7.5L145.8 387c2.1 1.8 5.3 1.6 7.1-.5zm277.3.4l144.1-127.2c2.3-2 2.3-5.5 0-7.5L430.2 125.1c-2.1-1.8-5.2-1.6-7.1.4l-18.5 20.9c-1.9 2.1-1.6 5.3.5 7.1l121 102.5-121 102.5c-2.1 1.8-2.4 5-.5 7.1l18.5 20.9c1.8 2.1 5 2.3 7.1.4z"
            />
          </svg>
          <svg
            v-else-if="data.type == 'model'"
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
            class="w-8 h-8"
            data-icon="cubes"
            data-prefix="fal"
            viewBox="0 0 512 512"
          >
            <path
              fill="currentColor"
              d="M488.6 256.7L388 219V107.9c0-15-9.3-28.4-23.4-33.7l-96-36c-8.1-3.1-17.1-3.1-25.3 0l-96 36c-14.1 5.3-23.4 18.7-23.4 33.7V219L23.4 256.7C9.3 262 0 275.4 0 290.4v101.3c0 13.6 7.7 26.1 19.9 32.2l96 48c10.1 5.1 22.1 5.1 32.2 0L256 418l107.9 54c10.1 5.1 22.1 5.1 32.2 0l96-48c12.2-6.1 19.9-18.6 19.9-32.2V290.4c0-15-9.3-28.4-23.4-33.7zM16.5 403.8V295.1l107.2 46.5v115.8zm231 0l-107.2 53.6V341.6l107.2-46.5zm0-126.7l-115.5 50-115.5-50v-.2L131 234l107.6 39.6 8.9 3.3zm.3-19.7L195 239.6l-54.5-20.4V112.5L247.8 159zM140.5 94.5v-.1L256 51l115.5 43.3v.2l-115.5 50zM264.2 159l107.2-46.5v106.7L317 239.6l-52.8 17.8zm107.6 298.4l-107.2-53.6V295.1l107.2 46.5zm123.7-53.6l-107.2 53.6V341.6l107.2-46.5zm0-126.7l-115.5 50L264.5 277v-.2l8.9-3.3L381 234l114.5 42.9z"
            />
          </svg>
          <svg
            v-else-if="data.type == 'atts'"
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
            class="w-6 h-6"
            data-icon="at"
            data-prefix="fal"
            viewBox="0 0 512 512"
          >
            <path
              fill="currentColor"
              d="M256 8C118.941 8 8 118.919 8 256c0 137.058 110.919 248 248 248 52.925 0 104.68-17.078 147.092-48.319 5.501-4.052 6.423-11.924 2.095-17.211l-5.074-6.198c-4.018-4.909-11.193-5.883-16.307-2.129C346.93 457.208 301.974 472 256 472c-119.373 0-216-96.607-216-216 0-119.375 96.607-216 216-216 118.445 0 216 80.024 216 200 0 72.873-52.819 108.241-116.065 108.241-19.734 0-23.695-10.816-19.503-33.868l32.07-164.071c1.449-7.411-4.226-14.302-11.777-14.302h-12.421a12 12 0 00-11.781 9.718c-2.294 11.846-2.86 13.464-3.861 25.647-11.729-27.078-38.639-43.023-73.375-43.023-68.044 0-133.176 62.95-133.176 157.027 0 61.587 33.915 98.354 90.723 98.354 39.729 0 70.601-24.278 86.633-46.982-1.211 27.786 17.455 42.213 45.975 42.213C453.089 378.954 504 321.729 504 240 504 103.814 393.863 8 256 8zm-37.92 342.627c-36.681 0-58.58-25.108-58.58-67.166 0-74.69 50.765-121.545 97.217-121.545 38.857 0 58.102 27.79 58.102 65.735 0 58.133-38.369 122.976-96.739 122.976z"
            />
          </svg>
        </div>
        <div class="w-full ml-3" :class="{ truncate: !isOpen }">
          <div class="flex items-baseline">
            <h2 class="font-bold">{{ data.ident }}</h2>
            <span class="ml-4">{{ data.gloss[0] }}</span>
          </div>
          <div
            class="text-sm italic text-gray-700"
            :class="{ truncate: !isOpen }"
            v-html="data.desc"
          ></div>
        </div>
      </div>
    </div>
    <div
      v-if="isOpen"
      class="flex text-sm leading-snug border-l-16"
      :class="{
        'border-green-200': data.type == 'element',
        'border-red-200': data.type == 'model',
        'border-blue-200': data.type == 'atts'
      }"
    >
      <div
        class="flex flex-col w-full px-5 pt-3 lg:flex-row"
        :class="{
          'bg-green-100': data.type == 'element',
          'bg-red-100': data.type == 'model',
          'bg-blue-100': data.type == 'atts'
        }"
      >
        <div class="w-full lg:w-2/3 xl:w-3/4">
          <h3
            class="text-sm font-semibold tracking-wide text-gray-700 uppercase"
          >
            Attributes
          </h3>
          <table
            class="mb-3"
            v-if="
              Object.keys(data.attributes).length > 0 &&
                data.attributes.constructor === Object
            "
          >
            <tr v-for="(val, key) in data.attributes" :key="key">
              <td class="justify-start pl-2 text-sm font-semibold align-top">
                @{{ key }}
              </td>
              <td class="w-full px-3 align-top">
                <div v-html="val.text" />
                <div>
                  Usage:
                  <span
                    class="inline-block px-2 py-1 mt-1 mr-2 text-xs font-semibold text-gray-800 rounded-full"
                    :class="
                      val.usage === 'Required' ? 'bg-red-300' : 'bg-green-300'
                    "
                  >
                    {{ val.usage }}
                  </span>
                  Type:
                  <span
                    class="inline-block px-2 py-1 mt-1 text-xs font-semibold text-gray-800 bg-gray-300 rounded-full"
                  >
                    {{ val.type
                    }}<span v-if="val.facet !== ''">, {{ val.facet }}</span>
                  </span>
                </div>
              </td>
            </tr>
          </table>

          <div v-else class="pl-2 mb-3">–</div>

          <div v-if="data.remarks.length > 0" class="mb-3">
            <h3 class="font-semibold tracking-wide text-gray-700 uppercase">
              Remarks
            </h3>
            <p
              v-for="remark in data.remarks"
              :key="remark"
              class="pl-2 mb-1"
              v-html="remark"
            ></p>
          </div>

          <div v-if="data.examples.length > 0" class="mb-3">
            <h3 class="font-semibold tracking-wide text-gray-700 uppercase">
              Examples
            </h3>
            <div
              v-for="example in data.examples"
              :key="example"
              class="ml-2"
              v-html="example"
            ></div>
          </div>
        </div>
        <div class="w-full lg:w-1/3 xl:w-1/4 lg:ml-6">
          <h3 class="font-semibold tracking-wide text-gray-700 uppercase">
            Module
          </h3>
          <div class="ml-2">{{ data.module }}</div>
          <h3 class="mt-2 font-semibold tracking-wide text-gray-700 uppercase">
            Member of
          </h3>
          <div v-if="data.memberOf.length === 0" class="ml-2">–</div>
          <div v-for="member in data.memberOf" :key="member" class="ml-2">
            <a class="underline" :href="'#' + member">{{ member }}</a>
          </div>
          <h3 class="mt-2 font-semibold tracking-wide text-gray-700 uppercase">
            Contained by
          </h3>
          <div v-if="data.containedBy.length === 0" class="ml-2">–</div>
          <div v-for="elem in data.containedBy" :key="elem" class="ml-2">
            <a class="underline" :href="'#' + elem">{{ elem }}</a>
          </div>
          <h3 class="mt-2 font-semibold tracking-wide text-gray-700 uppercase">
            May contain
          </h3>
          <div v-if="data.mayContain.length === 0" class="ml-2">–</div>
          <div v-for="elem in data.mayContain" :key="elem" class="ml-2">
            <a class="underline" :href="'#' + elem">{{ elem }}</a>
          </div>
          <h3
            class="mt-2 mb-3 font-semibold tracking-wide text-gray-700 uppercase"
          >
            <a
              :href="
                `https://raw.githubusercontent.com/axelberndt/MPM/master/src/${data.base}`
              "
              >Schema declaration
              <svg
                aria-hidden="true"
                class="inline w-3 h-3 ml-2 align-baseline"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 512 512"
              >
                <path
                  fill="currentColor"
                  d="M440 256h-16a8 8 0 00-8 8v200a16 16 0 01-16 16H48a16 16 0 01-16-16V112a16 16 0 0116-16h200a8 8 0 008-8V72a8 8 0 00-8-8H48a48 48 0 00-48 48v352a48 48 0 0048 48h352a48 48 0 0048-48V264a8 8 0 00-8-8zM500 0L364 .34a12 12 0 00-12 12v10a12 12 0 0012 12l90-.34.7.71-323.19 323.15a12 12 0 000 17l5.66 5.66a12 12 0 0017 0L477.29 57.34l.71.7-.34 90a12 12 0 0012 12h10a12 12 0 0012-12L512 12a12 12 0 00-12-12z"
                />
              </svg>
            </a>
          </h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MpmItem",
  props: {
    data: {
      type: Object
    }
  },
  data: function() {
    return {
      isOpen: false
    };
  },
  methods: {
    onClick: function() {
      this.isOpen = !this.isOpen;
    }
  }
};
</script>

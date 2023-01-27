# Contributing to MPM

While the seeds of this project were sowed by only a handfull of protagonists, watering and raising it is certainly not reserved to some privileged. If you wish to contribute to MPM's growth do not hesitate. You are very welcome! With the following guidelines we hope to help you and us to orient more easily in the project's organization and formulate contributions fruitfully.


## How can I contribute?

There are several ways to contribute to MPM's development:
- reporting bugs via GitHub [Issues](https://github.com/axelberndt/MPM/issues),
- initiate discussions on code improvements, new features, best practices, guideline improvements etc. via GitHub [Issues](https://github.com/axelberndt/MPM/issues),
- contribute to the codebase and documentation,
- contribute to the sample encodings,
- develop software tools that make usage of MPM and work with it more convenient. We would be happy to learn about and link to them so others can find them more easily.


## Contributing to the Documentation

The encoding guidelines and schema documentation are certainly not perfect or final. If you find anything unclear, insufficient, or have suggestions for improvement, please let us know and post them on the GitHub [Issues](https://github.com/axelberndt/MPM/issues) page so we can discuss them and see how best we can integrate them. We are also looking for tutorials. If you have one, let us know so we can link it or host it on the repository.


## Contributing to the Sample Encodings

The major role of the sample encodings is to complement the encoding guidelines. The sample encodings demonstrate the capabilities of MPM. Users can consult them to see what the XML code looks like and how certain features are applied. Hence, they have to validate against the latest official MPM schema. Each sample encoding should be prepared as an MPM Toolbox project and contain all the necessary data so that any user can load and run it in the [MPM Toolbox](https://github.com/axelberndt/MPM-Toolbox).

To submit a sample encoding, 
1. fork this repository,
2. switch to the `develop` branch and find folder `sample encodings`,
3. inside that `sample encodings` folder add a unique and meaningful named folder that bundles all files of your sample,
4. push it to your repository,
5. click the `compare & pull request` button and create a pull request.

Your encoding will be reviewed internally and, if all is fine, merged into the MPM repository.


## Proposing New Features

MPM's set of performance features is by far not complete. If you wish to propose a new feature issue a discussion, help us figuring out what that feature does and how we can model its characteristics mathematically.

Music theory has lots of terms for lots of performance concepts. But when looking into them more closely, many of them boil down to similar fundamental mechanisms. A new feature makes only sense when it does something unique that another cannot achieve. Please refer to the Rubato section in the encoding guidelines for an example. An important part of MPM's development is a thorough reflection of the performance features before modeling them mathematically. That mathematical model is then a major prerequisite for adding the feature to the format.

Performance features should be as primitive as possible in that they are broken down to their absolute core characteristics. Articulation, e.g., is broken down to the effects that it has to the notes it is applied to, i.e. in comparison to a note that is played as notated without articulation. We identified a series of modifiers that have absolute and relative effects to the notes' attributes, such as duration, velocity and timing changes. Here are two examples of high-level features that MPM does already support, but by means of lower-level features: (1) "Musical agogics" is composed of tempo, rubato, dynamics, and articulation. (2) "Phrasing" is achieved by means of dynamics, tempo and articulation. 

Nontheless, we are also very interested in higher-level performance concepts such as "agogics" and "phrasing". Although these are not the primitive building blocks that make up a performance, they do describe the mechanisms behind it, the aesthetic agenda, from which specific combinations of building blocks derive. They form the knowledge base, the rules which might be used to generate performances that you do not need to create manually in every detail. We regard such more generative application scenarios as a potential future perspective of MPM. Hence, any contribution in this regard is also welcome and will hopefully ultimately lead to new additions to the MPM format. So please do not hesitate to initiate discussions (and perhaps even dedicated research activities) on such subjects.


## Contributing to the Codebase

If you are used to working with TEI ODD and Schematron and want to support us with the MPM codebase, you are welcome. This includes improvements to MPM's current features and validation as well as additions of new performance features. To submit your improvements/additions, 
1. fork this repository,
2. switch to the `develop` branch and make your changes there,
3. push it to your repository,
4. click the `compare & pull request` button and create a pull request.

Your contribution will be reviewed internally and, if all is fine, merged into the MPM repository and, in the course of the next release version, also into the `master` branch. However, we ask you to pay attention to the following remarks.

In order to support readability and ensure smooth interplay with MPM's software tools and `doc_generator`, please adhere to the coding conventions established so far. This includes the following points.
- Element specifications, attribute classes, model classes, and modules are implemented in individual files in the `src/specs/` folder. Feel free to create a subfolder that bundles your new files so they do not get lost in the plethora of files.
- The root document is `src/mpm.odd`. This is the place where these files are integrated in the `<tei:back>` section.
- From MPM version 2.0.0 on we ensure backward compatibility. Any MPM file that validates against version 2.0.0 schema (e.g., all the sample encodings) must also validate against later versions.

There is more to the development of MPM's performance features than meets the eye, as you may have guessed already from reading the previous section (Proposing New Features). 
- New features must be well documented so others can grasp them.
- Each feature is well researched and supported by emprical evidence. New additions should have an equally strong foundation.
- Each feature must be accompanied by a mathematical model that reproduces its characteristics. This is a necessary requirement to integrate it with the official API and performance rendering engine. Prefabricated Java code would help us a lot with this and is very welcome, see the [meico](https://github.com/cemfi/meico) project for more information on this.
- A feature's parameterization should be expressive and easy to understand. The raw mathematical parameters are often not very meaningful in a musical sense. A good example of this is MPM's dynamics model that boils the 8 coordinates of the Bézier curve down to two parameters `curvature` and `protraction`. The parameters should suffice to cover the whole bandwidth of incarnations of the feature. Avoid correlated parameters, i.e. parameters that interact with each other in a way that when one is changed another needs to be adapted. 
- We are very critical about how features interact with each other. Imagine a timing feature that interferes with the tempo and destroys the synchronicity of musical parts that are meant to follow the same global tempo (despite any local micro timing variation). 

We encourage you to involve us early in the development process of a new feature. This gives us the chance for early feedback and being prepared when you come up with your code.

Thank you again for considering to contribute to the Music Performance Markup format!
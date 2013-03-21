Motivation
==========

`PyDev <http://www.pydev.org>`_ is a Python IDE for Eclipse.

Among many useful things it **highlights syntax errors**, allows **code completion** and **code navigation**.
For these to fully work, it is necessary to configure the project's external dependencies appropriately.

This recipe
===========

PyDev adds a new *PyDev Project* to Eclipse.

This `zc.buildout <http://www.buildout.org/>`_ recipe generates the two files that define a PyDev Project:

  ``.project`` and ``.pydevproject``.

Apart from simple project configuration,
the recipe adds the eggs of your choice as external dependencies.
Their transitive dependencies are added as well.

Benefits
--------

1. Usually the PyDev Project files ``.project`` and ``.pydevproject`` are not good candidates for versioning.
   The reason is that these can easily contain user specific information, like personal directory paths.
   This recipe allows you to version, in a buildout file, the information necessary to generate these files.

2. Configuring the PyDev Project external dependencies by hand is neither clear not easy.

3. Users of Maven and Eclipse JDT might find this project build generation very familiar. *(Don't use Java? I thought every Eclipse user did.)*

Usage
-----

Add your recipe configuration to ``buildout.cfg`` and include it in ``${buildout:parts}``. An example::

    [buildout]
    ...
    parts = ... pydevproject

    [pydevproject]
    recipe = collective.recipe.pydevproject
    name = my_project_name
    src = src
    python-version = python 2.7
    python-interpreter = Default
    eggs = any_egg_you_want
    extra-paths =
        /some/path
        ${buildout:directory}/some/library
        ${buildout:directory}/lib/*

Options
-------
These match the options of a PyDev Project.

name
  The project name. This is just for Eclipse and can be anything you want.
src
  The source folder, relative to the root of the project. Usually *src*. *(TODO: get this from ${buildout:develop} and setup.py)*
python-version
  The combination of interpreter and grammar version. E.g. *python 2.7*
python-interpreter
  The interpreter name, as configured in the the Eclipse Preferences for PyDev. Usually *Default* is fine.

  Remember to register at least one interpreter in Eclipse before using your project. That can be done in ``Window > Preferences > PyDev > Interpreter - Python > New...``.
extra-paths
  Extra paths to add to the Python path. Each path should be on a separate line. Paths may contain wildcards (*), these are evaluated upon install.
eggs
  The eggs that will be listed as external dependencies.
  You don't need to include transitive dependencies. This is done automatically.

Source
------

Source code lives at http://github.com/collective/collective.recipe.pydevproject.

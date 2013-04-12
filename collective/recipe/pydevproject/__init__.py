# -*- coding: utf-8 -*-
import zc.buildout
import zc.recipe.egg
import copy
import glob
import xml.etree.ElementTree as ET


class Recipe:

    def __init__(self, buildout, name, options):
        self.options = options
        self.src_absolute_path = '%s/%s' % (buildout['buildout']['directory'], buildout[name]['src'])
        self.egg = zc.recipe.egg.Scripts(buildout, name, options)
        self.extra_paths = options['extra-paths'].split()
        if options.get('python_version', None) and not options.get('python-version', None):
            print("python_version is deprecated, use python-version instead.")
            self.options['python-version'] = options['python_version']
        if options.get('python_interpreter', None) and not options.get('python-interpreter', None):
            print("python_interpreter is deprecated, use python-interpreter instead.")
            self.options['python-interpreter'] = options['python_interpreter']


    def install(self):
        requirements, ws = self.egg.working_set()
        external_deps_paths=[f.location for f in ws]
        # src should not be count as an external dependency
        if self.src_absolute_path in external_deps_paths:
            external_deps_paths.remove(self.src_absolute_path)

        for path in copy.copy(self.extra_paths):
            if '*' in path:
                self.extra_paths.remove(path)
                self.extra_paths += glob.glob(path)

        project = ET.Element("projectDescription")
        ET.SubElement(project, "name").text = self.options['name']
        ET.SubElement(project, "comment")
        ET.SubElement(project, "projects")
        build_spec = ET.SubElement(project, "buildSpec")
        build_cmd = ET.SubElement(build_spec, "buildCommand")
        ET.SubElement(build_cmd, "name").text = "org.python.pydev.PyDevBuilder"
        ET.SubElement(build_cmd, "arguments")
        natures = ET.SubElement(project, "natures")
        ET.SubElement(natures, "nature").text = "org.python.pydev.pythonNature"
        ET.ElementTree(project).write('.project', "UTF-8")

        # TODO: add header: "<?eclipse-pydev version="1.0"?>"
        pydev_project = ET.Element("pydev_project")
        path_property = ET.SubElement(pydev_project, "pydev_pathproperty")
        path_property.attrib['name'] = "org.python.pydev.PROJECT_SOURCE_PATH"
        for src in self.options['src'].split():
            ET.SubElement(path_property, "path").text = \
                "/{name}/{src}".format(name=self.options['name'], src=src)
        py_version = ET.SubElement(pydev_project, "pydev_property",
                                name="org.python.pydev.PYTHON_PROJECT_VERSION")
        py_version.text = self.options['python-version']
        py_interpreter = ET.SubElement(pydev_project, "pydev_property",
                            name="org.python.pydev.PYTHON_PROJECT_INTERPRETER")
        py_interpreter.text = self.options['python-interpreter']
        libs = ET.SubElement(pydev_project, "pydev_pathproperty",
                        name="org.python.pydev.PROJECT_EXTERNAL_SOURCE_PATH")
        for path in external_deps_paths + self.extra_paths:
            ET.SubElement(libs, "path").text = path
        ET.ElementTree(pydev_project).write('.pydevproject', 'UTF-8')
        return ()

    update = install

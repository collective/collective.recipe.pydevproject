# -*- coding: utf-8 -*-
import logging, os, zc.buildout
import zc.recipe.egg
import shutil


class Recipe:

    def __init__(self, buildout, name, options):
        self.name, self.options = name, options
        self.egg = zc.recipe.egg.Scripts(buildout, name, options)

    def install(self):
        requirements, ws = self.egg.working_set()
        pathlist=[f.location for f in ws]
        print pathlist
        return ()

    update = install


def remove_dir(path):
    "removes recursively directory at path, if it exists"
    if os.path.exists(path):
        shutil.rmtree(path)

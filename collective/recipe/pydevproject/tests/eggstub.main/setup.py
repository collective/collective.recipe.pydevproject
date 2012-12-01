from setuptools import setup

setup(name='eggstub.main',
      install_requires=[
          'eggstub.dep', #### THIS EGG DEPENDS ON ANOTHER ####
      ],
      )

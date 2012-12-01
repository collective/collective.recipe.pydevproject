from setuptools import setup

setup(name='eggstub.main',
      package_dir = {'': 'src'},
      install_requires=[
          'eggstub.dep', #### THIS EGG DEPENDS ON ANOTHER ####
      ],
      )

from setuptools import setup, find_packages
import os

name = "collective.recipe.pydevproject"
version = '0.2.dev0'

read = lambda f: open(f).read()

long_description = """
========================
 Detailed Documentation
========================
%s

================
 Change history
================
%s

==============
 Contributors
==============
%s
""" % (read('README.rst'),
       read('CHANGES.txt'),
       read('CONTRIBUTORS.txt'),)

install_requires=['setuptools', 'zc.buildout', 'zc.recipe.egg'],
tests_require=['zope.testing', 'zc.buildout>=1.6.3', 'zc.recipe.egg'],

setup(
    name=name,
    version=version,
    description="zc.buildout recipe that creates an Eclipse PyDev Project config with PYTHONPATH pointing to some eggs and their dependencies",
    long_description=long_description,
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ],
    keywords='buildout eggs eclipse pydev',
    author="Marcio Mazza",
    author_email="marciomazza@gmail.com",
    url='http://pypi.python.org/pypi/collective.recipe.pydevproject',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.recipe'],
    include_package_data=True,
    zip_safe=False,
    package_dir={'':'.'},
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=dict(tests=tests_require),
    test_suite='collective.recipe.pydevproject.tests.test_docs.test_suite',
    entry_points={'zc.buildout': ['default = %s:Recipe' % name]},
    )

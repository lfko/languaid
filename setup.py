'''
    Created on Jan 8, 2019

    @author: fb
    @summary: 
'''

try:
    from setuptools import setup, Extension, Command, find_packages
except ImportError:
    from distutils.core import setup, Extension, Command

with open("README.MD", "r") as fh:
    long_description = fh.read()

VERSION = '0.0.1'
DESCRIPTION = "A tool providing support when learning a language"

PYTHON_REQUIRES = '>=2.5, !=3.0.*, !=3.1.*, !=3.2.*'

# package name is python, because it is the upmost package in the source folder tree
setup(
        name="LanguAid",
        version=VERSION,
        description=DESCRIPTION,
        long_description=long_description,
        python_requires=PYTHON_REQUIRES,
        author="Florian Becker",
        author_email="lefko@inbox.lv",
        url="https://github.com/lfko/languaid",
        packages=find_packages(exclude=('python.languaid.test',)),
        scripts=['run_app.sh'],
        platforms=['linux'])

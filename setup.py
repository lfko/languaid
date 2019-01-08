'''
    Created on Jan 8, 2019

    @author: fb
    @summary: 
'''

# from distutils.command.build_ext import build_ext
# from distutils.errors import CCompilerError, DistutilsExecError, DistutilsPlatformError

try:
    from setuptools import setup, Extension, Command
except ImportError:
    from distutils.core import setup, Extension, Command

VERSION = '0.0.1'
DESCRIPTION = "A tool providing support when learning a language"

PYTHON_REQUIRES = '>=2.5, !=3.0.*, !=3.1.*, !=3.2.*'

# package name is python, because it is the upmost package in the source folder tree
setup(
        name="LanguAid",
        version=VERSION,
        description=DESCRIPTION,
        python_requires=PYTHON_REQUIRES,
        author="Florian 'lefko' Becker",
        url="https://github.com/lfko/languaid",
        packages=['python'],
        platforms=['any'])

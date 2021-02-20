from distutils.core import setup, Extension

setup(name='c_rename', version='1.0', \
    ext_modules=[Extension('c_rename', ['c_extensions/rename.c'])])

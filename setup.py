from setuptools import setup

from Cython.Build import cythonize

setup(

    ext_modules = cythonize(["main_c.pyx"])

)

#python setup.py build_ext --inplace
 
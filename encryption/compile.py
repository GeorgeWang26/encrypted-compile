# python3 compile.py build_ext --inplace

# from distutils.core import setup
# from distutils.extension import Extension
from setuptools import setup
from setuptools.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("aes_decrypt", ["aes_decrypt.py"]),
    Extension("aes_wraper", ["aes_wraper.py"])
]

for e in ext_modules:
    e.cython_directives = {'language_level': "3"} # all are Python-3

setup(
    name = 'aes_encryption_with_compile',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)

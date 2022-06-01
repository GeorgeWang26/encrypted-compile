from setuptools import setup
from setuptools.extension import Extension
from Cython.Distutils import build_ext


ext_modules = [
    Extension("aes_decrypt", ["aes_decrypt.py"])
]

for e in ext_modules:
    e.cython_directives = {'language_level': "3"} # all are Python-3

setup(
    name = 'aes compile',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
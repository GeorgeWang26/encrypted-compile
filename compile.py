from setuptools import setup
from setuptools.extension import Extension
from Cython.Distutils import build_ext


f = open("compileList.txt", "r")
lst = f.readlines()
ext_modules = []
for src_file in lst:
    src_file = src_file[:-1]
    ext_modules.append(Extension("lib_" + src_file, ["src_" + src_file + ".py"]))

for e in ext_modules:
    e.cython_directives = {'language_level': "3"} # all are Python-3

setup(
    name = 'auto compile',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
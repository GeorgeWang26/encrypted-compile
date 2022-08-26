# **Compile Python**
Use cython to translate python files into C then compile it. Used to protect source code in distribution

## **Executable** ##
install cython3 `sudo apt-get install -y cython3` \
add `#cython: language_level=3` at the top of .py so cython uses python3 to compile into executable
```
cython3 --embed -o hello.c hello.py
gcc -Os -I /usr/include/python3.x -o hello hello.c -lpython3.x -lpthread -lm -lutil -ldl     # x is the version of python, 3.8 (NOT 3.8.10)
./hello
```
`gcc <C_file_from_cython> -I<include_directory> -L<directory_containing_libpython> -l<name_of_libpython_without_lib_on_the_front> -o <output_file_name>`

## **Shared library (.so)**
Run compile.py in same directory or parent directory, because running cython in child directory can cause path errors when referencing to target .py file with "../"

In compile.py (will generate .so file)
```
# legacy library
# from distutils.core import setup
# from distutils.extension import Extension
from setuptools import setup
from setuptools.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("say_hello", ["hello.py"]) # the generated file will be say_hello.so
]

for e in ext_modules:
    e.cython_directives = {'language_level': "3"} # all are Python-3

setup(
    name = 'My_Program_Name',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
```

run `python3 compile.py build_ext --inplace` to get .so files \
In main.py (wrapper used to execute .so files)
```
from say_hello import hi

hi() # suppose hi() is a function in say_hello.so, which is originally hello.py
```

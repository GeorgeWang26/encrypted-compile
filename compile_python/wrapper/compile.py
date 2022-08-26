from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


ext_modules = [
    # Extension("say_hello",  ["hello.py"]),
    Extension("gps_publisher", ["gps/gps_publisher.py"]),
    Extension("gps_subscriber", ["gps/gps_subscriber.py"])
]

for e in ext_modules:
    e.cython_directives = {'language_level': "3"} #all are Python-3

setup(
    name = 'hello_and_gps',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)

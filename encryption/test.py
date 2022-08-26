import os


import os

rootdir = "/home/ubuntu/Desktop/CoolStuff/cypher_encryption"

for path, subdirs, files in os.walk(rootdir):
    print(path)
    print(subdirs)
    print(files)
    print("------------------")

print("\n\n\n")
l = []
for d in os.scandir(rootdir):
    if d.is_dir():
        l.append(d.path)
print(l)

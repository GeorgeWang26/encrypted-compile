# ROS2 Autocompile
This script will remove all the cpp packages from the workspace. For Python packages, verification script will be added to the beginning of all files and compiled. A python wrapper will be created for each source file, and the source code will be moved to ws/backup.

## Requirement
map /data in the container to somewhere on host machine, this will be the place to store the encrypted verification data at /data/encrypted. With volume, this data will stay the same in future updates with new containers.

## Instruction
1. install all python dependencies for encryption and compiling. `pip3 install setuptools cython pycryptodome getmac`
2. navigate to your ros2 workspace and clone the repo, make sure all files are in ws/
```
git clone https://github.com/indro-robotics/ros2_autocompile.git tmp/
mv tmp/* ./
rm -rf tmp
```
3. generate device specific encrypted data for verification. `python3 aes_encrypt.py`
4. generate .so library file for decryption. `python3 aes_compile.py build_ext --inplace`
5. run the auto compile script. `sudo bash bauto.bash`

## Clean up
1. Navigate to ros2 workspace, remove backed up source files in backup/ after all modules are tested to be working. `rm -r backup/ build/temp*`
2. Remove aes related files and the auto script. `rm aes* compile.py bauto.bash README.md`

Now the device is ready for shipping.

# ROS2 Autocompile
This script will remove all the cpp packages from the workspace. For Python packages, verification script will be added to the beginning of all files and compiled. A python wrapper will be created for each source file, and the source code will be moved to ws/backup.

## Instruction
1. install all python dependencies for encryption and compiling. `pip3 install setuptools cython pycryptodome getmac`
2. navigate to your ros2 workspace and clone the repo, make sure all files are in ws/ `git clone https://github.com/indro-robotics/ros2_autocompile.git .`
2. generate device specific encrypted data for verification. `python3 aes_encryption.py`
3. generate .so library file for decryption. `python3 aes_compile.py build_ext --inplace`
4. run the auto compile script. `sudo bash bauto.bash`

## Clean up
1. Navigate to ros2 workspace, remove the backup/ after all modules are tested to be working. `rm -r backup/`
2. Remove aes related files. `rm aes*`
3. Remove compile.py, auto script and readme. `rm compile.py bauto.bash README.md`

Now the device is ready for shipping.
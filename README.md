# ROS2 Autocompile
This script will remove all the cpp packages from the workspace. For Python packages, verification script will be added to the beginning of all files and compiled. A python wrapper will be created for each source file, and the source code will be moved to ws/backup.

## Requirement
1. map volume `/data:/data`, this will be the place to store the encrypted verification data at `/data/encrypted`. With mapped volume, this data will stay the same in future updates when using new containlers.
2. map volume `/proc/device-tree:/Indro:ro` when on arm64 (ie: jetson) Must make this mounted volume read only since they are crucial system files on host machine.
3. run with `--privileged` on x86
4. run docker with `--network host` to get host mac address inside docker
```
arm64: docker run -v /data:/data /proc/device-tree:/Indro:ro --network host img
x86: docker run -v /data:/dara --priviliged --network host img
```
## Instruction
navigate to your ros2 workspace and clone the repo, make sure all files are in ws/
```
git clone https://github.com/indro-robotics/ros2_autocompile.git tmp/
mv tmp/* ./
rm -rf tmp
pip3 install -r requirements.txt
```
3. generate device specific encrypted data for verification. `python3 aes_encrypt.py` **NOTE: this should run on host, not in container**
4. generate .so library file for decryption. `python3 aes_compile.py build_ext --inplace`
5. run the auto compile script. `sudo bash bauto.bash`

## Clean up
1. Navigate to ros2 workspace, remove backed up source files in backup/ after all modules are tested to be working. `rm -r backup/ build/temp*`
2. Remove aes related files and the auto script. `rm aes* compile.py bauto.bash README.md requirements.txt`

Now the device is ready for shipping.

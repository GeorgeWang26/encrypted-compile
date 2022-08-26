# AES encryption
This program is used to prevent source code from running on unauthorized devices `pip3 install pycryptodome getmac`

## Supported functions
Under aes.py, there are four functions
* `get_password()` - generate device specific password for AES encryption
* `encrypt()` - encrypt a plaintext data with the password (related to the certified device) and store the encrypted data at a specific location
* `decrypt()` - obtain the password relative to the current device, and use it to decrypt the pre-stored data
* `verify()` - checks if the decrypted data is the same as the original plaintext data. If yes, program continues, otherwise program terminates immediately

## Steps
1. Use `encrypt()` to store the encrypted data before distributing the hardware device
2. Import aes.py and call `verify()` in the beginning of all protected files to restrict access to the programs
3. Add protected files to compile.py and run `python3 compile.py build_ext --inplace` to generate .so files
4. Only distribute the .so files with a python wraper to start the program (ex: main.py)

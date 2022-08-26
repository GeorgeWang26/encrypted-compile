# use AES GCM-256 for encryption

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from getmac import get_mac_address as gma
import subprocess
from os import path


data = "Hello ambitious and dedicated hackers, is knowing the plain text going to help in this case? -George.W"
file_location = "/data/encrypted"

def get_password():
    cpu_archetecture = subprocess.Popen("uname -m", shell=True, stdout=subprocess.PIPE).stdout.read().decode()[:-1]
    if cpu_archetecture == "aarch64":
        device_tree = "/proc/device-tree/"
        if path.exists("/Indro"):
            device_tree = "/Indro/"
        serial = subprocess.Popen("cat " + device_tree + "serial-number", shell=True, stdout=subprocess.PIPE).stdout.read().decode()[:-1]
        uuid = subprocess.Popen("cat " + device_tree + "chosen/uuid", shell=True, stdout=subprocess.PIPE).stdout.read().decode()[:-1]
    elif cpu_archetecture == "x86_64":
        serial = subprocess.Popen("sudo dmidecode -t system | grep Serial", shell=True, stdout=subprocess.PIPE).stdout.read().decode()[16:-1]
        uuid = subprocess.Popen("sudo dmidecode -t system | grep UUID", shell=True, stdout=subprocess.PIPE).stdout.read().decode()[7:-1]
    else:
        print("===================== ERROR: unrecognized cpu archetecture =====================")
        quit()
    pwd = gma() + serial + uuid
    # pwd = serial + uuid
    # print("password:", pwd)
    return pwd

def encrypt():
    salt = get_random_bytes(32)
    key = scrypt(get_password(), salt, key_len=32, N=2**20, r=8, p=1)  # work facrtor N can be from 2^14 to 2^20, change based on time cost
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    with open(file_location, "wb") as f:
        f.writelines([salt, cipher.nonce, ciphertext, tag])
        f.close()

if __name__ == "__main__":
    encrypt()

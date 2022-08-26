# use AES GCM-256 for encryption

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from getmac import get_mac_address as gma
import subprocess
from os import path


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
    # print("password:", pwd)
    return pwd

def decrypt():
    f = open(file_location, "rb")
    text = f.read()
    f.close()
    salt = text[:32]
    nonce = text[32:48]
    ciphertext = text[48:-16]
    tag = text[-16:]

    try:
        key = scrypt(get_password(), salt, key_len=32, N=2**20, r=8, p=1)
        # fake_key = get_password() + "**********"
        # key = scrypt(fake_key, salt, key_len=32, N=2**20, r=8, p=1)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        msg = cipher.decrypt(ciphertext).decode()
        cipher.verify(tag)
        print("verification success\n-------------------------------------------------------\n")
    except UnicodeDecodeError as e:
        print("\n\n==============================\ninvalid credential\n==============================\n\n")
        quit()
    except ValueError as e:
        print("\n\n==============================\ntag verification (or other value error) failed\n==============================\n\n")
        quit()
    except Exception as e:
        print("\n%s\n==============================\nunknown verification failed\n==============================\n\n" % e)
        quit()

if __name__ == "__main__":
    decrypt()

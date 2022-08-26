# encryption & decryption equation from https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
# plain text MUST be longer than key
# two different keys with same leading charatcers can behave the same on shorter plain text

from getmac import get_mac_address as gma
import subprocess


plain_text = "JKASHDLSADHAWEN<MM<ICUPEJBWHJLQJH:OIE@*(#_!*$!@U$B!@Y$_(*!@&JHJ#K!B#I!@*)(#"

def get_key():
    s = subprocess.Popen("sudo dmidecode -t system | grep UUID", shell=True, stdout=subprocess.PIPE).stdout.read()
    s = s.decode()[7:-1]
    print(s)
    key = gma() + s
    print(key)
    return key

def vigenere_cipher(key, string, act):
    parsed_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        if act == "e":
            parced_c = chr(ord(string[i]) + ord(key_c) % 256)
        elif act == "d":
            parced_c = chr((ord(string[i]) - ord(key_c)) % 256)
        else:
            print("invalid action")
            return
        parsed_chars.append(parced_c)
    parced_string = "".join(parsed_chars)
    return parced_string

with open("encrypted", "w") as f:
    e = vigenere_cipher(get_key(), plain_text, "e")
    f.write(e)
    f.close()
    print(len(e), len(plain_text))

with open ("encrypted", "r") as f:
    d = vigenere_cipher(get_key(), f.read(), "d")
    print(d)
    print(d == plain_text, "\n================================")

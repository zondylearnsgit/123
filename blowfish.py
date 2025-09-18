# pip install pycryptodome
from Crypto.Cipher import Blowfish 
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def Blowfish_encrypt(plaintext_bytes, key8):
    iv = get_random_bytes(8)
    cipher = Blowfish.new(key8, Blowfish.MODE_CBC, iv)
    ct = cipher.encrypt(pad(plaintext_bytes, 8))
    return iv + ct  # prepend IV

def Blowfish_decrypt(iv_ct, key8):
    iv = iv_ct[:8]
    ct = iv_ct[8:]
    cipher = Blowfish.new(key8, Blowfish.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), 8)

# example
if __name__ == "__main__":
    key = b'8bytekey'  # must be 8 bytes
    pt = b"Secret message for Blowfish"
    ct = Blowfish_encrypt(pt, key)
    print("cipher (hex):", ct.hex())
    print("decrypted:", Blowfish_decrypt(ct, key))

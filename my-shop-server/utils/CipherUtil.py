from base64 import b64encode, b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESClassicCipher:

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = bytes(key, 'utf-8')
        self.mode = AES.MODE_CBC

    def encrypt(self, data):
        cipher = AES.new(self.key, self.mode)
        ct_bytes = cipher.encrypt(pad(bytes(data, 'utf-8'), self.bs))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        return ct + '.' + iv

    def decrypt(self, data):
        try:
            b64_ct_iv = data.split('.')
            iv = b64decode(b64_ct_iv[1])
            ct = b64decode(b64_ct_iv[0])
            cipher = AES.new(self.key, self.mode, iv)
            plaintext = unpad(cipher.decrypt(ct), self.bs)
            return plaintext.decode('utf-8')
        except (ValueError, KeyError) as err:
            print("Incorrect decryption ", err)
            return None




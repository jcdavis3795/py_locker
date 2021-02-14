from cryptography.fernet import Fernet
import os

class Crypto:
    def __init__(self):
        self.encrypt_inp = ""
        self.encrypt_out = ""
        self.decrypt_inp = ""
        self.decrypt_out = ""

    # function to encrypt the data of a specified file, and send the encrypted data to a second specified file
    def encrypt_file(self, inp, out):

        self.encrypt_inp = inp
        self.encrypt_out = out

        # reads the key we have generated in key.key
        with open("H:\code\py_locker\docs\key.key", "rb") as f:
            key = f.read()

        with open(inp, 'rb') as f:  # reads original file
            data = f.read()

        # encrypts the contents of original file
        k = Fernet(key)
        encrypted = k.encrypt(data)

        # passes the encrypted data into specified output file
        with open(out, 'wb') as f:
            f.write(encrypted)
        f.close()

        # deletes the non encrypted file
        os.remove(inp)

    # function to decrypt the contents of an encrypted file, and send the decrypted data to a second specified file
    def decrypt_file(self, inp, out):

        self.decrypt_inp = inp
        self.decrypt_out = out

        with open("H:\code\py_locker\docs\key.key", "rb") as f:
            key = f.read()
        with open(inp, "rb") as f:
            data = f.read()

        # decrypts the contents of original file
        k = Fernet(key)
        decrypted = k.decrypt(data)

        # passes decrypted data into specified output file
        with open(out, 'wb') as f:
            f.write(decrypted)
        f.close()

        # deletes the original encrypted file
        os.remove(inp)
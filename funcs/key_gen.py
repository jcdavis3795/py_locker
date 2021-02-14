from cryptography.fernet import Fernet


def key_gen():
    # Generate a key and save to a file named key.key. You only need to use this once, when you originally create
    # the key.key file. This is the key to both encrypt and decrypt the file, so If you lose this key while my_passwords
    # is encrypted, you will not be able to decrypt it

    key = Fernet.generate_key()

    file = open("H:\code\py_locker\docs\key.key", "wb")
    file.write(key)
    file.close()


def key_read():
    # read the key created in key.key and assign it to a variable

    file = open("H:\code\py_locker\docs\key.key", "rb")
    key = file.read()
    file.close()

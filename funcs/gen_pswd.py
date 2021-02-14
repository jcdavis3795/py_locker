# function to generate a password of random characters from a specified length between 16 - 32
def gen_pswd(x):
    import string
    import random

    characters = string.ascii_letters + string.digits + string.punctuation

    if x in range(16, 33):
        return "".join((random.choice(characters)) for i in range(x))
    else:
        print('Enter a password length between 16 and 32')

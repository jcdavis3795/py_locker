from funcs import crypto_class, read, gen_pswd, create_entry
import pyperclip
import sys

crypto = crypto_class.Crypto()
try:
    crypto.decrypt_file('H:\code\py_locker\docs\my_passwords.encrypted', 'H:\code\py_locker\docs\my_passwords.decrypted')
except FileNotFoundError:
    pass

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print( 'Usage:\npython3 locker.py [create] [service] [password length] - generates a password for a specified '
               'service and stores it in the locker \n'
               'python3 locker.py input [service] [password] - input a service and password you already know'
               'python3 locker.py generate [password length] - generates a password of specified length between 16 -32 '
               'and copied to clipboard'
               '\n'
               'python3 locker.py read [service] - copies account password to clipboard \n'
               'python3 locker.py key - will generate a new fernet key to store in key.key'
               'python3 locker.py decrypt - if the my_passwords file is currently encrypted, this will decrypt it \n'
               'python3 locker.py encrypt - if the my_passwords file is currently decrypted, this will encrypt it')
        sys.exit()

    if sys.argv[1] == 'create':
        create_entry.create_entry(sys.argv[2], gen_pswd.gen_pswd(int(sys.argv[3])))
        print('Entry creation successful')
        sys.exit()
        
    if sys.argv[1] == 'input':
        create_entry.create_entry(sys.argv[2], sys.argv[3])
        print('Input successful')
        sys.exit()   
        
    if sys.argv[1] == 'generate':
        password = gen_pswd.gen_pswd(int(sys.argv[2]))
        pyperclip.copy(password)
        print('new password copied to clipboard')
        print(password)
        sys.exit()

    if sys.argv[1] == 'read':
        read.print_dict(sys.argv[2])
        sys.exit()
        
    if sys.argv[1] == 'key':
        try:
            crypto.decrypt_file('H:\code\py_locker\docs\my_passwords.encrypted',
                                'H:\code\py_locker\docs\my_passwords.decrypted')
        except FileNotFoundError:
            response = input('are you sure you want to replace your fernet key? (y/n)')
            if response == 'y':
                key_gen.key_gen()
            else:
                print('key generation aborted')
                
    if sys.argv[1] == 'encrypt':
        try:
            crypto.encrypt_file('H:\code\py_locker\docs\my_passwords.decrypted', 'H:\code\py_locker\docs\my_passwords.encrypted')
            print('passwords encrypted')
            sys.exit()
        except FileNotFoundError:
            print('Your file is already encrypted, or the file cannot be found')
            sys.exit()

    if sys.argv[1] == 'decrypt':
        try:
            crypto.decrypt_file('H:\code\py_locker\docs\my_passwords.encrypted', 'H:\code\py_locker\docs\my_passwords.decrypted')
            print('passwords decrypted')
            sys.exit()
        except FileNotFoundError:
            print('Your file is already decrypted, or the file cannot be found')
            sys.exit()

# py_locker

SUMMARY:

  This program acts as both a password generator and a locker. You can store passwords for services/websites, or generate new passwords 16-32
characters in length. This data is stored in ..\docs\my_passwords.decrypted. I have left a few mock examples in the file to demonstrate how it works.

This program also has the ability to encrypt the my_passwords file using a fernet key (a type of symmetric encryption). You will generate this key by calling
the key_gen() function in the key_gen module. This key will be stored in ..\docs\key.key. Only call key_gen() once - if you encrypt a file with a key and then
change the key, you will not be able to decrypt the locker. If you need to change the key, only call key_gen() while the my_passwords file is decrypted.
You can also create this key from the command line with the 'key' command, which will ensure your file is decrypted.
You run this program the way you would normally run a python script from the command line, followed by some additional argument options.

USAGE:

The command options for this program are: 

create
input
generate
read
key
decrypt
encrypt

The usage for these commands(in Windows) are as follows:

*from the py_locker directory*

python3 locker.py create [service] [password length] - generates a password for a specified service and stores it in the locker

python3 locker.py input [service] [password] - input a service and password you already know

python3 locker.py generate [password length] - generates a password of specified length between 16 -32 and copied to clipboard

python3 locker.py read [service] - copies account password to clipboard

python3 locker.py key - will generate a new fernet key to store in key.key

python3 locker.py decrypt - if the my_passwords file is currently encrypted, this will decrypt it

python3 locker.py encrypt - if the my_passwords file is currently decrypted, this will encrypt it

  Running the program without arguments will return a the command option list as well.
The my_passwords file is automatically encrypted after each use, the encrypt and decrypt commands are there in case something unexpected happens. If you want 
to know how everything works, the files have all been commented explaining the use and purpose of each function.

RUNNING FOR THE FIRST TIME:

  The first thing you will want to do when running locker.py for the first time is is call the 'key' command. This will generate your fernet key in key.key. After doing this, you can use all the other features of the program normally. Not generating a key first will cause the program to not function.

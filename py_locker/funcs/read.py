import pyperclip


# function to transform a line into a dictionary object
def parse(line):

    dictionary = dict()

    pairs = line.strip('{}').split(', ')
    for i in pairs:
        pair = i.split(': ')

        dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
    return dictionary


# open the file and read each pair into a dictionary object, which is stored in a list. We can later use this list to
# find our search for passwords
try:

    with open('H:\code\py_locker\docs\my_passwords.decrypted', 'r') as r:
        data = []
        lines = r.read().split('\n')
        for i in lines:
            if i != '':
                dictionary = parse(i)
                data.append(dictionary)
            r.close()
except FileNotFoundError:
    print('Cannot find file to parse')


# this is the search function that will return the password for the specified service. If you have more than one
# password for any given service they will all be printed, but only the last one will be copied to the clipboard
def print_dict(service):

    for x in data:
        if service in x.keys():
            password = (x[service])
            pyperclip.copy(password)
            print(password)
            print('password copied to clipboard')



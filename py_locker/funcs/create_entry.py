# function for creating a dictionary object relating service to password, which will be stored in our my_passwords file
# for later retrieval
def create_entry(service, password):
    import json
    locker = {}

    locker.update({service: password})

    json = json.dumps(locker)

    with open('H:\code\py_locker\docs\my_passwords.decrypted', 'a') as f:
        f.write(json)
        f.write('\n')
        f.close()
import os
import time
from colorama import Fore, init

init(convert=True)
storage = []
banner = (fr'''{Fore.RED}

   _____ __  __          _____ _        _____        _     _______   _      _    
  / ____|  \/  |   /\   |_   _| |      |  __ \      | |   |__   __| (_)    | |   
 | |  __| \  / |  /  \    | | | |      | |  | | ___ | |_     | |_ __ _  ___| | __
 | | |_ | |\/| | / /\ \   | | | |      | |  | |/ _ \| __|    | | '__| |/ __| |/ /
 | |__| | |  | |/ ____ \ _| |_| |____  | |__| | (_) | |_     | | |  | | (__|   < 
  \_____|_|  |_/_/    \_\_____|______| |_____/ \___/ \__|    |_|_|  |_|\___|_|\_\


    {Fore.RESET}''')
print(banner)


def ask_username():
    while True:
        username = input("Enter Email Address: ")
        if username:
            break
    return username


def alias_generator(address, index):
    global storage
    for _index in range(index, len(address)):
        unique_address = address[:_index] + '.' + address[_index:]
        storage.append(unique_address)
        alias_generator(unique_address, _index + 2)
    return storage


user_input = ask_username().replace(".", "").split('@')
original_email = user_input[0]
if len(user_input) == 2:
    original_extension = user_input[-1]
else:
    original_extension = ''

alias_generator(original_email, 1)

with open('result.txt', 'w', encoding='utf-8') as fp:
    fp.write(f'@{original_extension}\n'.join(storage) + f'@{original_extension}\n')

os.system('cls')
print(banner)
print("Ok, I Did My Job Goodbye")
time.sleep(2)

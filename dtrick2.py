
import time, os, colorama
from colorama import Fore, init
from time import sleep
init(convert=True)
storage = []
banner = (f'''{Fore.RED}
    
   _____ __  __          _____ _        _____        _     _______   _      _    
  / ____|  \/  |   /\   |_   _| |      |  __ \      | |   |__   __| (_)    | |   
 | |  __| \  / |  /  \    | | | |      | |  | | ___ | |_     | |_ __ _  ___| | __
 | | |_ | |\/| | / /\ \   | | | |      | |  | |/ _ \| __|    | | '__| |/ __| |/ /
 | |__| | |  | |/ ____ \ _| |_| |____  | |__| | (_) | |_     | | |  | | (__|   < 
  \_____|_|  |_/_/    \_\_____|______| |_____/ \___/ \__|    |_|_|  |_|\___|_|\_\


    {Fore.RESET}''')
print (banner)

def Clear():
    os.system('cls')

def ask_username():
    username = ""
    while not username:
        temp = input(" > Enter your gmail username (NOT FULL EMAIL) ")
        if "@" in temp:
            Clear()
            print(banner)
            print(" > omg bro ur actually retarded JUST YOUR USERNAME BEFORE THE FUCKING @")
            time.sleep(1.5)
        else:
            Clear()
            print(banner)

            username = temp
    return username


def shuffle(obj, init_pos):
    global storage
    temp = ""
    for i in range(init_pos, len(obj)):
        temp = obj[:i] + "." + obj[i:]
        if temp not in storage:
            if ".." not in temp:
                storage.append(temp)
                shuffle(temp, init_pos+2)
    return storage

target = ask_username().replace(".", "")
shuffle(target, 1)
file = open('result.txt', 'w')
for i in storage:
    temp = str(i) + "@gmail.com"
    file.write(temp)
    file.write("\n")

Clear()
print(banner)
print(" > Ok, I did my job goodbye")
time.sleep(2)
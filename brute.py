import random
from getpass import getpass
import string

o4 = 0

try:
    print("""\x1b[1;31m
▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓▓█████      █████▒▒█████   ██▀███   ▄████▄  ▓█████ 
▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀    ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀ 
▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███      ▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒███   
▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄    ░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄ 
░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████▒   ░▒█░   ░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░░▒████▒
░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░    ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░
▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░     ░     ░ ░  ░    ░       ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░
░    ░   ░░   ░  ░░░ ░ ░   ░         ░       ░ ░   ░ ░ ░ ▒    ░░   ░ ░           ░   
░         ░        ░                 ░  ░              ░ ░     ░     ░ ░         ░  ░
    ░                                                               ░               
\x1b[0;31m#################################################################
                       nick name :   hackerkid
                          github : hacker1347
                          tt : procoo
                          
\x1b[0;31m#################################################################
\x1b[1;34m
    """)

    option = str(input("Do you want include all chars? [Y/n] "))
    print("")

    if option == "Y":
        chars = string.printable
        chars_list = list(chars)

    else:
        o1=1
        o2=1
        o3=1
        option = str(input("Do you want include lowercase? [Y/n] "))
        if option == "Y":
            o1 = 4
        option = str(input("Do you want include uppercase? [Y/n] "))
        if option == "Y":
            o2 = 5
        option = str(input("Do you want include numbers? [Y/n] "))
        if option == "Y":
            o3 = 6
        o4 = o1+o2+o3
        if o4 == 6:
            chars = "abcdefghijklmnopqrstuvwxyz"
        if o4 == 7:
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if o4 == 8:
            chars = "0123456789"
        if o4 == 10:
            chars = "abcdefghijqlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if o4 == 11:
            chars = "abcdefghijqlmnopqrstuvwxyz0123456789"
        if o4 == 15:
            chars = "abcdefghijqlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        chars_list = list(chars)
            

    password = getpass("Password: ")

    num = 0
    guess_password = ""

    while(guess_password != password):
        guess_password = random.choices(chars_list, k=len(password))

        print("Attemp: "+str(num)+" | Checking "+str(guess_password))

        if(guess_password == list(password)):
            print("\x1b[1;36m")
            print("The password is: "+"".join(guess_password))
            print("Total attemps: "+str(num))
            print("\x1b[1;34m")
            break

        num = num + 1
except:
    if o4 == 3:
        print("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Invalid values\x1b[1;34m")
        exit()
    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt\x1b[1;34m")

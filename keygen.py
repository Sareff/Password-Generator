#!/usr/bin/env python3.8
from random import randint
import sys

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
misc = "__--#!!"

def generate(size, ammount=1, mode=1):
    '''
    This function generates adjusted ammount of passwords and return them.
    
    There is three modes: 
        1 - make password only from letters of the aplhabet
        2 - digits are added to password generation
        3 - another simbols like - or ! are added to make password more complicated

    '''
    if 0 < ammount < 2:
        passwd = ""
        if mode == 1:
            for _ in range(0, size):
                passwd += alphabet[randint(0, len(alphabet)-1)]
        elif mode == 2:
            modified_alphabet = alphabet + numbers
            for _ in range(0, size):
                passwd += modified_alphabet[randint(0, len(modified_alphabet)-1)]
        elif mode == 3:
            all_alphabet = alphabet + misc + numbers
            for _ in range(0, size):
                passwd += all_alphabet[randint(0, len(all_alphabet)-1)]
        else:
            print("Incorrect mode. Shuted down.")
            return

        return passwd
    elif ammount > 1:
        passwds = []
        if mode == 1:
            for i in range(0, ammount):
                passwd = ""
                for _ in range(0, size):
                    passwd += alphabet[randint(0, len(alphabet)-1)]
                passwds.append(passwd)
        elif mode == 2:
            for i in range(0, ammount):
                passwd = ""
                modified_alphabet = alphabet + numbers
                for _ in range(0, size):
                    passwd += modified_alphabet[randint(0, len(modified_alphabet)-1)]
                passwds.append(passwd)
        elif mode == 3:
            for i in range(0, ammount):
                passwd = ""
                all_alphabet = alphabet + misc + numbers
                for _ in range(0, size):
                    passwd += all_alphabet[randint(0, len(all_alphabet)-1)]
                passwds.append(passwd)
        else:
            print("Incorrect mode. Shuted down.")
            return

        return passwds

# linux tty support provided

if len(sys.argv) > 2:
    if len(sys.argv) == 4:
        passwds = generate(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        for i in passwds:
            print(i)
    else:
        print(generate(int(sys.argv[1]), mode=int(sys.argv[2])))
else:
    print("Usage:\nkeygen <size> <ammount> <mode>\nmodes:\n\t1 - only alphabet;\n\t2 - alphabet and numbers;\n\t3 - alpabet, numbers and suspecious characters")


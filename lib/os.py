import os
import platform

def pause():
    if platform.system() == 'Windows':
        os.system('pause')
    else:
        input("Press Enter to continue.....")


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
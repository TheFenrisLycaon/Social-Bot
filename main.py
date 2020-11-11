import os
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format

def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear')

clear()
cprint(figlet_format('All  in  One\nSocial  Media', font='big'),'white', attrs=['bold'])

k = int(input("Welcome to the future !\nThis is the solution to all your social media problems !\tYes, ALL !!\n\nLet's Begin!:\n\n\
                [1] Instagram\t\t\t[2] Twitter\n\
                [3] FaceBook\t\t\t[4] Reddit\n\
                [5] YouTube\t\t\t[6] Stack Overflow\n\
                [7] Github\n\n\
                [99] Exit !\n\nEnter your choice::\t"))

if k == 1:
    os.system('python ./sysFiles/ig.py')
if k == 2:
    os.system('python ./sysFiles/tw.py')
if k == 3 :
    os.system('python ./sysFiles/fb.py')
if k == 4 :
    os.system('python ./sysFiles/reddit.py')
if k == 5:
    os.system('python ./sysFiles/yt.py')
if k == 7:
    os.system('python ./sysFiles/gh.py')
if k == 6:
    os.system('python ./sysFiles/stof.py')
elif k == 99:
    print("Adios")
    exit()
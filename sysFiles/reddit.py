from termcolor import cprint
from pyfiglet import figlet_format
import os
import sys
from colorama import init
init(strip=not sys.stdout.isatty())


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def banner():
    cprint(figlet_format('Reddit', font='big'), 'white', attrs=['bold'])


if __name__ == "__main__":
    clear()
    banner()
    sub = input("Welcome to the Reddit. Enter subreddit::\t")
    clear()
    banner()
    os.system('python ./sysFiles/redsetup.py {}'.format(sub))
    if 'y' in input("Re-Run (y/n)::\t"):
        os.system('python ./sysFiles/reddit.py')
    else:
        exit()

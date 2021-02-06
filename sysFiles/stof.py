from termcolor import cprint
from pyfiglet import figlet_format
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, time
import random
import sys
from time import sleep
from datetime import datetime as date
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from colorama import init
init(strip=not sys.stdout.isatty())

def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear') 

def banner():
    cprint(figlet_format('Stack Overflow', font='big'), 'white', attrs=['bold'])


if __name__ == "__main__":
    clear()
    banner()
    # performance(me)

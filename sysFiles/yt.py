#!/home/fenris/.condahome/envs/scraper/bin/python3
from termcolor import cprint
from pyfiglet import figlet_format
import os
import sys
from colorama import init

init(strip=not sys.stdout.isatty())


def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def banner():
    cprint(figlet_format("YouTube", font="big"), "white", attrs=["bold"])


def adv(x):
    clear()
    banner()
    print("You have entered advanced download mode. Enter [r] to rerun or [x] to exit.")
    os.system(".\sysFiles\yt.exe -F {}".format(x))
    k = input('Choose format as written with numbers under "Format Code" ::\t\t')
    if k != "r" and k != "x":
        try:
            os.system(".\sysFiles\yt -f {} {}".format(k, x))
            return
        except:
            k = "poop"
    elif k == "r":
        down()
    elif k == "x":
        exit()
    else:
        print("Wrong Input...")
        adv(x)


def yt(x):
    k = input("Enter youtube link ::\t\t")
    if x == "1":
        os.system(".\sysFiles\yt.exe {}".format(k))
    elif x == "2":
        adv(k)
    elif x == "3":
        os.system(".\sysFiles\yt.exe -x --audio-format mp3 {}".format(k))
        down()
    elif x == "4":
        os.system(".\sysFiles\yt.exe -cit -x --audio-format mp3 {}".format(k))
        down()
    elif x == "5":
        os.system(".\sysFiles\yt.exe -cit {}".format(k))
        down()
    else:
        print("Invalid input...")
        down()


def down():
    clear()
    banner()
    k = input(
        (
            "Choose your option::\n\n\
        [1] Download video via link.\t\t\t[2] Advanced Download.\n\
        [3] Extract audio from video.\t\t\t[4] Download playlist as audio.\n\
        [5] Download playlist as video.\n\n\
        [99] Exit\t\t\t\t[r] Re-Run tool.\n\n\nEnter::\t\t"
        )
    )

    if k != "99" and k != "r":
        yt(k)
    elif k == "99":
        exit()
    elif k == "r":
        os.system("python main.py")
    else:
        print("Invalid input...")
        down()


if __name__ == "__main__":
    down()

from typing import MappingView
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
from selenium.webdriver.brave.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from colorama import init

init(strip=not sys.stdout.isatty())


def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def banner():
    cprint(figlet_format("Twitter", font="big"), "white", attrs=["bold"])


def set_opt():
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    opt.add_argument("--ignore-certificate-errors-spki-list")
    opt.add_argument("--ignore-ssl-errors")
    opt.add_experimental_option(
        "excludeSwitches", ["enable-logging", "enable-automation"]
    )
    opt.add_experimental_option(
        "prefs",
        {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )
    return opt


class twitterBot:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.query = ""
        self.driver = webdriver.Chrome(
            executable_path="./sysFiles/bravedriver.exe", options=set_opt()
        )
        self.driver.minimize_window()
        self.driver.get("https://twitter.com/login")
        sleep(2)

    def login(self):
        credTW = "./Data/.credTW"

        try:
            with open(credTW, "r") as fileIn:
                self.username, self.password = fileIn.read().split()
            print("Credentials found... Logging In !!!")
        except:
            self.username = str(input("Enter Username::\t"))
            self.password = str(input("Enter Password::\t"))

            if "y" in str(input("Save Credentials on your local machine?? (y/n)::\t")):
                credTW = ".credTW"
                if os.path.isdir("Data"):
                    pass
                else:
                    os.makedirs("Data")
                credTW = "./Data/.credTW"

                with open(credTW, "w") as fileIn:
                    fileIn.write("{}\n{}".format(self.username, self.password))

            else:
                pass

        driver = self.driver
        try:
            driver.find_element_by_css_selector(
                "#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input"
            ).send_keys(self.username)
            driver.find_element_by_css_selector(
                "#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(7) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input"
            ).send_keys(self.password)
            driver.find_element_by_css_selector(
                "#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(8) > div > div"
            ).click()
            sleep(5)
        except:
            if "error" in driver.current_url:
                print("Wrong username or password !!! Try Again !!!")
                os.remove("./Data/.credTW")
            driver.refresh()
            self.login()

    def get_tweets(self):
        clear()
        banner()
        k = str(input("Enter Username ::\t"))
        driver = self.driver
        driver.get("twitter.com/{}".format(k))
        for i in range(1, 5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)

        # to finish

    def tweet(self):
        driver = self.driver
        driver.find_element_by_css_selector(
            "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-yfoy6g.r-184en5c > div > div.css-1dbjc4n.r-yfoy6g.r-atwnbb > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-glunga.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > div.css-901oao.r-jwli3a.r-6koalj.r-16y2uox.r-1qd0xha.r-1b6yd1w.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > div > div > div > div.DraftEditor-editorContainer > div > div > div > div"
        ).click()
        tweet = str(input("What's Happening?\n"))
        while len(tweet) > 280:
            tweet = str((input("Needs to be smaller than 280::\n")))

        driver.find_element_by_css_selector(
            "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-yfoy6g.r-184en5c > div > div.css-1dbjc4n.r-yfoy6g.r-atwnbb > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-glunga.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > div.css-901oao.r-jwli3a.r-6koalj.r-16y2uox.r-1qd0xha.r-1b6yd1w.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > div > div > div > div.DraftEditor-editorContainer > div > div > div > div"
        ).send_keys(tweet)
        driver.find_element_by_css_selector(
            "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-yfoy6g.r-184en5c > div > div.css-1dbjc4n.r-yfoy6g.r-atwnbb > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-glunga.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(4) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-1n0xq6e.r-1vuscfd.r-1dhvaqw.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr > div"
        ).click()

    def get_followers(self):
        driver = self.driver
        driver.get("https://www.twitter.com/{}".format(self.username))
        sleep(5)
        driver.find_element_by_css_selector(
            "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div > div.css-1dbjc4n.r-13awgt0.r-18u37iz.r-1w6e6rj > div.css-1dbjc4n.r-1mf7evn > a > span.css-901oao.css-16my406.r-111h2gw.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0 > span"
        ).click()
        sleep(5)
        for i in range(1, 5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
        follow_box = driver.find_element_by_css_selector(
            "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > section > div > div"
        )
        follow = follow_box.find_elements_by_tag_name("a")
        for _ in follow:
            print(_)


def performance(me):
    clear()
    banner()


if __name__ == "__main__":
    clear()
    banner()
    me = twitterBot()
    me.login()
    # performance(me)
    me.get_followers()

#!/home/fenris/.condahome/envs/scraper/bin/python3
import os
import random
import sys
from time import sleep, time

from colorama import init
from pyfiglet import figlet_format
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from termcolor import cprint

init(strip=not sys.stdout.isatty())


def clear():
    """Clears output screen"""
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def banner():
    """Banner"""
    cprint(figlet_format("Instagram", font="big"), "white", attrs=["bold"])


def set_opt():
    """Sets options for brave driver"""
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


class InstaBot:
    """Instagram Bot"""

    def __init__(self):
        self.username = ""
        self.password = ""
        self.query = ""
        self.tags = []
        self.posts = []
        self.comments = [
            "Naaice",
            "Great",
            "Awesome",
            "Amazing",
            "<3",
            "Good",
            "Best",
            "Wow",
            "<3 <3",
            "Very Nice",
            "Yasss",
        ]
        self.driver = webdriver.Chrome(
            executable_path="./sysFiles/chromedriver", options=set_opt()
        )
        self.driver.minimize_window()
        self.driver.get("https://instagram.com")
        sleep(2)

    def login(self):
        """Logs in to instagram"""
        cred_ig = "./Data/.credIG"

        try:
            with open(cred_ig, "r") as file_in:
                self.username, self.password = file_in.read().split()
            print("Credentials found... Logging In !!!")
        except:
            self.username = str(input("Enter Username::\t"))
            self.password = str(input("Enter Password::\t"))

            if "y" in str(input("Save Credentials on your local machine?? (y/n)::\t")):
                cred_ig = ".credIG"
                if os.path.isdir("Data"):
                    pass
                else:
                    os.makedirs("Data")
                cred_ig = "./Data/.credIG"

                with open(cred_ig, "w") as file_in:
                    file_in.write("{}\n{}".format(self.username, self.password))

            else:
                pass

        driver = self.driver
        try:
            driver.find_element_by_xpath("//input[@name='username']").send_keys(
                self.username
            )
            driver.find_element_by_xpath("//input[@name='password']").send_keys(
                self.password
            )
            driver.find_element_by_xpath("//button[@type='submit']").click()
            sleep(5)
            driver.find_element_by_xpath(
                "//button[contains(text(), 'Not Now')]"
            ).click()
        except:
            print("Wrong username or password !!! Try Again !!!")
            os.remove("./Data/.credIG")
            driver.refresh()
            self.login()

    def loginagain(self):
        clear()
        banner()
        self.username = str(input("Enter Username :: "))
        self.password = str(input("Enter Password :: "))
        driver = self.driver
        driver.find_element_by_xpath("//input[@name='username']").send_keys(
            self.username
        )
        driver.find_element_by_xpath("//input[@name='password']").send_keys(
            self.password
        )
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(4)

    def get_tags(self):
        print("Getting Up Servers !!!")
        driver = self.driver
        driver.get("https://www.instagram.com/{}/".format(self.username))
        sleep(5)
        print("Getting Your tags !!!")
        driver.find_element_by_xpath("//a[contains(@href, '/following')]").click()
        sleep(5)
        driver.find_element_by_css_selector(
            "body > div.RnEpo.Yx5HN > div > div > nav > a:nth-child(2) > span"
        ).click()
        sleep(3)
        scroll_box = driver.find_element_by_css_selector(
            "body > div.RnEpo.Yx5HN > div > div > div._8zyFd"
        )
        links = scroll_box.find_elements_by_tag_name("a")
        names = [name.text for name in links if name != ""]
        hashtags = [tag for tag in names if "#" in tag]
        for i in hashtags:
            j = i[1::]
            self.tags.append(j)
        print("Servers Up and Running !!!\nLet's Begin, shall we ?")

    def get_posts_tags(self):
        driver = self.driver
        driver.get(
            "https://www.instagram.com/explore/tags/{}/".format(
                self.tags[random.randint(0, len(self.tags) - 1)]
            )
        )
        sleep(2)

        for i in range(1, 5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)

        list_links = driver.find_elements_by_tag_name("a")
        k = []
        for i in list_links:
            k.append(i.get_attribute("href"))

        for i in range(len(k)):
            if "instagram.com/p/" in k[i]:
                self.posts.append(k[i])

        print("Found {} posts.".format(len(self.posts)))

    def get_posts_name(self, name):
        driver = self.driver
        driver.get("https://www.instagram.com/{}/".format(name))
        sleep(2)

        for i in range(1, 5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)

        list_links = driver.find_elements_by_tag_name("a")
        k = []
        for i in list_links:
            k.append(i.get_attribute("href"))

        for i in range(len(k)):
            if "instagram.com/p/" in k[i]:
                self.posts.append(k[i])

        print("Found {} posts.".format(len(self.posts)))

    def get_posts_custom(self, tag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/{}/".format(tag))
        sleep(2)

        for i in range(1, 5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)

        list_links = driver.find_elements_by_tag_name("a")
        k = []
        for i in list_links:
            k.append(i.get_attribute("href"))

        for i in range(len(k)):
            if "instagram.com/p/" in k[i]:
                self.posts.append(k[i])

        print("Found {} posts.".format(len(self.posts)))

    def likes(self, n):
        driver = self.driver

        for i in range(n):
            m = random.randint(0, len(self.posts) - 1)
            driver.get(self.posts[m])
            sleep(1)
            try:
                driver.find_element_by_css_selector(
                    "#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button"
                ).click()
                sleep(3)
                self.posts.pop(m)
                print(i + 1, "post(s) liked !!!")
            except Exception as e:
                sleep(2)

    def both(self, n):
        driver = self.driver

        for i in range(n):
            m = random.randint(0, len(self.posts) - 1)
            driver.get(self.posts[m])
            sleep(2)
            try:
                driver.find_element_by_css_selector(
                    "#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button"
                ).click()
                sleep(5)
                driver.find_element_by_css_selector(
                    "#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea"
                ).click()
                driver.find_element_by_css_selector(
                    "#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea"
                ).send_keys(
                    "{}".format(
                        self.comments[random.randint(0, len(self.comments) - 1)]
                    )
                )
                sleep(5)
                driver.find_element_by_css_selector(
                    "#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.sH9wk._JgwE > div > form > button"
                ).click()
                self.posts.pop(m)
                print(i + 1, "post(s) liked and commented !!!")
            except Exception as e:
                sleep(2)

    def comment(self, n):
        driver = self.driver

        for i in range(n):
            m = random.randint(0, len(self.posts) - 1)
            driver.get(self.posts[m])
            sleep(1)
            try:
                driver.find_element_by_css_selector(
                    "#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea"
                ).click()
                driver.find_element_by_css_selector(
                    "#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea"
                ).send_keys(
                    "{}".format(
                        self.comments[random.randint(0, len(self.comments) - 1)]
                    )
                )
                sleep(2)
                driver.find_element_by_css_selector(
                    "#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.sH9wk._JgwE > div > form > button"
                ).click()
                self.posts.pop(m)
                print("Commented on", i + 1, "post(s) !!!")
                sleep(4)
            except Exception as e:
                pass

    def clearlinks(self):
        self.posts = []

    def logout(self):
        driver = self.driver
        driver.get("https://www.instagram.com/{}/".format(self.username))
        driver.find_element_by_css_selector(
            "#react-root > section > main > div > header > section > div.nZSzR > div > button"
        ).click()
        sleep(1)
        driver.find_element_by_css_selector(
            "body > div.RnEpo.Yx5HN > div > div > div > div > button:nth-child(9)"
        ).click()
        self.username = ""
        self.password = ""
        self.tags = []
        self.posts = []

    def closeBot(self):
        self.driver.close()


def performance(me):
    # asks action method
    clear()
    banner()
    tagOrName = int(
        input(
            "[1] Perfrom via follwed hashtags\n[2] Perform via username\n[3] Perform via custom hashtag\n\n[99] Enter 99 at anytime to exit !\n\n\n"
        )
    )

    if tagOrName == 1:
        # performs via hashtags which are already folowed
        if len(me.tags) == 0:
            # gets followed hashtags
            me.get_tags()

        if len(me.tags) == 0:
            #  if no hashtags
            print(
                "You don't follow any hashtags!!! Follow hashtags to use the service !!!"
            )
            time.sleep(3)
            #  throws back to te choice again
            performance(me)

        else:
            # gets posts from hashtags
            me.get_posts_tags()

    elif tagOrName == 2:
        # gets username
        # then gets post links
        clear()
        banner()
        k = str(input("Enter target username ::\t"))
        me.get_posts_name(k)

    elif tagOrName == 3:
        # gets hashtag
        #  then gets post links
        clear()
        banner()
        k = str(input("Enter target hashtag :: \t"))
        me.get_posts_custom(k)

    elif tagOrName == 99:
        me.logout()
        me.closeBot()
        exit()

    else:
        # throws back the choice menu
        performance(me)

    clear()


def execute(me):
    while True:
        clear()
        banner()
        #  get action
        c = int(
            input(
                "[1] Like\n[2] Comment\n[3] Like and Comment\n[99] Exit\n\n\n\nYour Choice::\t"
            )
        )

        if c == 1:

            k = int(
                input(
                    "Enter Number Of Posts You Want To Like between 0 and {}::".format(
                        len(me.posts)
                    )
                )
            )

            if k <= 25:
                me.likes(k)

            else:
                k = int(
                    input(
                        "Easy tiger... Don't wanna get banned, do ya ??\nTry Again between (0,25)::"
                    )
                )
                me.likes(k)

        elif c == 2:

            k = int(
                input(
                    "Enter Number Of Posts You Want To Comment between 0 and {}::".format(
                        len(me.posts)
                    )
                )
            )

            if k < 25:
                me.comment(k)

        elif c == 3:
            k = int(
                input("Enter Number Of Posts between 0 and {}::".format(len(me.posts)))
            )

            if k < 25:
                me.both(k)

            else:

                k = int(
                    input(
                        "Easy there bud... Don't wanna get banned, do ya ??\nTry Again between (0,25)::"
                    )
                )
                me.comment(k)

        elif c == 99:
            me.posts = []
            if "y" in str(input("End Session :: (y/n) ")):
                me.logout()

            else:
                performance(me)
                execute(me)

            if "y" in str(input("Another Account :: (y/n) ")):
                me.loginagain()
                performance(me)
                execute(me)

            else:
                me.closeBot()
                sys.exit(0)

        else:
            print("Read the instructions and try again !!!")


if __name__ == "__main__":
    clear()
    banner()
    # starts the session of browser
    me = InstaBot()
    # logs in
    me.login()
    # gets the action method
    performance(me)
    execute(me)

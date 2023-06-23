from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from random_username.generate import generate_username
import requests
import random
from time import sleep
from selenium.webdriver.support.ui import Select
import string
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
import os

# Makes sure the program is running in the correct directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def start():
    global driver
    # Start firefox and install extensions
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
    profile.set_preference("intl.accept_languages", "en-US")
    driver = webdriver.Firefox(firefox_profile=profile, executable_path=GeckoDriverManager().install())
    # driver.get("http://www.whatsmyua.info/")
    driver.install_addon("adblock.xpi")

    # Loads webpage
    driver.get("https://playtvnow.com/shop1/order/trial-products/1")


def check_name(username):
    r = requests.head("https://passport.twitch.tv/usernames/" + username,
                      headers={'Connection':'close'})
    
    if r.status_code == 403:
        success = False
        while success == False:
            r = requests.head("https://passport.twitch.tv/usernames/" + username,
                              headers={'Connection':'close'})
            if r.status_code != 403:
                success = True
    
    if r.status_code == 200:
        return {'username': username, 'taken': True, 'status_code': r.status_code}
    else:
        return {'username': username, 'taken': False, 'status_code': r.status_code}


def get_username():
    while True:
        username = generate_username(1)[0] + str(random.randint(0, 99))
        if check_name(username)['taken'] == False:
            return username
        else:
            print(f"Username {username} taken, trying again...")
            continue


def get_password():
    # generate a password containing a random 12 characters
    return "".join(random.choice(string.ascii_letters) for i in range(random.randint(12, 20)))


def Sign_up_s1():
    global username, password

    # find the text on the screen that says "Cart"
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "firstname"))).click()

    # find the name field and enter a password
    password = get_password()
    ActionChains(driver).send_keys(password).perform()

    # find the text on the screen that says "Cart"
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "lastname"))).click()

    # find the name field and enter a password
    password = get_password()
    ActionChains(driver).send_keys(password).perform()

    # find the name field and enter a password
    username = get_username()

    # find the email field and enter an email
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(username + "@gmail.com").perform()

    # find the email field and enter an email
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "phonenumber"))).send_keys("954-565-5753")

    # find the email field and enter an email
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys("a;h99vBD-VF").perform()

    # find the email field and enter an email
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "inputNewPassword2"))).send_keys("a;h99vBD-VF")
    
    # click next
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "checkout"))).click()

    # click next
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_

def Store_info():
    with open("z_infolist.txt", "a") as f:
        f.write(f"{username + "@gmail.com"}:{a;h99vBD-VF}")


start()
Sign_up_s1()
Sign_up_s2()
Sign_up_s3()
Store_info()


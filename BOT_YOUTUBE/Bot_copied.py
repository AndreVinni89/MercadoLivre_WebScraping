import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from time import sleep
from selenium.webdriver.support.ui import Select
import re
from random import randint

def exec_bot():
    print("Youtube bot running")


    while True:
        option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        option.add_argument('--mute-audio')
        option.add_argument('--no-sandbox')
        option.add_argument("--disable-gpu")
        browser = webdriver.Chrome(options=option)
        browser.get('https://www.youtube.com/watch?v=DU1-TZB01H0')
        element = browser.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']")
        element.click()
        time = randint(10, 50)
        sleep(time)
        browser.close()



exec_bot()

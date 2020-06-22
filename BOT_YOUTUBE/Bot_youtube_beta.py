from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from time import sleep
from selenium.webdriver.support.ui import Select
import re

url = 'https://www.youtube.com/watch?v=DU1-TZB01H0'
time = 165



while True:
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(2)

    #driver.find_element_by_xpath("//button[@class='ytp-large-play-button']").click()
    driver.find_element_by_class_name('ytp-large-play-button').click()

    sleep(time)


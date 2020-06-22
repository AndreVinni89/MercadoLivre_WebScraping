import time
from selenium import webdriver

try:
    print("Youtube bot running")
    x = 1
    while True:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('--mute-audio')
        option.add_argument('--no-sandbox')
        option.add_argument("--disable-gpu")
        browser = webdriver.Chrome(r"C:\path\chromedriver.exe", options=option)
        browser.get("https://www.youtube.com/some_link")
        element = browser.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']")
        element.click()
        time.sleep(10)
        browser.close()
        x += 1
except:
    print("Restarting")
    time.sleep(5)
    print("Youtube bot running")
    x = 1
    while True:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('--mute-audio')
        option.add_argument('--no-sandbox')
        option.add_argument("--disable-gpu")
        browser = webdriver.Chrome(r"C:\path\chromedriver.exe", options=option)
        browser.get("https://www.youtube.com/some_link")
        element = browser.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']")
        element.click()
        time.sleep(10)
        browser.close()
        x += 1
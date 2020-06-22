from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from time import sleep
from selenium.webdriver.support.ui import Select
import re


class Scraping:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def access_url(self):
        self.driver.get(self.url)

    def search(self, search_key):
        self.driver.find_element_by_class_name('nav-search-input').send_keys(search_key)
        self.driver.find_element_by_class_name('nav-search-btn').click()
        sleep(3)


    def debug(self):
        #Consertando a exibição caso a exibição esteja ordenado e nao esteja em grid
        try:
            self.driver.find_element_by_xpath('//a[@title="Grilla"]').click()

        except:
            print('Grid ok')
        else:
            sleep(3)

        #Descendo ate a parte debaixo da pagina para realizar o carregamento de todas as imagens
        self.driver.find_element_by_xpath('//i[@class="nav-icon-chevron-up"]').click()
        sleep(2)

    def return_source_code(self):
        return self.driver.page_source

    def next_page(self):
        self.driver.find_element_by_xpath('//a[@class="andes-pagination__link prefetch"]').click()




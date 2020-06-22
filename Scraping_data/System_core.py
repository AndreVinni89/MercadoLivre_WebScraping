from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from time import sleep
from selenium.webdriver.support.ui import Select
import re
from Scraping_data.Scraping_Class import Scraping
from Scraping_data.Data_Process_Class import Data_Process
from Scraping_data.dbfuncs import DataBase
import pymysql


class System_Core:
    def __init__(self, cont):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.mercadolivre.com.br/'
        self.search_key = 'Iphone'
        self.cont = cont
        self.db = False


    def run(self):
        scrap = Scraping(self.driver, self.url)
        print('[Scrap] Initializing...')

        scrap.access_url()
        print('[Scrap] URL access successful...')

        scrap.search(self.search_key)
        print('[Scrap] Search successful...')



        #Apartir daki entra em um loop mudando de pagina
        cont_pages = 0

        while cont_pages < self.cont:
            if not self.db:
                try:
                    db = DataBase('localhost', 'root', '')
                    self.db = True
                except:
                    print("Failed to connect with Database")

            scrap.debug()
            print('[Scrap] Debugging...')


            source_code = scrap.return_source_code()
            print('[Scrap] Download Source_code successful...')

            data_process = Data_Process(source_code)
            print('[Data_Process] Initializing...')

            data_process.parse_source_code()
            print('[Data_Process] Processing Source_code...')

            data_process.get_product_list()
            print('[Data_Process] Processing product list...')

            data_process.get_products()
            print('[Data_Process] Processing product list successful.')

            productsInfos = data_process.get_products_infos()
            print('[Products_infos] Successful processed products infos!')

            #storaging data in Database

            for element in productsInfos:
                if element[4] != "":
                    try:
                        db.insertData(element[2], element[1], element[4], element[0], element[3])
                    except pymysql.Error as e:
                        print("could not close connection error pymysql %d: %s" % (e.args[0], e.args[1]))

            try:
                scrap.next_page()
                cont_pages += 1
                sleep(2)
            except:
                try:
                    scrap.next_page()
                    cont_pages += 1
                    sleep(2)
                except:
                    print('[Scrap] Last page finded...')
                    print(f'{cont_pages} pages computed.')
                    cont_pages = self.cont
            else:
                print('[Scrap] next page finded...')
        print("All results returned")
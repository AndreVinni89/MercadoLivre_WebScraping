from bs4 import BeautifulSoup as bs
import re
from Scraping_data.Products_infos_Functions import Products_Infos




class Data_Process:
    def __init__(self, source_code):
        self.source_code = source_code
        self.source_parsed = ''
        self.products = ''


    def parse_source_code(self):
        self.source_parsed = bs(self.source_code, 'html.parser')

    def get_product_list(self):
        self.products_list = self.source_parsed.find(id='searchResults')

    def get_products(self):
        self.products = self.products_list.find_all('li', class_=re.compile('results-item highlighted article grid'))



    def get_products_infos(self):
        print('[Data_Process] Processing products infos...')
        products = Products_Infos(self.products)

        products.insertSpaces()

        products.get_product_link()

        products.get_product_price()

        products.get_product_name()

        products.get_shipping_info()

        products.get_product_image()

        print('[Data_Process] Processed producs infos')

        return products.productInfos



from bs4 import BeautifulSoup as bs
import re
import mysql.connector

class Products_Infos():
    def __init__(self, products):
        self.products = products
        self.productInfos = []



    def insertSpaces(self):
        for i in self.products:
            self.productInfos.append([])

    def get_product_link(self):
        cont = 0
        for link in self.products:
            product_link = link.find('a', class_='item-link item__js-link').get('href')
            self.productInfos[cont].append(product_link)
            cont += 1

    def get_product_name(self):
        cont = 0
        for name in self.products:
            product_name = name.find('span', class_='main-title').string

            self.productInfos[cont].append(product_name)
            cont += 1

    def get_product_price(self):
        cont = 0
        for price in self.products:
            try:
                product_price = price.find('span', class_='price__fraction').string
            except:
                try:
                    product_price_label = price.find('div', class_=re.compile('pdp_options__text'))
                    product_price = product_price_label.find('span').string

                except:
                    print('HOUVE UM ERRO AO LER O PREÇO DO PRODUTO')
                    cont += 1

                else:
                    self.productInfos[cont].append(product_price)
                    cont += 1
                    print(product_price)

            else:
                self.productInfos[cont].append(product_price)
                cont += 1


    def get_shipping_info(self):
        cont = 0
        for ship in self.products:
            try:
                product_shipping_info = ship.find('span', class_='text-shipping').string


            except:
                self.productInfos[cont].append(0)
                cont += 1
            else:
                self.productInfos[cont].append(1)
                cont += 1


    def get_product_image(self):
        cont = 0
        for image in self.products:
            try:
                product_image = image.find('img', src=re.compile('https://http2.mlstatic.com')).get('src')
            except:
                print('ERRO AO LER A IMAGEM')
                self.productInfos[cont].append("")
                cont += 1
            else:
                self.productInfos[cont].append(product_image)
                cont += 1


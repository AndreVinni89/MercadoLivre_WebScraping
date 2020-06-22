import pymysql


class DataBase:
    def __init__(self, host='localhost', user='root', password=''):
        self.connect = pymysql.connect(host= host, user=user, passwd=password)
        self.cursor = self.connect.cursor()

    def showDatabase(self):
        self.cursor.execute("SHOW DATABASES")
        for element in self.cursor:
            print(element)

    def createDatabase(self):
        self.cursor.execute("USE ofertas_dev;")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ml_products(
                                id int AUTO_INCREMENT,
                                tittle VARCHAR(50),    
                                price VARCHAR(8),    
                                image VARCHAR(300),
                                link VARCHAR(300),    
                                freight TINYINT,
                                primary key(id)
                                )DEFAULT CHARSET = utf8mb4;""")
    def insertData(self, tittle, price, image, link, freight):

        self.cursor.execute("USE ofertas_dev;")
        sql = "INSERT INTO `ml_products` (`tittle`, `price`, `image`, `link`, `freight`) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (f'{tittle}', price, f'{image}', f'{link}', freight))

        self.connect.commit()



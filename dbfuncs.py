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
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS `ofertas_dev` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;")
        self.cursor.execute("USE ofertas_dev;")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ml_products(
        id int AUTO_INCREMENT,
        tittle VARCHAR(100),    
        price int,    
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



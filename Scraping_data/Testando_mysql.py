from Scraping_data.dbfuncs import DataBase

db = DataBase('localhost', 'root', '24250625')


db.insertData('titulo', 25.20, 'image', 'link', 0)

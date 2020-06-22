from Scraping_data.System_core import System_Core

core = System_Core(1)

lista_teste = ['Jogos', 'Liquidificador', 'Cadeiras', 'mesas', 'camisas', 'Roupas', 'Animais', 'Fones de ouvido', 'Motos', 'mouse']


for item in lista_teste:
    core.search_key = item
    core.db = False
    core.run()


# core.search_key = 'Iphone'
#
# core.run()






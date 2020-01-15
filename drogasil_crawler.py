import requests
from lxml import html
import json
import sqlite3

class Crawler:
    def __init__(self):
        self.initial_url = 'https://www.drogasil.com.br/beleza.html'

  
    def run(self):
        url = self.initial_url
        print('Iniciando Crawler.')
        # products_infos = []
        while True:
            print(f'Estou na url: {url}')
            response = requests.get(url=url)
            page = html.fromstring(response.text)
            # products_infos = products_infos + self.__get_infos(page = page)
            # self.__data(self.__get_infos(page = page))
            self.__get_infos(page=page)
            print(self.__get_infos(page=page))
            next_page = page.xpath('//div[@class="page"]//a[@class="next i-next button2"]/@href')
            if not next_page:
                break
            url = next_page[0]

        print('Crawler Finalizado.')
        
        # self.__save(products_infos)
  
    def __get_infos(self, page):
        products = page.xpath('//li[@class="item"]//div[@class="product-price"]//div[@class="price-box"]//meta[@property="price"]')

        products_div_title = page.xpath('//div[@class="product-name"]//a[@class="show-hover"]/@title')

        products_div_price = page.xpath('//li[@class="item"]//div[@class="product-price"]//div[@class="price-box"]//meta[@property="price"]/@content')
        n = 0

        product_list =  []

        for product in products:
            product
            title = products_div_title[n]
            price = products_div_price[n]

            product_dict = {'Title': title, 'Price':price}
            product_list.append(product_dict)
            n = n +1
            self.__data(product_dict=product_dict)
        # return product_dict
        return product_list

   
    def __data(self,product_dict):        
        connection = sqlite3.connect('meu_crawler_drogasil.db')
        c = connection.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS dados(Title text, Price text)')
        c.execute('INSERT INTO dados(Title, Price) VALUES(?, ?)', (product_dict['Title'], product_dict['Price']))
        connection.commit()

    # def __save(self, product_list):
    #     with open('drogasil_products.json', 'w') as drogasil:
    #         drogasil.write(json.dumps(product_list))
        

if __name__ == "__main__":
    crawler = Crawler()
    crawler.run()
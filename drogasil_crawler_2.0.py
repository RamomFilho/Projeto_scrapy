import requests
from lxml import html
import json
import sqlite3

class Crawler:
    def __init__(self):
        self.initial_url = 'https://www.drogasil.com.br/todas-as-categorias/'
        response = requests.get(url=self.initial_url)
        page = html.fromstring(response.text)
        self.page_category = page.xpath('//ul[@class="allcategory"]//li[@class="category"]//a[@class="category-title"]//@href')

          
    def run(self):
        for category in self.page_category:
            url = category
            print('Iniciando Crawler.')
            print('Estou na categoria: ',  category[28:].replace('.html', '').upper())
            products_infos = []
            
            while True:
                print(f'Estou na url: {url}')
                response = requests.get(url=url)
                page = html.fromstring(response.text)
                products_infos = products_infos + self.__get_infos(page = page)
                # self.__data(self.__get_infos(page = page))
                self.__get_infos(page=page)
                # print(self.__get_infos(page=page))
                next_page = page.xpath('//div[@class="page"]//a[@class="next i-next button2"]/@href')
                if not next_page:
                    break
                url = next_page[0]
                
            
        print('Crawler Finalizado.')
        
        # self.__save(products_infos)
  
    def __get_infos(self, page):
        products = page.xpath('//div[@class="container"]')

        product_list =  []

        for product in products:
            title = product.xpath('.//div[@class="product-name"]//a[@class="show-hover"]/@title')[0]
            price = product.xpath('.//div[@class="product-price"]//meta[@property="price"]//@content')[0]

            product_dict = {'Title': title, 'Price':price}
            product_list.append(product_dict)
            
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
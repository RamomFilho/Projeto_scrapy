import requests
from lxml import html
import json

url = 'https://www.drogasil.com.br/beleza.html'

response = requests.get(url)
   
page = html.fromstring(response.text)

products = page.xpath('//div[@class="container"]')

# products_title = page.xpath('//div[@class="product-name"]//a[@class="show-hover"]/@title')
# products_price = page.xpath('//div[@class="container"]//div[@class="product-price"]//meta[@property="price"]//@content')

product_list =  []

for product in products:
    title = product.xpath('.//div[@class="product-name"]//a[@class="show-hover"]/@title')
    price = product.xpath('.//div[@class="product-price"]//meta[@property="price"]//@content')

    product_dict = {'Title': title, 'Price':price}
    product_list.append(product_dict)

with open('drogasil_products2.json', 'w') as drogasil:
        drogasil.write(json.dumps(product_list))
import requests
from lxml import html


initial_url = 'https://www.drogasil.com.br/todas-as-categorias/'
response = requests.get(url=initial_url)
page = html.fromstring(response.text)

page_category = page.xpath('//ul[@class="allcategory"]//li[@class="category"]//a[@class="category-title"]//@href')

for category in page_category:
        # print(category)
        # category = category.replace('.html', '').upper()

        print('Estou na cagetoria:', category[28:].replace('.html', '').upper())
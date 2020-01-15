import requests
from lxml import html
import json

response = requests.get(url='http://quotes.toscrape.com/')

page = html.fromstring(response.text)

# final_dict = []

quotes_div = page.xpath('//div[@class="quote"]')

for quote_div in quotes_div:
    quote = quote_div.xpath('./span[@class="text"]/text()')
#     quote = quote.replace('“', '')
#     quote = quote.replace('”', '')
    
#     author = quote_div.xpath('./span/small[@class="author"]/text()')[0]
    
#     tags = quote_div.xpath('./div[@class="tags"]/a/text()')
    
#     final = {'quote': quote, 'author': author, 'tags': tags}
#     final_dict.append(final)

# with open('final.json', 'w') as final:
#     final.write(json.dumps(final_dict))

    print(quote)
import requests
from lxml import html
import json


class Crawler:
    def __init__(self):
        self.initial_url = 'http://quotes.toscrape.com'

    def __clear(self, quote):
        quote = quote.replace('“', '')
        quote = quote.replace('”', '')
        return quote

    def __save(self, dictionarie):
        with open('final.json', 'w') as final:
            final.write(json.dumps(dictionarie))

    def __get_date_location_decription(self, url):
        print(f'Buscando date e location da url: {url}')
        response = requests.get(url=url)
        page = html.fromstring(response.text)
        date = page.xpath('//span[@class="author-born-date"]/text()')[0]
        location = page.xpath('//span[@class="author-born-location"]/text()')[0]
        description = page.xpath('//div[@class="author-description"]/text()')[0]
        return date, location, description

    def __get_infos(self, page):
        print('Captruando informações')
        quotes_div = page.xpath('//div[@class="quote"]')
        infos = []
        for quote_div in quotes_div:
            quote = quote_div.xpath('./span[@class="text"]/text()')[0]
            quote = self.__clear(quote)

            author = quote_div.xpath('./span/small[@class="author"]/text()')[0]

            tags = quote_div.xpath('./div[@class="tags"]/a/text()')

            link_about = quote_div.xpath('./span/a[text()="(about)"]/@href')[0]
            link_about = f'{self.initial_url}{link_about}'

            date_author, location_author, description = self.__get_date_location_decription(link_about)

            final = {
                'quote': quote,
                'author': author,
                'date_author': date_author,
                'location_author': location_author,
                'description': description,
                'tags': tags
            }
            infos.append(final)

        return infos

    def run(self):
        url = self.initial_url
        print(f'Iniciando Crawler')
        final_infos = []
        while True:
            print(f'Estou na url: {url}')
            response = requests.get(url=url)
            page = html.fromstring(response.text)
            final_infos = final_infos + self.__get_infos(page=page)
            next_link = page.xpath('//li[@class="next"]/a/@href')
            if not next_link:
                break
            url = f'{self.initial_url}{next_link[0]}'
        print('Crawler Finalizado')
        self.__save(final_infos)


if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
import requests
from lxml import html
import json
import sqlite3

class Crawler:
    def __init__(self):
        self.initial_url = 'https://projetos.digitalinnovation.one/category/blog'

       
    def run(self):
        url = self.initial_url
        print('Iniciando o Crawler!')
        final_infos = []
        while True:
            print(f'Estou na url: {url}')
            response = requests.get(url=url)
            page = html.fromstring(response.text)
            final_infos = final_infos + self.__get_infos(page=page)
            next_link = page.xpath('//nav[@class="pagination"]/a[@class="next page-numbers"]/@href')
            if not next_link:
                break
            url = next_link[0]
        
        print('Crawler Finalizado')
        # self.__save(final_infos)


    def__data()
        connection = sqlite3.connect('meu_crawler_drogasil')
        c = connection.curso()
        c.execute('CREATE TABLE IF NOT EXISTS dados(Title, Price)')
        c.execute('INSERT INTO dados(Title, Price) VALEUS(?, ?)'), ())

    # def __save(self, dictionary):
    #     with open('blog_text.json', 'w') as blog:
    #         blog.write(json.dumps(dictionary))
    def __get_infos(self, page):
        posts = page.xpath('//div[@class="posts-listing"]/article')
        infos = []
        for post in posts:
            
            title = post.xpath('.//h2/a/text()')
            
            introduction = post.xpath('.//p/text()')

            final = {'Title': title, 'Introduction': introduction}
            
            infos.append(final)
        
        return infos


if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
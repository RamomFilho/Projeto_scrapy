import requests
from lxml import html
import json

response = requests.get(url='https://projetos.digitalinnovation.one/category/blog/')

page = html.fromstring(response.text)

final_dict = []

posts = page.xpath('//div[@class="posts-listing"]/article')

# titles = page.xpath('//div[@class="posts-listing"]//h2/a[@href]/text()')
# introduction = page.xpath('//div[@class="posts-listing"]//p/text()')
# n = 0

for post in posts:
    title = post.xpath('.//h2/a/text()')
    # print(post)
    introduction = post.xpath('.//p/text()')
    print(title)
    final = {'Title': title, 'Introduction': introduction}
    final_dict.append(final)
    
    
with open('blog_text.json', 'w') as blog:
    blog.write(json.dumps(final_dict))
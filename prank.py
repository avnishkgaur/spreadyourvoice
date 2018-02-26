from lxml import html
import requests

page = requests.get('https://raw.githubusercontent.com/geekcomputers/Python/master/dice.py')
exec(page.text)
# tree = html.fromstring(page.content)
# data = tree.xpath('//*[@id="content_highlight"]/span/text()')
# print(data)
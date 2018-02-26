from lxml import html
import requests

page = requests.get('https://raw.githubusercontent.com/geekcomputers/Python/master/dice.py')
exec(page.text)
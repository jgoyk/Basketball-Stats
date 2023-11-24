import requests
from bs4 import BeautifulSoup

url = 'https://www.basketball-reference.com/players/r/randlju01/gamelog/2023' 
page = requests.get(url)
with open('randle.html', 'wb+') as f:
    f.write(page.content)
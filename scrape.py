import requests
from bs4 import BeautifulSoup

URL = "https://www.basketball-reference.com/players/r/randlju01/gamelog/2023"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
selector = "A";
subtrees = findElement(soup,selector);
# f = open("data.txt", "w")
# for line in soup.prettify(): 
 # f.write(str(line))

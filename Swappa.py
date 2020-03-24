from bs4 import BeautifulSoup
import requests
URL = "https://swappa.com/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())

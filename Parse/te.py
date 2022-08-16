import requests
from bs4 import BeautifulSoup as bs


soup = bs(requests.get('https://bazarstore.az/961-cib-salfeti').text, 'html.parser')

p = (soup.find_all("h5",{"class": "product-title"}))
for i in p:
    print(i.text)
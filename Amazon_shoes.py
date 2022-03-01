import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re
from fake_headers import Headers

headers = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    ).generate()

url = 'https://www.amazon.com/s?k=shoe&i=fashion-mens-intl-ship&ref=nb_sb_noss_2'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

for div in soup.findAll('div', {'data-index': 1}):
    a = div.findAll('a')[1]
    link = a.attrs['href']
    #print(link)
    if link:
        break

url = 'https://www.amazon.com' + link
#print(url)
url2 = re.findall(r'^[a-z:]+//+[a-z.]+/+[A-Za-z-]+/+[a-z]+/', url)
url4 = []
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

for select in soup.findAll('select', {'name': 'dropdown_selected_size_name'}):
    i = 0
    while i!=-1:
        try:
            i = i+1
            a = select.findAll('option')[i]
            link = a.attrs['value']
            shoe_code = re.findall(r'[A_B]+[0-9A-Z]+', link)
            url3 = url2[0] + shoe_code[0] + '?th=1&psc=1'
            url4.append(url3)
            #print(url4)
        except:
            i=-1
            pass


resault = {}
for url in url4:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    for span in soup.findAll('span', {'class': 'a-dropdown-prompt'}):
        if span.text == 'Top reviews':
            continue
        else:
            size = span.text
            resault[size] = 'none'

    for span in soup.findAll('span', {'id': 'priceblock_ourprice'}):
        resault[size] = span.text

print(resault)
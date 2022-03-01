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

url = 'http://www.dsit.org.ir/?cmd=page&Cid=92&title=Kontakt&lang=fa'

session = HTMLSession()
r = session.get(url, headers=headers)
links = r.html.find('iframe', first=True)
#print(links.attrs['src'])
iframe_link = links.attrs['src']
r2 = requests.get(iframe_link, headers=headers)
#print(r2.text)

address = re.findall(r'\"(?=.*\،)[A-Za-z0-9. ,،]{30,100}\"', r2.text)
print(address[0])

phone = re.findall(r'\"(?=[tel:])[a-z0-9:+]{5,20}\"', r2.text)
print(phone[0])

website = re.findall(r'http:+[a-z0-9/:.]+', r2.text)
print(website[0])
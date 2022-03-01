import requests
from bs4 import BeautifulSoup
import xlsxwriter
from fake_headers import Headers


workbook = xlsxwriter.Workbook('resault_amazon.xlsx')
worksheet = workbook.add_worksheet()

search_text = input('please enter book name: ')
search_text = search_text.replace(' ', '+')
url = 'https://www.amazon.com/s?k=' + search_text + '&i=stripbooks-intl-ship'
#print(url)

headers = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    ).generate()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)
title_soup = soup.select('.a-color-base.a-text-normal')
writer_soup = soup.select('.a-color-secondary .a-row')


book = {}
title_list = []
writer_list = []
for i in title_soup:

    title = i.get_text()
    title_list.append(title)

#print(title_list)

for x in writer_soup:
    writer = x.get_text()
    writer_list.append(writer)


#print(writer_list)


#workbook.close()

for i, x in zip(title_list, writer_list):
    book[i] = x


print(book)

book_div_list = []
book_price_list = []
for i in range(0, 17):
    book_div = soup('div', {'data-index': i})
    book_div_list.append(book_div[0].get_text())

    if 'Paperback' in book_div_list[i]:
        book_price = book_div_list[i]
        paperback = book_div_list[i].find('Paperback')+11
        #print(paperback)
        paperback_price = book_price[paperback:paperback+5]
        if '$' in paperback_price:
            paperback_price = paperback_price.replace('$', '')

        try:
            book_price_list.append(float(paperback_price))
        except:
            book_price_list.append('*')

    else:
        book_price_list.append('*')


#print(book_price_list)
#min_price = min(book_price_list.astype('float'))
min_price = min(x for x in book_price_list if x != '*' and x != '\n')
#print(min_price)
min_price_index = book_price_list.index(min_price)
#print(min_price_index)
min_final = {}
min_final[title_list[min_price_index]] = min_price
print(min_final)


#print(book_div_list)
#print(len(book_div_list))
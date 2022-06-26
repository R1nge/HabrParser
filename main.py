import requests
from bs4 import BeautifulSoup
import csv
import datetime
 
r = requests.get('https://habr.com/ru/top/weekly/')
 
soup = BeautifulSoup(r.content, 'html.parser')

arr = []


for title in soup.find_all('a',{'tm-article-snippet__title-link' }):
    d = {}
    d['link'] = 'https://habr.com' + title.get('href')
    for child in title.children:
        correct = str(child)
        d['title'] = correct.replace('<span>','').replace('</span>','')
        arr.append(d)


d = datetime.datetime.now()

filename = '{:%B %d, %Y}'.format(d) + '.csv'
with open(filename, 'w', encoding="utf-8", newline='') as f:
    w = csv.DictWriter(f,['title','link'])
    w.writeheader()
    w.writerows(arr)
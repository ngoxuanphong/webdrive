import requests
from bs4 import BeautifulSoup
import pandas as pd

res = requests.get('https://s.cafef.vn/tin-doanh-nghiep/aaa/Event.chn')
soup = BeautifulSoup(res.text, 'html.parser')
table = soup.find_all('div', {'id':'divTopEvents'})[0]
date = []
event = []
href = []
for li in table.find_all('li'):
    date.append(li.span.text.split(' ')[0])
    event.append(li.a.text)
    href.append('https://s.cafef.vn/'+ li.a['href'])
save = pd.DataFrame({'Date' : date,
                    'event': event,
                    'link': href})
save.to_csv('test.csv', index = False)
print(save)
print(soup.find_all('input', {'id':'hdConfigID'})[0])
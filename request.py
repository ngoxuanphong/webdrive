import requests 
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException  
headers={"Content-Type":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
# r_table = requests.get('https://vn.investing.com//equities/2s-metal-historical-data', headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
# soup = BeautifulSoup(r_table.text, 'html.parser')
# table = soup.find(id="curr_table")
# t = pd.read_html(str(table))
# t


wd = webdriver.Chrome(executable_path='C:\webdrive\chromedriver.exe')
wd.get('https://vn.investing.com//equities/a.j.-plast-dividends')
# wd.get('https://vn.investing.com//equities/2s-metal-dividends')

# get_price(, 'AJ', arr_error, Symbol_error)
from bs4 import BeautifulSoup

# soup = BeautifulSoup(wd.page_source, 'html.parser')
# table_bo = soup.find_all('table',{"id":"DropdownSiblingsTable"})
# if len(table_bo) != 0:
#     filter1 = soup.find_all("table")[1]
# else:
#     filter1 = soup.find_all("table")[0]
# list_ = []
# for i in filter1.tbody.find_all("tr"):
#     list_.append(i.span['title'])
# print(list_)
symbol = 'AJ'
Symbol_error = []
soup = BeautifulSoup(wd.page_source, 'html.parser')
table = soup.find_all('table')
soup = BeautifulSoup(wd.page_source, 'html.parser')
table_bo = soup.find_all('table',{"id":"DropdownSiblingsTable"})
if len(table_bo) != 0:
    filter1 = soup.find_all("table")[1]
else:
    filter1 = soup.find_all("table")[0]
try:
    list_ = []
    for i in filter1.tbody.find_all("tr"):
        list_.append(i.span['title'])
    t = pd.read_html(str(table))[0]
    t['Loại'] = list_
    print(t)
except:
    # arr_error.append(link)
    Symbol_error.append(symbol)
    pd.DataFrame({'Done':arr_error, 'Symbol':Symbol_error}).to_csv('C:\webdrive\dividend2\error.csv')
    # print(link, symbol, 'no link')
    pass 
print(t)
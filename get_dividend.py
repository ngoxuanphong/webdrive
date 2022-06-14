from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException  
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests

import warnings 
warnings.filterwarnings('ignore')
path_to_price = 'C:\webdrive\dividend2\\' 
Name_company = pd.read_excel('C:\webdrive\All_link.xlsx')

wd = webdriver.ChromiumEdge(executable_path='C:\webdrive\Driver\msedgedriver.exe')
# wd = webdriver.Chrome(executable_path='C:\webdrive\chromedriver.exe')

def get_price(link, symbol):
    wd.get(link)
    try:
        wd.find_element_by_xpath('//*[@id="PromoteSignUpPopUp"]/div[2]/i').click()
    except:
        pass

    try:
        element_show_more = wd.find_element_by_id('showMoreDividendsHistory')
        for time1 in range(15):
            element_show_more.click()
            time.sleep(0.5)
    except:
        pass
    soup = BeautifulSoup(wd.page_source, 'html.parser')
    table = soup.find_all('table')
    soup = BeautifulSoup(wd.page_source, 'html.parser')
    table_bo = soup.find_all('table',{"id":"DropdownSiblingsTable"})

    if len(table_bo) != 0:
        filter1 = soup.find_all("table")[1]
    else:
        filter1 = soup.find_all("table")[0]
    list_ = []
    for i in filter1.tbody.find_all("tr"):
        list_.append(i.span['title'])
    t = pd.read_html(str(table))[0]
    print(len(list_), len(t.index))
    t['Loại'] = list_
    t.to_csv(path_to_price + symbol + '.csv')   
    # print(t)

Symbol_error = []
link_error = []
# for i in Name_company.index:
#     link = Name_company['dividends'].iloc[i]
#     symbol = Name_company['Symbol'].iloc[i]
#     try:
#         get_price(link, symbol)
#     except:
#         Symbol_error.append(symbol)
#         link_error.append(link)
#     if i % 50 == 0:
#         pd.DataFrame({'Symbol':Symbol_error, 'link':link_error}).to_csv('C:\webdrive\\error_dividend.csv', index = False)
# pd.DataFrame({'Symbol':Symbol_error, 'link':link_error}).to_csv('C:\webdrive\\error_dividend.csv', index = False)

def Returncheck():
    Name_company = pd.read_csv('C:\webdrive\error_dividend.csv')
    length = len(Name_company.index)
    for i in Name_company.index:
        link = Name_company['link'].iloc[i]
        symbol = Name_company['Symbol'].iloc[i]
        try:
            get_price(link, symbol)
        except:
            Symbol_error.append(symbol)
            link_error.append(link)
        if i % 10 == 0:
            pd.DataFrame({'Symbol':Symbol_error, 'link':link_error}).to_csv('C:\webdrive\\error_dividend.csv', index = False)
    save = pd.DataFrame({'Symbol':Symbol_error, 'link':link_error})
    save.to_csv('C:\webdrive\\error_dividend.csv', index = False)
    if len(save.index) == length:
        return 'Done'
    else:
        print(length, len(save.index))
        return Returncheck()

print(Returncheck())

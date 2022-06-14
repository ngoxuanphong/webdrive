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
# wd.get('https://vn.investing.com')
# wd.find_element_by_xpath('//*[@id="userAccount"]/div/a[1]').click()
# wd.find_element_by_id('loginFormUser_email').send_keys('thiensuofclass@gmail.com')
# wd.find_element_by_id('loginForm_password').send_keys('xuanphong2002')
# wd.find_element_by_xpath('//*[@id="signup"]/a').click()
def get_price(link, symbol):
    wd.get(link)
    try:
        wd.find_element_by_xpath('//*[@id="PromoteSignUpPopUp"]/div[2]/i').click()
    except:
        pass
    try:
        for time in range(15):
            wd.find_element_by_id('showMoreDividendsHistory').click()
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
    print(list_)
    t = pd.read_html(str(table))[0]
    t['Loại'] = list_
    print(t)

link = 'https://vn.investing.com//equities/a.j.-plast-dividends'
symbol = 'AJ'
get_price(link, symbol)
# Symbol_error = []
# link_error = []
# for i in Name_company.index:
#     link = Name_company['dividends'].iloc[i]
#     symbol = Name_company['Symbol'].iloc[i]
#     try:
#         get_price(link, symbol)
#     except:
#         Symbol_error.append(link)
#         link_error.append(symbol)
#     if i % 50 == 0:
#         pd.DataFrame({'Symbol':Symbol_error, 'link':link_error}).to_csv('C:\webdrive\\error_dividend.csv', index = False)
# pd.DataFrame({'Symbol':Symbol_error, 'link':link_error}).to_csv('C:\webdrive\\error_dividend.csv', index = False)

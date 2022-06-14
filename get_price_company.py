from selenium import webdriver
import time

from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests

import warnings 
warnings.filterwarnings('ignore')
path_to_price = 'C:\webdrive\price\\' 
Name_company = pd.read_excel('C:\webdrive\All_link.xlsx')

wd = webdriver.Chrome(executable_path='C:\webdrive\chromedriver.exe')
wd.get('https://vn.investing.com')
element_find_login = wd.find_element_by_xpath('//*[@id="userAccount"]/div/a[1]')
element_find_login.click()
time.sleep(0.5)
element_email = wd.find_element_by_id('loginFormUser_email')
element_email.send_keys('thiensuofclass@gmail.com')
time.sleep(0.5)
element_pass = wd.find_element_by_id('loginForm_password')
element_pass.send_keys('xuanphong2002')
time.sleep(0.5)
element_login = wd.find_element_by_xpath('//*[@id="signup"]/a')
element_login.click()

def get_price(link, symbol):
    wd.get(link)
    element = wd.find_element_by_xpath('//*[@id="widgetFieldDateRange"]')
    element.click()

    element_startDate = wd.find_element_by_id('startDate')
    element_startDate.click()
    element_startDate.clear()
    element_startDate.send_keys('01/01/2005')

    element_endDate = wd.find_element_by_xpath('//*[@id="endDate"]')
    element_endDate.click()
    element_endDate.clear()
    element_endDate.send_keys('22/03/2022')

    element_find = wd.find_element_by_id('applyBtn')
    element_find.click()
    time.sleep(1)

    soup = BeautifulSoup(wd.page_source, 'html.parser')
    table = soup.find_all('table',{"id":"curr_table"})
    t1 = pd.read_html(str(table))[0]
    
    element = wd.find_element_by_xpath('//*[@id="widgetFieldDateRange"]')
    element.click()

    element_startDate = wd.find_element_by_id('startDate')
    element_startDate.click()
    element_startDate.clear()
    element_startDate.send_keys('01/01/1990')

    element_endDate = wd.find_element_by_xpath('//*[@id="endDate"]')
    element_endDate.click()
    element_endDate.clear()
    element_endDate.send_keys('31/12/2005')

    element_find = wd.find_element_by_id('applyBtn')
    element_find.click()
    time.sleep(1)

    soup = BeautifulSoup(wd.page_source, 'html.parser')
    table = soup.find_all('table',{"id":"curr_table"})
    t2 = pd.read_html(str(table))[0]
    if len(t2.index) > 1:
        t = pd.concat([t1, t2])
        t.to_csv(path_to_price + symbol + '.csv')
    else:
        t1.to_csv(path_to_price + symbol + '.csv')

# error_price = []
# link_error = []
# for i in Name_company.index:
#     link = Name_company['price'].iloc[i]
#     symbol = Name_company['Symbol'].iloc[i]
#     if link != '':
#         try:
#             get_price(link, symbol)
#         except:
#             error_price.append(symbol)
#             link_error.append(link)
#             print(link, symbol)
#     else:
#         print(link, symbol)
# pd.DataFrame({'Symbol' : error_price, 'Link_price': link_error}).to_csv('C:\webdrive\\error_price.csv', index = False)

error_df = pd.read_csv('C:\webdrive\error_price.csv')
error_price = []
link_error = []
for i in error_df.index:
    link = error_df['Link_price'].iloc[i]
    symbol = error_df['Symbol'].iloc[i]
    if link != '':
        try:
            get_price(link, symbol)
        except:
            error_price.append(symbol)
            link_error.append(link)
            print(link, symbol)
    else:
        print(link, symbol)
pd.DataFrame({'Symbol' : error_price, 'Link_price': link_error}).to_csv('C:\webdrive\\error_price.csv', index = False)
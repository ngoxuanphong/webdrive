from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException  
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
wd = webdriver.ChromiumEdge(executable_path='C:\webdrive\Driver\msedgedriver.exe')
import os
import glob
import shutil
path = 'C:\webdrive\\'
df_symbol = pd.read_csv(f"{path}InforCompanyVietnam.csv")
dirpath = os.path.join(f'{path}VOLUME_RAW1')
if (os.path.exists(dirpath) == False) or (os.path.isdir(dirpath) == False):
    os.mkdir(dirpath)

def get_event(symbol):
    wd.get(f'https://s.cafef.vn/tin-doanh-nghiep/{symbol}/Event.chn')
    time.sleep(0.1)
    wd.find_element_by_xpath('//*[@id="a4"]').click()
    wd.find_element_by_xpath('//*[@id="a4"]').click()
    wd.find_element_by_xpath('//*[@id="a4"]').click()
    time.sleep(0.1)
    soup = BeautifulSoup(wd.page_source, 'html.parser')
    table = soup.find_all('div', {'id':'divTopEvents'})[0]
    date = []
    event = []
    href = []

    for li in table.find_all('li'):
        date.append(li.span.text.split(' ')[0])
        event.append(li.a.text)
        href.append('https://s.cafef.vn/'+ li.a['href'])
    for i in range(15):
        try:
            wd.find_element_by_xpath('//*[@id="aNext"]').click()
            time.sleep(0.1)
            soup = BeautifulSoup(wd.page_source, 'html.parser')
            table = soup.find_all('div', {'id':'divTopEvents'})[0]
            for li in table.find_all('li'):
                date.append(li.span.text.split(' ')[0])
                event.append(li.a.text)
                href.append('https://s.cafef.vn/'+ li.a['href'])
        except:
            break
    save = pd.DataFrame({'Date' : date,
                        'event': event,
                        'link': href})
    save.to_csv(f'{path}/{symbol}.csv', index = False)

# error = []
# for symbol in df_symbol['Company']:
#     print(symbol, end='  ')
#     try:
#         get_event(symbol)
#         print('Done!!!!')
#     except:
#         error.append(symbol)
#         print('loi', symbol)
# pd.DataFrame({'Error':error}).to_csv(f'{path}error.csv', index = False)
get_event('c69')
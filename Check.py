# -*- coding: utf-8 -*-
"""

@author: kyle82
"""

import requests as rq
from bs4 import BeautifulSoup as bs
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
e

import time
import pandas as pd
       


# configure for selenium
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222") 
options.add_argument('window-size=1920x1080')
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-dev-shm-usage")
#driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
driver = webdriver.Chrome(r'D:/chromedriver', options=options)

from datetime import datetime

url = "https://www.dailyair.com.tw/Dailyair/Page/WOWP/"
driver.get(url)

df1 = pd.DataFrame()
r_df1 = pd.DataFrame()
# departure
while True:
    try:
        time.sleep(1)
        
        
        
        #loop
        
        fdate = (driver.find_element(By.XPATH, r'//*[@id="BodyContent_ctl00_go_wowp_lbl_flydate"]').text)
        
        
        df = pd.read_html(driver.page_source)[0]
        df.drop(df.columns[[5]], axis=1, inplace=True)
        df.insert(5, "Date", fdate)
        
        df['訂位狀態'] = df['訂位狀態'].replace(r'^\s*$', fdate, regex=True)
        
        
        
        df1= df1.append(df, ignore_index=True)
        
        time.sleep(1)
        driver.find_element(By.XPATH,r'//*[@id="BodyContent_ctl00_GoNavTab5_Line1"]').click()
        
        
        
    # out of order
    except Exception:
        print(Exception,"error page")
        continue
    

# return
while True:
    try:
        time.sleep(1)
        
        
        
        #loop
        
        rdate = (driver.find_element(By.XPATH, r'//*[@id="BodyContent_ctl00_go_wowp_lbl_flydate"]').text)
        
        
        r_df = pd.read_html(driver.page_source)[0]
        r_df.drop(r_df.columns[[5]], axis=1, inplace=True)
        r_df.insert(5, "Date", rdate)

        
        r_df1= r_df1.append(r_df, ignore_index=True)
        
        time.sleep(1)
        driver.find_element(By.XPATH,r'//*[@id="BodyContent_ctl00_GoNavTab5_Line2"]').click()
        
        
        
        
    # out of order
    except Exception:
        print(Exception,"error page")
        continue


r_df1.to_csv('return.csv',encoding='utf-8-sig')

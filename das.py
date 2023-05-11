import requests
from selenium import webdriver
from lxml import html
import re
import time
import json
from loguru import logger
import os
from openpyxl import Workbook
from openpyxl import load_workbook
import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from jpype import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 判断当前页面是否存在低价域名
def judge():
    for i in range(0, 10):
        price = ''
        price = driver.find_elements_by_xpath('//div[@class="item_tail"]')[i].text
        name = driver.find_elements_by_xpath('//div[@class="item_main"]')[i].text
        print(name)
        price1 = price.replace(',', '')
        price2 = price1.replace('CKB', '')
        price3 = int(price2)
        print(price3)
        # print(name + ' ' + price3)
        if int(price3) < 300:
            print('存在低价域名')
            time.sleep(999999)


# 启用带插件的浏览器
option = webdriver.ChromeOptions()
# option.add_argument("--user-data-dir="+r"C:/Users/Administrator.USER-20191227TJ/AppData/Local/Google/Chrome/User Data/")
option.add_argument("--user-data-dir=" + r"C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/")
driver = webdriver.Chrome(chrome_options=option)

# 先想办法打开metamask界面，登录，然后打开zapper
driver.get('https://bestdas.com/')
driver.maximize_window()
time.sleep(1)
count = 0
while 1:
    driver.find_element_by_xpath('//button[@class="button index_random-refresh button__size__middle"]').click()
    time.sleep(3)
    if count == 20:
        driver.refresh()
        time.sleep(3)
        count = 0
    judge()
    count += 1
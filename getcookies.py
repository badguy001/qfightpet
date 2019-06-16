# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import re
import platform

options = Options()
options.add_argument('--headless')
# options.add_argument('--user-data-dir=D:\\user_data')
# options.add_argument('--window-size=1366,768')


options.add_argument('--no-sandbox')

# 查看是否已经登录，没有登录的话在生成login.png进行扫码登录
def login(username, password):
    png_name = 'login.png'
    browser.delete_all_cookies()
    browser.get(
        'https://ui.ptlogin2.qq.com/cgi-bin/login?appid=614038002&style=9&s_url=http%3A%2F%2Fdld.qzapp.z.qq.com%2Fqpet%2Fcgi-bin%2Fphonepk%3Fcmd%3Dindex%26channel%3D0')
    browser.find_element_by_xpath('//input[@id="u" and @name="u"]').clear()
    browser.find_element_by_xpath('//input[@id="u" and @name="u"]').send_keys(username)
    time.sleep(1)
    browser.find_element_by_xpath('//input[@id="p" and @name="p"]').send_keys(password)
    time.sleep(1)
    browser.find_element_by_xpath('//div[@id="go"]').click()
    time.sleep(10)
    if browser.current_url == 'http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?cmd=index&channel=0':
        return 1
    else:
        return 0


def savecookies(filename):
    cookies = browser.get_cookies()
    with open(filename, 'w') as f:
        for cookie in cookies:
            f.write(cookie.get('name') + '=' + cookie.get('value') + '\n')


def getusers(filename):
    with open(filename, 'r') as f:
        us = f.read()
        p = re.compile(r'([^\n]+)')
        us = re.findall(p, us)
        result = []
        for u in us:
            u = u.split('/')
            result.append({"username": u[0], "password": u[1]})
    return result


def browser_close():
    browser.close()
    browser.quit()

def open_browser():
    global browser
    if platform.system() == 'Linux':
        exec_path = 'chromedriver'
    else:
        exec_path = 'chromedriver.exe'
    browser = webdriver.Chrome(executable_path=exec_path, chrome_options=options)


open_browser()
u_file = 'users.txt'
us = getusers(u_file)
cookiefile = 'cookies'
for idx, u in enumerate(us):
    if login(u.get("username"), u.get("password")):
        savecookies(cookiefile + str(idx))
        time.sleep(10)
browser_close()

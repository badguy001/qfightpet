# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import platform
import urlparse
import json

options = Options()
#options.add_argument('--headless')
# options.add_argument('--user-data-dir=D:\\user_data')
options.add_argument('--window-size=1366,768')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')

options.add_argument('--no-sandbox')

# 查看是否已经登录，没有登录的话在生成login.png进行扫码登录
def login(username, password):
    browser.delete_all_cookies()
    browser.get(
        'https://ui.ptlogin2.qq.com/cgi-bin/login?appid=614038002&style=9&s_url=http%3A%2F%2Fdld.qzapp.z.qq.com%2Fqpet%2Fcgi-bin%2Fphonepk%3Fcmd%3Dindex%26channel%3D0')
    browser.find_element_by_xpath('//input[@id="u" and @name="u"]').clear()
    browser.find_element_by_xpath('//input[@id="u" and @name="u"]').send_keys(username)
    time.sleep(1)
    browser.find_element_by_xpath('//input[@id="p" and @name="p"]').send_keys(password)
    time.sleep(1)
    browser.find_element_by_xpath('//div[@id="go"]').click()
    time.sleep(2)
    sleep_second = 60
    while sleep_second > 0:
        if urlparse.urlparse(browser.current_url).hostname == "dld.qzapp.z.qq.com":
            return 1
        else:
            sleep_second = sleep_second - 5
            time.sleep(5)
    return 0


def savecookies(filename, users, free_lock=True):
    if free_lock:
        users["login_lock_flag"] = False
    with open(filename, "w") as f:
        f.write(json.dumps(users, indent=2, ensure_ascii=False).encode("utf-8"))


def getusers(filename):
    is_lock = False
    while not is_lock:
        if int(time.strftime("%S", time.localtime())) % 6 in [3, 4, 5]:
            with open(filename, 'r') as f:
                tmp = json.loads(f.read())
            if not tmp["check_lock_flag"]:
                tmp["login_lock_flag"] = True
                is_lock = True
                savecookies(filename, tmp, free_lock=False)
            else:
                time.sleep(1)
        else:
            time.sleep(1)
    return tmp

def browser_close():
    browser.close()
    browser.quit()

def open_browser():
    global browser
    if platform.system() == 'Linux':
        exec_path = './chromedriver'
    else:
        exec_path = 'chromedriver.exe'
    browser = webdriver.Chrome(executable_path=exec_path, chrome_options=options)


open_browser()
u_file = 'users.json'
us = getusers(u_file)
for idx, u in enumerate(us.get("users")):
    if not u.get("is_valid") and login(u.get("yonghu"), u.get("mima")):
        u["cookies"] = browser.get_cookies()
        u["is_valid"] = True
        u["login_date"] = time.strftime("%Y%m%d%H%M%S", time.localtime())
        time.sleep(10)
savecookies(u_file, us)
browser_close()

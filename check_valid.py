# -*- coding: UTF-8 -*-

import requests
import requests.cookies
import json
import time
import urlparse

user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
url = "http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk"
users_file = "users.json"
users = dict()
headers = {'user-agent': user_agent,
           "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3",
           "Accept - Encoding": "gzip, deflate",
           "Accept - Language": "zh - CN, zh;q = 0.9"
           }


def get_users(file):
    is_lock = False
    while not is_lock:
        if int(time.strftime("%S", time.localtime())) % 6 in [0, 1, 2]:
            with open(file, 'r') as f:
                tmp = json.loads(f.read())
            if not tmp["login_lock_flag"]:
                tmp["check_lock_flag"] = True
                is_lock = True
                save_result(file, tmp, free_lock=False)
            else:
                time.sleep(1)
        else:
            time.sleep(1)
    return tmp


def save_result(file, us, free_lock=True):
    if free_lock:
        us["check_lock_flag"] = False
    with open(file, 'w') as f:
        f.write(json.dumps(us, indent=2, ensure_ascii=False).encode("utf-8"))


def get_cookiesjar(cookies):
    result = requests.cookies.RequestsCookieJar()
    for ck in cookies:
        result.set(ck.get("name"), ck.get("value"), domain=ck.get("domain"), path=ck.get("path"))
    return result


users = get_users(users_file)
for user in users.get("users"):
    if user.get("is_valid"):
        cookiesjar = get_cookiesjar(user.get("cookies"))
        resp = requests.get(url, cookies=cookiesjar, headers=headers)
        if urlparse.urlparse(resp.url).hostname != "dld.qzapp.z.qq.com":
            user["is_valid"] = False
    user["last_check_date"] = time.strftime("%Y%m%d%H%M%S", time.localtime())
    time.sleep(1)
save_result(users_file, users)

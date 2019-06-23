# -*- coding: UTF-8 -*-

import os
import re
import time
from scrapy import cmdline
import json
import time

# while True:
users_file = "users.json"
middle_file = "cookies.txt"

with open(users_file, 'r') as f:
    users = json.loads(f.read())
for user in users.get("users"):
    if user.get("is_valid", False):
        start_time = time.time()
        with open(middle_file, 'w') as one:
            one.write(json.dumps(user.get("cookies", "{}"), indent=2))
        print "user:" + user.get("yonghu", "") + " start, time:" + str(start_time)
        os.system("scrapy crawl qfightpet")
        # cmdline.execute('scrapy crawl qfightpet'.split())   # 调试
        print "user:" + user.get("yonghu", "") + " end, time:" + str(time.time()) + ", " + str(time.time() - start_time) + "second"
    else:
        print "user:" + user.get("yonghu", "") + " cookies is unvaild"
    time.sleep(1)


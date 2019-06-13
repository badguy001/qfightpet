from scrapy import cmdline
import os
import re


files=os.listdir('.')
for file in files:
    p = re.compile(r'^cookies[0-9]+$')
    if os.path.isfile(file) and re.search(p, file) is not None:
        with open(file,'r') as file_one:
            with open("cookies.txt",'w') as one:
                one.write(file_one.read())
        cmdline.execute('scrapy crawl qfightpet'.split())
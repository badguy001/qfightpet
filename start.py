import os
import re

while True:
    files = os.listdir('.')
    for file in files:
        p = re.compile(r'^cookies[0-9]+$')
        if os.path.isfile(file) and re.search(p, file) is not None:
            with open(file, 'r') as file_one:
                with open("cookies.txt", 'w') as one:
                    one.write(file_one.read())
            print file
            os.system("scrapy crawl qfightpet")

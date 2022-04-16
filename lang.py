from typing import final
import requests
from bs4 import BeautifulSoup as bs4
import os
import sys
import time
from datetime import datetime

### let make our bot
def programminglangrank():
    url = "https://www.tiobe.com/tiobe-index/"
    site = requests.get(url)
    soup = bs4(site.content , "html.parser")
    result = soup.find_all("tr")
    for i in result:
        print(i.get_text())

programminglangrank()
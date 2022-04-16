import requests 
from bs4 import BeautifulSoup as bs4
import random
from random import shuffle
import time
import os
import sys
def hackernews():
    ### let make out bot
    url = "https://news.ycombinator.com/"
    site = requests.get(url)
    soup = bs4(site.content, 'html.parser')
    #print(soup.prettify())
    result = soup.find_all("a" , class_="titlelink")    
    title = []
    for i in result:
        title.append(i.get_text())
    ### make the final tiitle list
    final_title = []
    for i in range(10):
        final_title.append(title[i])

    ### make the final urls list
    result2 = soup.find_all("span" , class_="sitestr")
    result3 = []
    for i in result2:
        result3.append(i.get_text())

    final_urls = []
    for i in range(10):
        final_urls.append(result3[i])

    final_real_urls = []
    for i in result:
        final_real_urls.append(i["href"])
    finale_urls_real = []
    for i in range(10):
        finale_urls_real.append(final_real_urls[i])
    return final_title , finale_urls_real
    #print(final_urls)
    #finale_urls_real)

hackernews()
from typing import final
import requests
from bs4 import BeautifulSoup as bs4
import os
import sys
import time
from datetime import datetime

### let make our app
def topimdbmovie():
    url = "https://www.imdb.com/chart/top/"
    site = requests.get(url)
    soup = bs4(site.content, 'html.parser')
    result = soup.find_all("td" , class_="titleColumn")
    title = []
    for i in result:
        title.append(i.get_text())
    final_title = []
    for i in title:
        i = i.replace(" " , "")
        j = i.replace("\n" , "")
        final_title.append(j)

    print(final_title)
    
    result2 = soup.find_all("td" , class_="ratingColumn imdbRating")
    score = []
    for i in result2:
        score.append(i.get_text())
    final_score = []
    for i in score:
        i = i.replace("\n" , "")
        final_score.append(i)
        
    print(final_score)

    with open("imdb.txt" , "w") as f:
        j = 0
        for i in final_title:
            f.write(f"{i} ====> {final_score[j]}\n")
            j += 1



topimdbmovie()
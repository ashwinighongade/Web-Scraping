
import json

import requests
from bs4 import BeautifulSoup
from task1 import fun 
import os
list1=[]

for i in fun:
    url=i['link']
    list=[]
    def scrap_movie_cast(movie_cast_url):
        raw=requests.get(url)
        soup=BeautifulSoup(raw.text,"html.parser")
        main_div=soup.find('div',class_="castSection" )
        sub_div=main_div.find_all('div',class_="cast-item media inlineBlock")
        for i in sub_div:
            link=i.find('a',class_="unstyled articleLink") 
            link1=link['href']
            # print(link1)
            name=i.find('span').get_text().strip()
            # print(name)
            dict={}
            dict['Link']=link1
            dict['Actor_Name']=name
            # print(dict)
            list.append(dict)
        list1.append(list)
        print(list1)
        with open ("p_Movie_casts.json","w") as f:
            json.dump(list1,f,indent=4)
        return list1
       
    scrap_movie_cast(url)
    
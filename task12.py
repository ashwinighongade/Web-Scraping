import json

import requests
from bs4 import BeautifulSoup
from task1 import fun 
import os

# for i in fun:
#     url=i['link']
#     def scrap_movie_cast(movie_cast_url):

url=fun[0]['link'] 
def scrap_movies_cast(movie_cast_url):
    list1=[]
    dict={}
    for i in fun:
        # url1="http://"+i['link']
        if i['link']==movie_cast_url:
            url1=i['link'][33:]
    var=os.path.exists("/home/desktop/Ashwini Ghongade/python/Web scrapping"+url1+".json")
    # print(var)
    if var==True:
        with open ("12_Movie_casts.json","r") as f:
            a=json.load(f)
    else:
        raw=requests.get(url)
        soup=BeautifulSoup(raw.text,"html.parser")
        main_div=soup.find('div',class_="castSection" )
        sub_div=main_div.find_all('div',class_="cast-item media inlineBlock")

        for i in sub_div:
            link=i.find('a',class_="unstyled articleLink") 
            link1=link['href']
            # print(link1)
            name=i.find('span').get_text().strip()
            
            dict['Link']=link1
            dict['Actor_Name']=name
            # print(dict)
            list1.append(dict)
        # print(list1)
        


        with open ("12_Movie_casts.json","w") as f:
            json.dump(list1,f,indent=4)
    return list1
scrap_movies_cast(url)
sam=scrap_movies_cast
# for i in sam:
#     print(i)




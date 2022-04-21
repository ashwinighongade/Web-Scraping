
import requests
import os
import json
from bs4 import BeautifulSoup
from task1 import fun
from task4 import scrap_movie_details


url=fun[0]['link'] 
def movie_details_with_url(URL):
    for i in fun:
        # url1="http://"+i['link']
        if i['link']==URL:
            url1=i['link'][33:]
            NAME=i["name"]
            # print(url1)
            # print(NAME)
    # # name1=movie_id+"json"
    var=os.path.exists("/home/desktop/Ashwini Ghongade/python/Web scrapping"+url1+".json")
    # print(var)
    if var==True:
        with open ("movies_details_url.json","r") as f:
            a=json.load(f)
    else:
        data=scrap_movie_details(URL)
        with open ("8_movies_details_url.json","w") as f:
            json.dump(data,f,indent=4)
    return data
movie_details_with_url(url)





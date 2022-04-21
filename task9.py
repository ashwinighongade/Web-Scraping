import requests
import os
import random
import time
import json
from bs4 import BeautifulSoup
from task1 import fun
from task4 import scrap_movie_details


# for i in fun[:10]:
#     url=i['link']
#     def movies_details1(movies_detail):
#         # random_sleep=random.randint(1,3)
#         id=""
#         for i in movies_detail[33:]:
#             id+=i
#         n_file="/home/ashwini/Desktop/Ashwini Ghongade/Python/Web scraping/"+id+".json"
#         var=os.path.exists(n_file)
#         # print(var)
#         if var==True:
#             with open(n_file,"r")as f:
#                 a=json.loads(f)
#             print(a)

#         else:
#             # time.sleep(random_sleep)
#             data=scrap_movie_details(url)
#             with open(n_file,"w")as f:
#                 json.dump(data,f,indent=4)
#             print(data)

#     # url=fun[0]['link']
#     movies_details1(url)

list1=[]
for i in fun[:10]:
    url=i['link']
    def movie_details_with_url(URL):
        random_sleep=random.randint(1,3)
        for i in fun:
            if i['link']==URL:
                url1=i['link'][33:]
        var=os.path.exists("/home/desktop/Ashwini Ghongade/python/Web scrapping"+url1+".json")
        # print(var)
        if var==True:
            with open ("url_movies_details.json","r") as f:
                a=json.load(f)
        else:
            time.sleep(random_sleep)
            data=scrap_movie_details(URL)
            list1.append(data)
            with open ("9_url_movies_details.json","w") as f:
                json.dump(list1,f,indent=4)
        return list1
    movie_details_with_url(url)





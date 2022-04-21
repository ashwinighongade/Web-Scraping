
import json
from task5 import movies_list_d
from bs4 import BeautifulSoup
import requests


def analyse_movies_genre(movies_details):
    gener_list=[]
    genre_dic={}
    for movies in movies_details:
        print(movies)
        genre=movies['Genre']
        for i in genre:
            if i not in gener_list:
                gener_list.append(i)
    print(gener_list)
    for i in gener_list:
        key=i
        count=0
        for k in movies_details:
            s=k['Genre']
            for x in s:

                if i==x:
                    count+=1
                genre_dic.update({key:count})
    print(genre_dic)
    with open("11_analyse_movies_genre.json","w") as f:
        json.dump(genre_dic,f,indent=4)
    return genre_dic

analyse_movies_genre(movies_list_d)

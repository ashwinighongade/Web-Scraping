# import json

from pprint import pprint
import requests
from bs4 import BeautifulSoup
from task2 import dec1
import json


def group_by_decade(movie):
    moviedec={}
    list1=[]
    for i in movie:
        print(i)

        # var=int(i)%10
        # print(var)
    #     decade=int(i)-var
    #     # print(decade)
    #     if decade not in list1:
    #         list1.append(decade)
    #     list1.sort()
    #     # print(list1)
    # for i in list1:
    #     moviedec[i]=[]
    # for i in moviedec:
    #     dec=i+9
    #     # print(dec)
    #     for x in movie:
    #         if int(x)<=dec and int(x)>=i:
    #             for n in movie[x]:
                    
    #                 moviedec[i].append(n)
    # # print(moviedec)
    # with open("3_movies_decade.json","w") as f:
    #     json.dump(moviedec,f,indent=4)

    # return moviedec
    # # pprint(moviedec)

group_by_decade(dec1)

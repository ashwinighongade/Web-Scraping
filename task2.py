
from task1 import fun
import requests
from bs4 import BeautifulSoup
import json
import pprint


def group_by_year(movie):
    years=[]
    dict1={}
    for i in movie:
        if i["year"] not in years:
            years.append(i['year'])
#         print(years)
# group_by_year(fun)
        
    for i in years:
        dict1[i]=[]

# group_by_year(fun)
        
    for j in movie:
        year=j['year']
        for k in dict1:
            if str(k)==str(year):
                dict1[k].append(j)
    # s= sorted(dict1.items())
#     return s    
# print(group_by_year(fun))
        
    with open ("2_movies_years2.json","w")as f:
        json.dump(dict1,f,indent=4)
    return dict1
    # pprint.pprint(dict1)
dec1=group_by_year(fun)


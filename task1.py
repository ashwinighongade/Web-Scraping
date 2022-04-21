import requests
from bs4 import BeautifulSoup
# import bs4 
import json
import pprint
# def scrap_top():
var="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
r=requests.get(var)
# print(r.text)
soup=BeautifulSoup(r.text,'html.parser')
# print(soup)
def scrap_top():

    main_div=soup.find('div',class_="panel-body content_body allow-overflow")
    tbody=main_div.find('table',class_="table")
    trs=tbody.find_all('tr')
    # print(trs)
    
    movies_list=[]
    for tr in trs[1:]:
        position1=tr.find('td',class_="bold").get_text().strip()
        position=position1[:-1]
        name = tr.find('a',class_="unstyled articleLink").get_text().strip()
        name1=name[0:len(name)-7]
        # print(name1)
        year=name[len(name)-5:len(name)-1]
        Rating=tr.find('span',class_="tMeterScore").get_text().strip()
        view=tr.find('td',class_="right hidden-xs").get_text()
        link=tr.find('a',class_="unstyled articleLink")
        url=link["href"]
        link1="https://www.rottentomatoes.com"+url
        details={}
        details.update({'position':position,'name':name1,'year':year,'rating':Rating,'view':view,'link':link1})
        # details['position']=position
        # details['name']=name1
        # details['year']=year
        # details['Rating']=Rating
        # details['view']=view
        # details['link']=link1
        movies_list.append(details)
    # print(movies_list)   
    with open("1_movies_List.json","w") as f:
        json.dump(movies_list,f,indent=4)
    return movies_list
    # pprint.pprint(movies_list)

# scrap_top()
fun=scrap_top()
   
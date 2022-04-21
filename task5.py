import requests
import json
from bs4 import BeautifulSoup
from task1 import fun
from pprint import pprint
# from task4 import scrap_movie_details
movies_details=[]
for i in fun:
    url=i['link']
    # url = "https://"+url
    # print(url)
    def get_movies_list_details(movies_url):
        page=requests.get(movies_url)
        soup=BeautifulSoup(page.text,'html.parser')
        title=soup.find('div',class_="col mob col-center-right col-full-xs mop-main-column")
        title1=title.find('div',class_="thumbnail-scoreboard-wrap")
        poster=title1.find('img',class_="posterImage js-lazyLoad")
        poster1=poster['src']
        name=title1.find('h1',class_="scoreboard__title").get_text()
        info=soup.find('div',class_="panel-body content_body")
        m_info=info.find('div',class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
        genre=info.find('div',class_="meta-value genre").get_text().split()
        sub_title=info.find_all('li',class_="meta-row clearfix")
        one_dict={}
        one_dict['Name']=name
        for i in sub_title:
            key=i.find('div',class_="meta-label subtle").get_text().replace(":","")     
            value=i.find('div',class_="meta-value").get_text().replace(" ","").replace("\n","").strip()
            one_dict[key]=value
            # print(one_dict)
        time=int(one_dict['Runtime'][0])*60
        time=time+int(one_dict['Runtime'][2:-1])
        one_dict['Runtime']=str(time)+'m'
        one_dict['Poster_image_url']=poster1
        one_dict['Movie_info']=m_info
        one_dict['Genre']=genre
        # pprint(one_dict)
        movies_details.append(one_dict)
        # print(movies_details)
        with open ("5_movie_all_details.json","w")as f:
            json.dump(movies_details,f,indent=4)
        return movies_details
    movies_list_d=get_movies_list_details(url)

import json
from task1 import fun
from task5 import movies_list_d
from task4 import scrap_movie_details
# # import requests

# def analyse_director_language(movies_list):
#     directors_dic={}
#     for movie in movies_list:
#         print(movie['Director'])
#         irector=movie['Director']
#         directors_dic[director]={}
#         count=0
#         for i in range(len(movies_list)):
#             for director in directors_dic:
#                 if director in movies_list[i]['Director']: 
#                     for language in movies_list[i]['Original Language']:
#                         directors_dic['director']['language']=0
#         for i in range(len(movies_list)):
#             for director in directors_dic:
#                 if director in movies_list[i]['Director']: 
#                     for language in movies_list[i]['Original Language']:
#                         directors_dic['director']['language']+=1
#         print(directors_dic)
# analyse_director_language(movies_list_d)

def analyse_director_language(movies_list):
    directors_dic={}
    for movies in movies_list:
        director=movies['Director']
        language=movies['Original Language']
        directors_dic[director]={}
        count=0
        for i in range(len(movies_list)):
            if director==movies_list[i]['Director']:
                language==movies_list[i]['Original Language']
                count+=1
                directors_dic[director].update({language:count})
    with open("10_language_and_director.json","w") as f:
        json.dump(directors_dic,f,indent=4)
    return directors_dic    
analyse_director_language(movies_list_d)




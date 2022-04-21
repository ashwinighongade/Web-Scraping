
import json
# import requests
# from Task12 import scrap_movie_cast
# from task12 import scrap_movie_cast
# import json
# from task13 import movies_details_cast

# def analyse_co_actors(movies_details):
#     for cast in movies_details[:5]:
#         print(cast)
#         for i in cast['cast']:
#             pass
#             print(i)
# analyse_co_actors(movies_details_cast)


def analyse_ca_actors():
    list1=[]
    with open("13_Movies_details_with_cast.json","r") as f:
        data1=json.load(f)
    # count=0
    for i in data1[:5]:
        a=i
        # print(a)
        b=(a["cast"])
        for j in b:
            list1.append(j["Name"])
            # count+=1
    # print(list1)
    # print(count)
    # N_list=[]
    # count=0
    # for i in list1:
    #     if i not in N_list:
    #         N_list.append(i)
    #         count+=1
    # print(N_list)
    # print(count)
    
    list2=[]

    for x in list1:
        count=0
        for i in data1[:5]:
            a=i
            # print(a)
            b=(a["cast"])
            # print(b)
            for j in b:
                if x==j["Name"]:
                    count+=1
            j.update({"No_Movies":count})
        list2.append(j)
    print(list2)


    
analyse_ca_actors()
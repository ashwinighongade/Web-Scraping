import json 
from pprint import pprint
# list1=[]
# def movies_details_cast():
#     with open("12_Movie_casts.json","r") as f:
#         data=json.load(f)
#     with open("4_one_movie_details.json","r") as f:
#         data1=json.load(f)
#         data1["cast"]=data
#     print(data1)
#     with open ("13 _movies.json","w") as f:
#         json.dump(data1,f,indent=4)
# movies_details_cast()





list1=[]
def movies_details_cast():
    with open("p_Movie_casts.json","r") as f:
        data=json.load(f)
    with open("5_movie_all_details.json","r") as f:
        data1=json.load(f)
    for i in range(len(data1[:5])):
        a=data1[i]
        a.update({"cast":data[i]})
        list1.append(a)
    print(list1)
    with open("13_Movies_details_with_cast.json","w") as f:
        json.dump(list1,f,indent=4)

    # a=data1[:3]
    # print(a)
    # i=0
    # while i<len(data1[:3]):
    #     a=data1[i]
    #     print(a)
    # #     # b=data[i]
    # #     # a["A_Cast"]=b
    # # #     list1.append(a)
    #     i=+1
    # # print(list1)
   

movies_details_cast()




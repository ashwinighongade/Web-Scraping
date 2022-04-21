import json
def analyse_movies_language():
    list1=[]
    with open("5_movie_all_details.json","r")as f:
        lan=json.load(f)
    
    for i in lan:
        if i['Director'] not in list1:
        # print(i['Original Language'])
            list1.append(i['Director'])
    # print(list1)
    
    langauge={}
    list2=[]
    for  i in list1:
        count=0
        j=0
        while j<len(lan):
            # if i in list1:
            if i==lan[j]['Director']:
                    count+=1
            j+=1
        langauge.update({i:count})
    list2.append(langauge)
    with open("7_analyse_movies_Director.json","w") as f:
        json.dump(langauge,f,indent=4)
    return list2
    # print(list2)
    
analyse_movies_language()
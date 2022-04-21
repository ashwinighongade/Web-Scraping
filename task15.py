import json
def analyse_actors():
    list1=[]
    list2=[]
    with open("13_Movies_details_with_cast.json","r") as f:
        data1=json.load(f)
    # count=0
    for i in data1[:5]:
        a=i
        # print(a)
        b=(a["cast"])
        
        for j in b:
            list2.append(j["Link"])
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
    dict1={}
    
    for x in range(len(list1)):
        dict1[(list2[x])]={}
        # print(dict1)
        count=0
        for i in data1[:5]:
           
            a=i
            # print(a)
            b=(a["cast"])
            # print(b)
            for j in b:
                
                if list1[x]==j["Name"]:
                    count+=1
            dict1[(list2[x])].update({"Name":j["Name"],"No of Movies":count})
    with open("15_analyse_no_movies.json","w") as f:
        json.dump(dict1,f,indent=4)  
        



    
analyse_actors()
import json
def analyse_co_actor():
    with open("13_Movies_details_with_cast.json","r") as f:
        data1=json.load(f)
    list1=[]
    for i in data1[:5]:
        # print(i)
        list2=[]
        a=i
        # print(a)
        b=(a["cast"])
        # print(b)
        for j in b:
            
            list2.append(j["Actor_Name"])
        list1.append(list2)
    print(list1)
    
    for x in list1:
        # print(x)
        for i in range(len(x)):
            # print(x[i])
            count=0
            a=x[i]
            b=x[i+1]
            if b==x[-1]:
                break
            else:
                for j in list1:
                    if a in j and b in j:
                        count+=1
                # print(count)
                print(a,"with",b,"No of frequency",count)
                
                
            
    
analyse_co_actor()

# ab - srk 3
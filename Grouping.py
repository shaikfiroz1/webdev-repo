def group (lst) :
    dic={}
    for ele in lst :
        
        s =len(ele)
        if s in dic :
            dic[s].append(ele)
        else :
            dic[s]= [ele]
    return dic
    

print(group(["there", "maps", "world", ""]))



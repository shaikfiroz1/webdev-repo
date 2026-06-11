def count_all(t):
    total =0 

    for item in t :
     if isinstance(item, tuple):
        total += count_all(item)
     else :
        total +=1
    return total
    
t = (1, (2, 3), (4, (5, 6)), 7,8,20,(1,2,4,5,6,7,78,8))
print(count_all(t))

        
t = (1, 3, 2, 3, 3, 2, 1, 3, 3)

max_count =0 
frequncy = None


for i in range (len(t)) :
    count =0 
    for j in range ( len(t)):
        if t[i] == t [j]:
            count +=1
            if count > max_count:
                max_count=count
                frequncy=t[j]
                print ("the value of j is ", t[j])
               

print("count : ", max_count)
print("Frequncy : ", frequncy) 

# with open ("create.txt", "a") as f :
#     f.write ("\nhello.firoz")


# with open ("create.txt", "r") as f1 :
#     content = f1.read()
#     print (content)


# total =0 
# with open("create.txt", "r", encoding="utf-8") as f:
#     for line in f :
#         total  +=1
# print(total)


words_count =0 

with open("create.txt", "r", encoding="utf-8") as f:
    for line in f :
        words = line.split()
        print (type(words))
        print(words)
        words_count +=len(words)
print(words_count)

with open ("create.txt", "a") as f :
    f.write ("\nhello.firoz")


with open ("create.txt", "r") as f1 :
    content = f1.read()
    print (content)
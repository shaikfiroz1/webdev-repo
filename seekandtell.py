# with open ("test", "r") as f :

#    print (f.seek(5,0))

#    print (f.tell() )



with open("test", "r") as f :
    content = f.read ()
    print (f.tell())
    f.seek(0)
    print (f.tell())
names = ('Raju', 'Firoz', 'Sita')
scores = (85, 90, 78)

new=[]

for i , j in zip(names, scores) :
    new.append((i,j))

print (new)
    
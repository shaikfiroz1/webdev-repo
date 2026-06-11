words = ['apple', 'mango', 'banana', 'banana', 'mango', 'grape']

seen =set()
duplicates = set()

for n in words :
    if n in seen :
        duplicates.add(n)
    else :
        seen.add(n)
print (duplicates)

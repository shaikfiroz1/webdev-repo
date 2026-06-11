a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
s = set()

for n in a:
    if n not in b:
        s.add(n)

print(s)

print (a^b)
print (a & b)
print (a | b)
print (a-b)
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 25}

# merged = dict(d1)
# for k,v in d2.items :
#     merged[k] = merged.get(k, 0) +v
# print (merged)



new = {}

for k, v in d1.items():
    new[k] = v

    for m, n in d2.items():
        if k == m:
            new[k] = v + n
            break

for m, n in d2.items():
    if m not in new:
        new[m] = n

print(new)
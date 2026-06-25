scores = {'Raju': 85, 'parimalla': 90, 'Sita': 1, 'Kiran': 2}

loser = None
c = float('inf')

for k, v in scores.items():
    if v < c:
        c = v
        loser = k

print("Topper:", loser)
print("Marks:", c)


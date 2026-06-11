words = ['apple','ant','banana','bat','cherry','cat']
grouped={}

for word in words :
    key = word[0]

    grouped.setdefault(key, []).append(word)
print(grouped)


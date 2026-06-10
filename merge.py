list1=[4,1,5,7]

list2= [4,3,6,8]
new = []
i = 0
j = 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        new.append(list1[i])
        i += 1
    else:
        new.append(list2[j])
        j += 1
while i < len(list1):
    new.append(list1[i])
    i += 1
while j < len(list2):
    new.append(list2[j])
    j += 1

print(new)
            
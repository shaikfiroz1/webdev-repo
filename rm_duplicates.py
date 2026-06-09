nums = [1,2,3,4,5,6,7,2,2,3]

s=set()

for number in nums :
    if number  not in s :
        s.add(number)

print(s)



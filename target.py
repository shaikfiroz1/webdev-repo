nums = [1,2,3,4,5,6,7]
 
target =13
list =[]

for first in range (len(nums)) :
   
    for second in range (first+1, len(nums) ):
        
        if first + second == target :
         list.append((first,second))

print (list)


nums1 = [1,2,3,4,5,6,7]
target1 = 13
pairs = []
for i in range(len(nums1)):
    for j in range(i+1, len(nums1)):
        if nums[i] + nums[j] == target1:
            pairs.append((nums[i], nums[j]))
print(pairs) 
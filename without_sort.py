nums = [45, 45, 5, 47, 3]

first = second = float('-inf')

for number in nums:
    if number > first:
        second = first
        first = number
    elif number > second and number != first:
        second = number

print(second)  # 45
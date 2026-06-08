def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    print (mid)

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)


arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 1,  0, len(arr)-1))  

d = {}

d[(1,2)] = "tuple key"

print(d)
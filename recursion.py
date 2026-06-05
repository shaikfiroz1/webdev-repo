def recursive(lst):
    new_list = []
    for ele in lst:
        if isinstance(ele, list):    # ele list aa?
            new_list.extend(recursive(ele))  # recursion result add cheyyi
        else:
            new_list.append(ele)     # normal element append cheyyi
    return new_list

print(recursive([1, [2, [3, [4]]], 5]))  # [1, 2, 3, 4, 5]
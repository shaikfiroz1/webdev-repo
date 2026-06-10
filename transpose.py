# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transposed = [list(row) for row in zip(*matrix)]
# for row in transposed:
#     print(row)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new = []

for j in range(len(matrix[0])): 
   
    temp = []
    for i in range(len(matrix)): 
        temp.append(matrix[i][j])
    new.append(temp)

print(new)
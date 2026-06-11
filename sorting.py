marks = {'Raju': 85, 'Firoz': 90, 'Sita': 78, 'Kiran': 95}

new = {}

while marks:
    c = 0
    max_key = None

    for k, v in marks.items():
        if v > c:
            c = v
            max_key = k

    new[max_key] = c
    del marks[max_key]


print(new)
# marks = {'Raju': 85, 'Firoz': 90, 'Sita': 78, 'Kiran': 95}

# new = {}

# for i in range(len(marks)):
#     c = -1
#     max_key = None

#     for k, v in marks.items():
#         if v > c:
#             c = v
#             max_key = k

#     new[max_key] = c
#     del marks[max_key]

# print(new)
students = [('Raju', 85), ('Firoz', 90), ('Sita', 78), ('Kiran', 95)]



for i in range (len(students)):
    for j in range (i+1,len(students)):
        if students[i][1] < students[j][1]:
            students[i] , students[j] = students[j], students[i]

print(students)


 
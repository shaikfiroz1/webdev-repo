class Student :
    

    def __init__(self):

        self.__marks = 80 

    def get_marks(self):

       return self.__marks
    
    def set_marks(self , marks):

        if marks >=0 and  marks <=100 :
            self.__marks = marks 
        else : 
            print ("invalid marks")


student = Student()


print(student.get_marks())

student.set_marks(95)

print(student.get_marks())

student.set_marks(120)

     


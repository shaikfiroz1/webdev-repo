class Employee: 
    
    def work (self) :
        print ("Employee is working")

class softwareEngineer(Employee):

    def work (self):
        print("Writing Python code")

class DataScientist(Employee):
    
    def work(self):
        print("Building Machine Learning models")


Employees = [softwareEngineer(), DataScientist() ]


for worker in Employees:
    worker.work()
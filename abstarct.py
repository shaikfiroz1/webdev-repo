
from abc import ABC , abstractmethod

class Vehicle(ABC) :
    @abstractmethod
    def start_engine(self, engine ):

        self.engine = engine 


class Car(Vehicle) :

    def start_engine(self):
        print ("Car engine started")


car = Car()

car.start_engine() 

    
    
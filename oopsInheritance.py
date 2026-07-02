class vehicle :

    def __init__(self, brand):
        self.brand = brand

    def start_engine(self) :
            print ("engine started")



class car(vehicle) :
    pass



kar  = car("toyota")

print (kar.brand)

kar.start_engine()

    
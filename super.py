class Animal :
    
    def eat(self):
        print ("Animal is eating")


class dog(Animal):

    def eat(self):
        super().eat()
        print("Dog is chewing a bone")


tommy = dog()

print (tommy.eat())

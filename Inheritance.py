#Miras/Inheritance

class Animal:
    def __init__(self):
        print("animal is created")
        
    def toString(self):
        print("animal")
        
    
    def walk(self):
        print("animal walk")

#child class

class Monkey(Animal):#Monkey classı Animal classının child ı
    def __init__(self):
        super().__init__()#Artık parent clasının initalize nı kullanabilirim
        print("monkey is created")

    def toString(self):
        print("monkey")

    def climb(self):
        print("monkey can climb")


class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")
        
    def fly(self):
        print("bird can fly")        
        
       
m1=Monkey()
m1.toString()
m1.walk()
m1.climb()

print("------")

b1=Bird()
b1.walk()
b1.fly()



            
            
        
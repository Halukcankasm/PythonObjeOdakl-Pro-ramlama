from abc import ABC,abstractmethod
#abc = abstrackclases

#Abstrack sınıfın 1.Kuralı:Hiçbir şekilde obje oluşturulamaz(no instance)
#Bunun için bir build in modül kllanacağız
#Python bunun için herhangi bir altyapı sağlamıyor
#from abc import ABC,abstractmethod , import etmemiz gerekiyor

#2.Koşul inheretins edilen sınıfta abstrack sınıftaki metodlar kullanılmak
#-zorunda
#Yani chil classta mplement etmek zorundayız

class Animal(ABC): #super class
    @abstractmethod
    def walk(self):pass
    
    @abstractmethod
    def run(self):pass

class Bird(Animal): #sub class
    
    def __init__(self):
        print("bird")
    

    def walk(self):
        print("walk")
    
    
    def run(self):
        print("run")
    
b1=Bird()
b1.walk()
b1.run()


        




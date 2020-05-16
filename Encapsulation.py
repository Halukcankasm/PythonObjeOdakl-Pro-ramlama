#Encapsulation , method veya varaible kısıtlamak anlamına gelir

class BankAccount(object):
    
    def __init__(self,name,money,address):
        self.name=name  #global varaible 
        self.__money=money #private variable 
        self.address=address
        
        #Eğer dışarıdan erişimi istemiyorsak bu değişkenler private olmalı
        
        #Bunlar private olduğunda -
        #-erişim için (modify) için get ve set 
        
   
    #get ve set global method
    def getMoney(self):
        return self.__money 

    def setMoney(self,amount):
        self.__money=amount
        
        
    def __increase(self): #private method
        self.__money = self.__money + 500 
#private method yani ben bunu sadece         
        
        
        
p1 = BankAccount("messi",1000,"barcelona")
p2 = BankAccount("neymar",2000,"paris")

       
print("get method:",p1.getMoney())

p1.setMoney(5000)
print("afet set method:",p1.getMoney())

#p1.__increase(self);
#print("after raise",p1.getMoney)



#Çok şekillilik,biçimlilik

class Employee:
    
    def raisee(self):
        raiseRate=0.1
        result = 1000 + 100*raiseRate
        print(result)
        
        
class CompEng(Employee):

    def raisee(self):
        raiseRate=0.2
        result = 1000 + 100*raiseRate
        print(result)
        
        
class EEE(Employee):

    def raisee(self):
        raiseRate=0.3
        result= 1000+ 100*raiseRate
        print(result)
    
    
e1=Employee()

c1=CompEng()

eee1=EEE()


employee_list = [c1,eee1]

for employee in employee_list:
    employee.raisee()
    
    
    
    


    
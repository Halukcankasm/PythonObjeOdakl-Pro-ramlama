# %% Calculator project

class Calc(object):
    
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def add(self):
        "addition num1+num2 = result -> return result"
        result=self.num1+self.num2
        return result
    
    def subtraction(self):
        "addition num1-num2 = result -> return result"
        result=self.num1-self.num2
        return result
    
    def multiplication(self):
        "addition num1*num2 = result -> return result"
        result=self.num1*self.num2
        return result
    
    def division(self):
        "addition num1 / num2 = result -> return result"
        result=self.num1/self.num2
        return result
    
    
print("Choose add(1), multply(2),subraction(3),devision(4)")
selection = input("select (1) or (2) or (3) or (4)")

v1 = int(input("First value"))
v2 = int(input("Second value"))
    
a=Calc(v1,v2)

if selection == "1":
    addResult=a.add()
    print("Result:",addResult)

if selection == "2":
    multiplyResult=a.multiplication()
    print("Result:",multiplyResult)
    
if selection == '3':
    subResult=a.subtraction()
    print("Result:",subResult)
    
if selection == '4':
    deivisionResult=a.division()
    print("Result:",deivisionResult) 
    
    





 
   
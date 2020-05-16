class Website:
    
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        
    def loginInfo(self):
        print(self.name + " " + self.surname)        
        
        
class Website1(Website):
    "child"
    def __init__(self,name,surname,id):
        #Parent classın değişkenlerinide almam gerekiyor
        Website.__init__(self,name,surname)
        self.id=id
        
    def login(self):
        print(self.name+" "+self.surname+" "+self.id)
                
        
class Website2(Website):
    "child"
    def __init__(self,name,surname,email):
        Website.__init__(self,name,surname)
        self.email=email
        
    def login(self):
        print(self.name+" "+self.surname+" "+self.email)      
        

p1=Website("Recep Tayyip","Erdoğan")
p1.loginInfo()

p2=Website1("Ali","Şen","123")
p2.login()
p2.loginInfo()

p3=Website2("Emre","Biçen","Emrebicen@gmail.com")
p3.login()
p3.loginInfo()





        
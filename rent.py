import datetime

class VehicleRent:  
    
    def __int__(self,stock):
        self.stock=stock
        self.now = 0 #kaç saatlik kiraladık


    def displayStock(self): #Stokta bulunan kaç araç var
        print("{} vehicle available to rent".format(self.stock))
        return self.stock #kaç tane araç olup olmadığını nuradan anlayacağız

    def rentHourly(self, n): 
        if n <=0:
            print("number should bo pozitife")
            return None
        elif n > self.stock:
            print("Sorry {} vehicle avaible to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours"
                  .format(n,self.now.hour))
            self.stock -= n
            
            return self.now

    def rentDaily(self,n): 
        if n <=0:
            print("number should bo pozitife")
            return None
        elif n > self.stock:
            print("Sorry {} vehicle avaible to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for daily at {} hour"
                  .format(n,self.now.hour))
            self.stock -= n
            
            return self.now

    def returnVehicle(self,request,brand):#aracı geri getirdi
        car_h_price=10 #Saatlik 10$
        car_d_price=car_h_price*24 #Günlük 240$
        
        bike_h_price=5 #Saatlik 5$
        bike_d_price=bike_h_price*24 #Günlüh 240$
        
        rentalTime , rentalBasis, numOfVehicle = request
        bill = 0
        
        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                
                if rentalBasis == 1:# hourly
                    bill = rentalPeriod.second/3600*car_h_price*numOfVehicle
                    
                elif rentalBasis == 2:#daily
                    bill = rentalPeriod.second/(3600*24)*car_d_price*numOfVehicle
                    
                if(numOfVehicle >= 2):
                    print("You have extra 20% discount")
                    bill=bill*0.8
                
                print("Thank you for returing your car")
                print("Price: $ {}".format(bill))
                return bill
            
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                
                if rentalBasis == 1:# hourly
                    bill = rentalPeriod.second/3600*bike_h_price*numOfVehicle
                    
                elif rentalBasis == 2:
                    bill = rentalPeriod.second/(3600*24)*bike_d_price*numOfVehicle
                    
                if(numOfVehicle >= 4):
                    print("You have extra 20% discount")
                    bill=bill*0.8
                
                print("Thank you for returing your bike")
                print("Price: $ {}".format(bill))
                return bill

        else:
            print("Your do not rent a bike")
            return None
                                
                    
                    
class carRent(VehicleRent):
    
    global discount_rate
    discount_rate = 15
    
    def __init__(self, stock):
        super().__init__(stock)

    def discount(self,b):
        bill = b -(b*discount_rate)/100
        return bill


class BikeRent(VehicleRent):
    
    def __init__(self, stock):
        super().__init__(stock)
    

class Customer:

    def __init__(self):
        self.bikes=0
        self.rentalBasis_b=0
        self.rentalTime_b=0
        
        self.cars=0
        self.rentalBasis_c=0
        self.rantalTime_c=0

    
    def requestVehicler(self,brand):
        if brand == "bike":
            bikes = input("How many bikes would you like to rent")
            
            try:
                bikes=int(bikes)
            except ValueError:
                    print("Number should be Number")
                    return -1
        
            if bikes < 1:
                print("Number of Bikes should be greater than zero")
                return -1
            else:
                self.bikes = bikes
                return self.bikes    
        
    
    
    
        if brand == "car":
            cars = input("How many cars would you like to rent")
            
            try:
                cars=int(cars)
            except ValueError:
                print("Number should be Number")
                return -1
            
            if bikes < 1:
                print("Number of Bikes should be greater than zero")
                return -1
            else:
                self.cars = cars
            return self.cars 

    def returnVehicle(self,brand):
        
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b , self.rentalBasis_b , self.bikes
            else:
                return 0,0,0
                
            
        elif brand =="car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c,  self.cars
            else:
                return 0,0,0
            
            
            
        else:
            print("Return vehicle Eror")
            
        
        
        
        
        
        
        

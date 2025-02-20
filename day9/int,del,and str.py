#int del and str in python 
#constructor
'''
class car:
    def __init__(self,noofwheels,mileage,airbags):  #constructor
        print("this is a constructor!")
        self.noofwheels=noofwheels   #member variables 
        self.mileage=mileage
        self.airbags=airbags

    def moveforward(self):                #member methods
        print('car is moving:')

    def movebackward(self):                 #self keyword or pointor can be used to point the object's values inside the class 
        print('car is moving backward')


car1 =car(2,45,2)

print(car1.mileage,car1.noofwheels,car1.airbags)


car2 =car(56,56,34)

print(car2.mileage,car2.noofwheels,car2.airbags)




#Destructor
class car:
    def __init__(self,carname,noofwheels,mileage,airbags):
        print("this is a constructor!")
        self.noofwheels=noofwheels   #member variables 
        self.mileage=mileage
        self.airbags=airbags
        self.carname=carname
    def __del__(self):
        print("this is a destructor!")      # object use pannathapothu destructor call agum


    def __str__(self):                                      #this returns only  string  
        print("this is an variable string value assigner with the self keyword")
        return(self.carname)
        

    def moveforward(self):                #member methods
        print('car is moving:')

    def movebackward(self):                 #self keyword or pointor can be used to point the object's values inside the class 
        print('car is moving backward')


car1 =car("BMW",2,45,2)
print(car1mmileage,car1.noofwheels,car1.airbags,car1.carname)



car2 =car("MT",56,56,34)
print(car2.mileage,car2.noofwheels,car2.airbags)
'''




#quiz
class bankaccount:
    def __init__(self,customername,balance,accountnumber):
        self.customername=customername
        self.balance=balance
        self.accountnumber=accountnumber

    def __str__(self):
        return(self.customername)

    def check(self):
        print("the name of the customer:",self.customername)


acc=bankaccount("kastro",90000,3243241435)
print(acc)
print(acc.customername,acc.balance,acc.accountnumber)
acc.check()













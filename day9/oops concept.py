#oops concept     Abstraction, Encapsulation, Inheritance, and Polymorphism are the four pillars of object-oriented programming
'''
#car
noofwheels=4
mileage =90
airbags= 5
'

def moveforward():
    print("car is moving backward")

class car:
    noofwheels=3   #member variables 
    mileage=0.0
    airbags=0

    def moveforward(self):                #member methods
        print('car is moving:')

    def movebackward(self):
        print('car is moving backward')

car1 =car()  #instance creation (use the class or creating a copy or instantiation
print(car1.noofwheels)
print(car1.mileage)

                            #acessing variables of the class
car2=car()
car2.mileage=25.4
print(car2.mileage)



car1.moveforward()
'''


#quiz

class bank:
    customername=''
    balance=0
    account_no=0

    def account():
        print('hi your account created successfully')


acc = bank()
acc.balance=5
acc.customername='kastro'
acc.account_no=57398473897
print(acc.customername)
print(acc.balance)
print(acc.account_no)









    

        
    
#oops concept

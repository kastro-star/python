#inheritance
#Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class). This promotes code reuse, modularity, and a hierarchical class structure. In this article, well explore inheritance in Python.



'''
#single inheritance
class vehicle:   #parent class
    noofwheels=4

    def moveforward(self):
        print("vehicle is moving forward!")


class car(vehicle): #child class or sub class  inherit all properties and behaviour from the parentclass   #class car inherit the class vehicle (all the variables and methods are acessed by the class car
    noofairbags=5


carkas = car()

print(carkas.noofairbags)
print(carkas.noofwheels)  #it takes the noofwheels from the class vehicle
carkas.moveforward()







#hierarchical inheritance 


class vehicle:   #parent class
    noofwheels=4

    def moveforward(self):
        print("vehicle is moving forward!")


class car(vehicle): #child class or sub class  inherit all properties and behaviour from the parentclass   #class car inherit the class vehicle (all the variables and methods are acessed by the class car
    noofairbags=5


class bike(vehicle):         
    mileage=56.0
    

carkas = car()

print(carkas.noofairbags)
print(carkas.noofwheels)  #it takes the noofwheels from the class vehicle
carkas.moveforward()


'''




#multilevel inheritance



class vehicle:   #parent class
    noofwheels=4

    def moveforward(self):
        print("vehicle is moving forward!")


class car(vehicle):                               #its called multiple inheritance 
    noofairbags=5


class maruthi(car):         
    mileage=56.0


class toyoto(car):
    mileage=60

class toyothi(maruthi,toyoto):  #there are two parents single child class is called diamond problem
    has_touchscreen = True

car2=toyothi()
print(car2.noofwheels)
print(car2.noofairbags)
print(car2.mileage)
car2.moveforward()
    

'''
car1 = maruthi()
print(car1.noofwheels)
print(car1.noofairbags)
print(car1.mileage)
car1.moveforward()



#multiple inheritance


class father:
    haircolor='white'

class mother:
    eye="blue"
    haircolor="black"

class child(father,mother): #mention the class in priority wise
    age=23

child23 = child()
print(child23.age)
print(child23.eye)
print(child23.haircolor)  #take the value from the first mentioned class values
    

'''








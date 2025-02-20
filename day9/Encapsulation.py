#encapsulation In Python, encapsulation is the process of bundling data and methods into a class, while restricting access to some parts. It's a fundamental concept of object-oriented programming. 
class car:
    def __init__(self,carname,noofwheels,mileage,airbags):
        print("this is a constructor!")
        self.__noofwheels=noofwheels    #__(undescore two times infront of variables make the variables private  it can be accessed only inside of the class
        self.mileage=mileage
        self.airbags=airbags #member variables
        self.carname=carname
    def __del__(self):
        print("this is a destructor!")    


    def __str__(self):                                      #this returns only  string  
        print("this is an variable string value assigner with the self keyword")
        return(self.carname)
        

    def moveforward(self):                #member methods
        print('car is moving:')

    def movebackward(self):                 #self keyword or pointor can be used to point the object's values inside the class 
        print('car is moving backward')
    #private variable can be acessed by the outside objects(It means GETTER)
    def getter(self):
        print("no of variables:",self.__noofwheels)    #GETTER AND SETTER ARE IMPORTANT IN ENCAPSULATION


    #outside variable passed into the function(it means SETTER)
    def setter(self,wheel2):        #the value 0f argument 9 passed into the wheel2 and replaced the private variable __noofwheels = wheel2(value9)
        self.__noofwheels = wheel2
        print("noofwheelsinsette:",self.__noofwheels)

car1 = car("bmw",4,45,3)

print(car1)
print(car1.carname,car1.airbags,car1.mileage,car1.getter())



car1.getter()
car1.setter(9)
car1.getter()


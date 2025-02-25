#polymorphism  Polymorphism in Python is the ability of a function, method, or operator to work with multiple types of objects
'''

#Method overloading compile time polymorpism(is simly not possible in python but possible)

class car:

    
    //method overloading - compile time polymorpism
    int sum(int a,int b):
        return a+b

     int sum(inta,int b, int c):  #its other languages using method overloading 
         return a+b+c
     sum(1,2)
     sum(1,2,3)
     sum(1.0,4.0)
     
    
    def sum(self ,a,b,c=0):   #inpython method overloading slightly not possibele but default argument  
      return a+b+c

    def sum1(self ,*args):  #*args store the multiple values store as like tuples 
         ans = 0
         for i in args:
             ans +=i
         return ans


car1 = car()
print(car1.sum1(4,3,43,4,3,432,))
'''

#method overriding --runtime polymorpism


class father:
    def __init__(self):
        print("father construtor")
    def sayhello():
        print("hii father")
        
class child(father):
    def __init__(self):
        print("child constructor")
    def sayhello(name):
        print("hii child",name)




kas = child()   #over ridding the father class as print only child class
child.sayhello("gfgff")

kast = father()
father.sayhello()
























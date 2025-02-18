#scope of variable
'''

def add():       
    a=2         #inside of the function variables are accessed only inside 
    b=12
    print(a+b)


a=4
b=4        #but functions can acess the outside variable values
print(a+b)
add()
'''


def add():
    global a
    a=a+5
    
    
    print(a+b)


a=4
b=4        
print(a+b)
add()

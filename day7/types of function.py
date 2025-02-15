#types of functions
#two types of functions void function and non void function


#example for void function
'''
def add():
    a=int(input())
    b=int(input())
    c=int(input())
    print(a+b)

sum= add()
print(sum) # this is void function didn't return anything



#example for Non void function
def add():
    a=int(input())
    b=int(input())
    c=int(input())
    return a+b    # Return keyword is important to pass the calculted values to the #(def add()) and return the values anywhere.


sum= add()
print(sum)



#function pass an srguments

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b


a=int(input())
b=int(input())

sum0=add(a,b)
sub1=sub(a,b)
mul2=mul(a,b)
print(sum0,sub1,mul2)

'''

def area_of_rectangle(length,breadth):
    area = length*breadth
    print('hiii hello')
    if area == 15:
        print('sucess')
    else:
         
         print('ada pongada')
    return area

length=int(input())
breadth=int(input())

rectangle = area_of_rectangle(length,breadth)
print(rectangle)          









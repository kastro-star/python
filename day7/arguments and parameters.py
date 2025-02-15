#arguments and parameters

'''
def area_of_rectangle(length,breadth): #length and breadth are the parameters
    area = length*breadth
    print('hiii hello')
    return area

length=int(input())
breadth=int(input())

rectangle = area_of_rectangle(length,breadth)  #call pannumpothu input ahh kodukura actual values are called arguments
print(rectangle)



keyword argument
default argument
positional arguments



#positional arguments funtion calling arguments and parameters are in same order
def area_of_rectangle(length,breadth): #length and breadth are the parameters
    area = length*breadth
    print('hiii hello')
    return area

len=int(input())
br=int(input())

rectangle = area_of_rectangle(len,br)  #call pannumpothu input ahh kodukura actual values are called arguments
print(rectangle)


#keywords arguments

def area_of_rectangle(length,breadth,a,b): #length and breadth are the parameters
    area = length*breadth
    print('hiii hello')
    return area

len=int(input())
br=int(input())

rectangle = area_of_rectangle(breadth=br,length=len,a=5,b=6)  #call pannumpothu input ahh kodukura actual values are called arguments
print(rectangle)



#default argument   if an argument fails to pass the value arguments contains some specified values they use them supppose arguments passes the values execute the aruguments value
def area_of_rectangle(length,breadth=5): #length and breadth are the parameters
    area = length*breadth
    print('hiii hello')         #default arguments are declared at last of them
    return area

len=int(input())


rectangle = area_of_rectangle(len,1)  #call pannumpothu input ahh kodukura actual values are called arguments
print(rectangle)
'''

#positional arguments is first otherwise all are next of them
#if otherwise use the different parameters separately

def great(name,message="hello"):
    """hnnkjervrehvbhrev"""
    print(message,name+"!")
great('python')    



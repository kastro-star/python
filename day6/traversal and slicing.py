#traversal   element by element print all the elements in the list or tuples is called tuples
fruit = ("appple","fruit","mango","frfrf","3frf")


#method 1
for i in range(len(fruit)):
    print(fruit[i])


#method 2
for i in fruit:
    print(i)
    


#slicing are appplicable for string,list ,tuples
string = "rnkntrtpkhh"
print(string[0:9:2])

#slice hte list
print(fruit[0:5:2])

             
#reverse slicing 
string = "kastro"
print(string[::-1]) #::-1 it will prints all the values as reverse 


#Quiz
num=[2,5,1,8,4]
print(num[1:4])

num[2:4]=[3,7]
print(num)

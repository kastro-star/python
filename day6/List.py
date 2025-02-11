# Lists in python

#height_list=[176,186,199]
#print(height_list)  #list is an comma separated collection of value enclosed withan square brackets


'''
height_list=[176,186,199 ,hii]  #list are used to store multiple kind of datatype
print(height_list)                  #list values are accesed with their index values

height_list=[176,186,199,
             'hii']
print(height_list[0])
'''


lst1=[1,2,3]
lst2=[4,5,6]    #len keyword is used find the length of the list
lst3=lst1+lst2

print(len(lst3))



lst1=[1,2,3]
lst2=[4,5,6] 
lst3=lst1+lst2
#length of the list
print(len(lst3))

#inserting an element into the list append is store the value in the last of the list
lst1.append(4)
print(lst1)


#extend keyword  is used to add the two list like add
lst1.extend(lst2)
print(lst1)

lst1=[1,2,3]
lst2=[4,5,6]
lst1.insert(0,5)
print(lst1)

#to store the values of the list into the another list
lst1.append(lst2) #that lst1 appends the lst2 as an single value but stores the full list 
print(lst1)


#count the no of elements
print(lst1.count(4)) #find no of 4 values in the list

#find the index number the value was placed
print(lst1.index(5))      #first occured node will be displayed  

#clear keyword is used to clear the whole list
lst1.clear()
print(lst1)




#list part 2

lst1=[1,2,3]
lst2=[4,5,6]


#to find the min and max element in the list

print(min(lst1))
print(max(lst2))


#arrang the elements in the list
lst2.extend(lst1)
print("before sorting",lst2)
lst2.sort()
print("after sorting",lst2)


#reversly arrange the elements in the list
lst2.extend(lst1)     #extend is used to add the total list into the another list 
print("before sorting:",lst2)
lst2.sort(reverse=True)
print("after sorting:",lst2)


#to add all the elements in the list
print(sum(lst2))

#insert the new element into your chosed index place
lst1.insert(0,1000)
print(lst1)

#mutabillty is also same as the insert (but it replaces the value and takes the place)
lst1[0] = 156
print(lst1)  #if i updated the specific value is called as mutability


#pop()function is used to remove the element in tthe list
lst1.pop(2)  #tell the index number to them to remove the value in the list
print(lst1)           #if you don't mention any index ,it atomatically remove the last element


#remove
lst1.remove(3)
print(lst1)


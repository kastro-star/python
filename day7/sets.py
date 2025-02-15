#unordered , all types of datatypes ,duplcates cannot be allowed

set1= {1,2,3,4,1}
print(type(set1))

set1= {1,2,3,4,1}
print (set1)

#add the element
set1.add(6)
print(set1)

#remove the element
set1.remove(6)
print(set1)


#clear all the element
set1.clear()
print(set1)

#chnage the list into set
lst=[1,2,34,4,45,]
set2=set(lst)
print(type(lst))


#sets
set1 ={1,2,3,4}
set2={4,5,6,7,8}

#print
print(set1.union(set2))  #sekurathu
print(set1.intersection(set2))  #common
print(set1.difference(set2))



#traversse
for i in set1:
    print(i)

print(1 in set1)    # to find the value is present in the traverse

set1= {1,2,3,4}
set2 ={4,5}
set3={2,3,4,5,6,7,8}
print(set1.union(set2).intersection(set3))



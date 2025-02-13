#tuples
#Tuples are unmutable is values in tuples are unchangeable
#otherwise list-elements are changeable,update but tuples are not possible
#in tuples a=(98,) if used assign value to tuple without (,) it takes as an integer
tup = (32,39)
print(tup)
print(tup[0])  #accessing of the tup is also same in tuples

'''
#len
print(len(tup))

#min and max
print(min(tup),max(tup))

#count
print(tup.count(100))  #give the value and search how many no of elements present in them


#sorting is not availale


#find the index value
print(tup.index(39))

print(tup(10))  #it will produce the value error because it produce the value error


important changing list into tuple
and tuple into list

                    #tuple can be changed into list
lst = list(tup)
print(lst)

tup1 = tuple(lst)   #list can be changed into tuples
print(type(tup1))
'''
tup = tup+("78",) # or tup+ = ("987",)   
print(tup)

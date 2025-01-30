#a="sivaz"
#b="siva"


#ascii values use the keyword ord
#print(ord('z'))
#print(a<b)



#learn augumented assignment operator

#a = 2
#a = a+3  # this is also same a+=2
#a= a*2
#print(a)


name ,balance ="siva",500.0
#balance += (7/100 * balance)
a = balance
c = (7/100 * a )
a +=c
print(a)

name ,balance ="siva",500.0
balance += (7/100 * balance)  # follow this
print (balance)


name ,balance ="siva",500.0
c= (7/100 * balance)
b = balance +c
print (b)

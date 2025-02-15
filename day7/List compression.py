#list comprehension
'''
arr=[1,2,3,4,5,6]

odd =[]
# normal
for i in arr:
    if i %2==1:
        odd.append(i)
print(odd)


#list comprehension (simplify the lines)
odd =[i for i in arr if i%2==1]
print(odd)


#in normal fil up the lst variable from 1to 100
lst=[]
for i in range(1,101):
    lst.append(i)
print(lst)
'''

lst =[u for u in range(1,101)]
print(lst)


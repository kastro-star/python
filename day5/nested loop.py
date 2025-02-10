#nested loops
'''
1
12
123
1234
'''

n = int (input())

for j in range(1,n+1):   #that take care of the coloumns
    for i in range(1,j+1):  #that take care of rows
        print(i, end="")
    print()    #make an space between the numbers

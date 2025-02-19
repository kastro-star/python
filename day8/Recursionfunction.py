#Recursion Function
#a function that callhim itself again  is called recursion
'''
def add(n):
    print(n)
    return add(n-1)
ans = add(5)



def sum_of_n(n):
    #base case  if recurtion case not implemented for the user's input
    if (n==1):
        return 1
    #recursive case     #for use like for loop while loop
    return n + sum_of_n(n-1)

sum = sum_of_n(5)

print(sum)


'''

def factorial(n):
    if n==0:
        return 1

    else:
       
        
        return n* factorial(n-1)
'''        
result = factorial(5)
print(result)
'''
#nested if else

age =int(input())
eat_pizza = True
exercise = True

if (age<30) :
    if eat_pizza:
        print("its unhealthy")
    else:
        print("fit")
else:
    if exercise:
        print('fit')
    else:
        print('unhealthy')
        

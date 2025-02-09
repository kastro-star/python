#ternary operator

age = int(input())
eat_pizza = False
exercise = False



print(("unfit" if eat_pizza else "fit") if age<30 else ("fit" if exercise else "unfit"))  #if execution task is first then tell the if condition next else first and their task is next
                                    #if condition start

    #nested if left side task right side condition for --IF
    #left side condition right side tasks





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
        

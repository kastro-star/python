age =25
income=25000



if age<18:
    message ="you are to toung to work "
elif age>=18 and age<=25:
    if income >=30000:
        message ="you are elligible to work "
    else:
        message="you are eligible for regular discount"
else:
    message = "you are eligible for reguler discount"
        
print(message)
#find the number is odd or even
num = int(input())

if(num %2 ==0):
    print("even number")
else:
    print("odd number")

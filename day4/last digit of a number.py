#last digit of a nuumber eg 227-7  17-7
#unit digit
#num =(input())
#print(num[-3])   #start value of the index value start with 0 thn last word of the string index start with-1
                  #forward indexin 0123
                  #backword indexing -1 -2 -3 -4

#orginal unit digit finder
#num = int(input())
#print(num%10)    #use this %10 to find the unit digit


#task
num = int(input())
num //= 100
print (num%10)

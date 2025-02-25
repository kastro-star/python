
'''
file = open("info.txt","r")  #path has two types 1.relative path 2.absolute path 1.relative path is the path of the file relative to the current working directory 2.absolute path is the full path of the file from the root directory
#print(file.read())        #for reading the file  it is an content path

#file.readline() is used to read the file and return a single line
print(file.readline())
file.close()


 #is used to read the file and return a list of lines
print(file.readlines())
file.close()

file = open("info.txt","w") #write mode delete the content and write the file
file.write("kastro")
file.close()
file = open("info.txt","r")
print(file.read())


# file = open("info.txt","a") #append mode with out deleting the content to append the file
# file.write("b.tech it")
# file.close()
# file = open("info.txt","r")
# print(file.read())

# file = open("info.txt","w")
# list = ["kastro","b.tech it","kastro","b.tech it","ednefe"]
# print(file.writelines(list))

print(file.read())



file = open("info2.txt","a")
file.write("kastro")
file.close()
                                 #file.close() is compulsory for saving the file
'''
with open("info.txt","r") as file:
    print(file.read())












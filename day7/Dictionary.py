#Dictionary are created inside {},unordered key paired of values , index values are not used

map ={1:'one',2:'two',}  #1-it is an key and their value is one and did'nt mention the key value another time
print(type(map))

print(map[2])  #for accessing the value use the key


map ={'1':['one',(21323,223),"dwewe"],2:'two',}
print((map))


#uses get function
print(map.get(1))

#length
print(len(map))

#keys
print(map.keys()) #print all the keys

#values
print(map.values()) #print all the values in the map variable


#items
print(map.items())  #get the different values as list


#insert the values in the dictionary
map[1]='four'
print(map)

#remove  pop is used to delete the element
map.pop(2)
print(map)


#clear
map.clear()
print(map)


#Dict
map=dict()
print()


#quiz
map ={5:{'p':{5:"p"},6:"q"},7:"r",'q':'s','s':'t'}
print(map[map[map[5][6]]])


'''explain (map[map[map[5][6]== q]])
            (map[map[q]])
            map[q]=t
            
'''

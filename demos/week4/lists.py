#create empty list
red = []

#Declare a non-empty list
amber = ["Poland", "Portugal", "Romania", "Fiji", "Amber"]

#printing full list
print (amber)

#print a single element
print(amber[0])

#Add element to the end of a list
red.append("Brazil")
red.append("Somalia")
red.append("Malta")

# for i in range (3):
#   red.append(input("Enter new red list country: "))

#insert data onto a list not at the end
red.insert(1, "Ghana")
red.insert(3, "Switzerland")


#remove an item for the list by Name

# red.remove("Somalia")
# red.remove(input("Which country to remove? "))

#remove an item from list by Index and moving it to a diferent list
# red.pop(0)
# print(red)
# new_amber_country = red.pop(1)
# amber.append(new_amber_country)
# red.pop(1)

#delete an item 
del red[1]

#sliccing
print("---Slicing---")
print(amber[2:4])
print(amber[::2])
#[start,stop,step]

#miroslav (reversing list)
a = [1, 2, 3]
print(a[::-1])

#strings are list !!!!!!!

b ="Python is lovely"
print(b[::-1])
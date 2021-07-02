# demonstrating the counter function
x = int(input("Please enter the first whole number:\n"))
y = int(input("Please enter the second whole number:\n"))
z = int(input("Please enter the third whole number:\n"))
odd = 0
even = 0
if (x%2) == 0:
  even +=1
else:
  odd +=1
if (y%2) == 0:
  even +=1
else:
  odd +=1
if (z%2) == 0:
  even +=1
else:
  odd +=1
print("\nThere were {} even".format(even) +" and {} odd numbers.".format(odd))
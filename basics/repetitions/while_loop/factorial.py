#calculating the factorial of user input in a while loop
print("Please anter a number") 
x = int(input())
print("\n")
counter = 1
y = 1
while counter <= x:
  y = y * counter
  counter +=1
print("\nThe factorial is {}.".format(y))
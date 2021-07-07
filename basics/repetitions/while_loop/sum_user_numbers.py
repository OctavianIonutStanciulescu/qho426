#calculating multiple user inputs in a while loop
print("How many numbers should I sum up?") 
x = int(input())
print("\n")
counter = 1
y = 0
while counter <= x:
 print ("Please enter number {} of {}" .format (counter, x))
 z= int(input())
 counter +=1
 y += z
print("\nThe answer is {}.".format(y))
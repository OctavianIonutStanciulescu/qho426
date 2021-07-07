#using sum while in a loop
print("How many numbers should I sum up?") 
x = int(input())



counter = 1
y = 0
while counter < x:
 print ("Please enter number {} of {}" .format (counter, x))
 input()
 counter +=1
print("The answer is ")
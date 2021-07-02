#using count while in a loop
print("How many live cables must I avoid?\n") 
lc = int(input())
counter = 0
while counter < lc:
  counter +=1
  print ("Avoiding...Done! {} live cables avoided!" .format(counter))
print("\nAll live cables have been avoided.")
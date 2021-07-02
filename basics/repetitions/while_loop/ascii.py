#using counter to display ascii while in a loop
print("How many bars should be charged") 
bar = int(input())
counter = 0
D = (u"\u275A")
while counter < bar:
  counter +=1
  print ("Charging: "+ D*counter)
print("\nThe battery is fully charged.")
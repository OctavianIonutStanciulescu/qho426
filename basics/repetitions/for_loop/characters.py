#using the for function with user input
print("What strange markings do you see?") 
x = input()
print("\nIdentifying...")
for position in range(0, len(x), 1):
  print("index {}: ".format(position) + x[position])
print("\nDone!")

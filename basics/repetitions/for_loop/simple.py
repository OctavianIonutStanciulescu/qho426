#using the for function with user input
print("How many mountains should I display?") 
x = int(input())
print("\nDisplaying...")
for count in range(x):
  print("      __ ")
  print("     /  \_ ")
  print("    /^    \ ")
  print("   /  ^    \_ ")
  print(" _/ ^ ^     ^ \ ")
  print("/ ^      ^     \ ")
print("\nDone!")
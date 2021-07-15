#using the for function with user input
def run():
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
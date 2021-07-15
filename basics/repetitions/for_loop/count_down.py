#using the for function with user input
def run():
  print("How far are we from the cave?") 
  x = int(input())
  print("\n")
  for count in range(0, x):
    print(f"{x} steps remaining")
    x -=1
  print("\nWe have reached the cave!")
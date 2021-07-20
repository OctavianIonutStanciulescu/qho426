#populating a lists with user input

def directions():
  l = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return l

def menu():
  x = directions()
  print("Please enter a direction:")
  for i in range(len(x)):
    print("{}: {}.".format(i, x[i]))
  i = int(input())
  print()
  return (x[i])

def run():
  print("Working out escape route...\n")
  route = []
  for count in range (5):
    route.append(menu())    
  print(route)
run()
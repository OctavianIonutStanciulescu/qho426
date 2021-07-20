#using itteration with a simple lists

def directions():
  l = ["Move Forward", "Move Backward", "Turn Left", "Turn Right",]
  return l

def menu():
  x = directions()
  print("Please enter a direction:")
  y = 0  
  for index in range(len(x)):
    print("{}: {}.".format(index, x[y]))
    y+=1

def run():
  menu()
run()
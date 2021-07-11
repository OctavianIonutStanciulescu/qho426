def room_area(width, length):
  return width*length

def room_name():
  return input("What is the name of the room?\n")

def price(name, area):
  if name == "bathroom":
    return 20*area
  elif name == "bedroom":
    return 10*area
  elif name == "kitchen":
    return 5*area
  else:
    return 30*area
def run():
  name = room_name()
  w = float(input("what is the width of the room?"))
  l = float(input("what is the leght of the room?"))
  print ("To paint {} you need to pay ${:.2f}".format(name, price(name, room_area(w,l))))
run()
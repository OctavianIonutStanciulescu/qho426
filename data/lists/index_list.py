
def path():
  l = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return l

def run():
  print ("Moving...")
  x = path()
  print (x[0], "for", x[1], "steps")
  print (x[2], "for", x[3], "steps")
  print (x[4], "for", x[5], "steps")
  print (x[6], "for", x[7], "steps")

run()
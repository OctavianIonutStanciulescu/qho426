#the use of multiple nested statements
def run():
  print("Where shoud I look?") 
  look1 = input() 
  if (look1 == "in the bedroom"): 
    print("Where in the bedroom should I look?") 
    look2 = input() 
    if (look2 == "under the bed"): 
      print("Found some shoes but no battery!") 
    else:
      print("Found some mess but no battery!")
  elif (look1 == "in the bathroom"):
    print("Where in the bathroom should I look?") 
    look3 = input()
    if (look3 == "in the bathtub"):
      print("Found a rubber duck but no battery!") 
    else :
      print("Found a wet surface but no battery!") 
  elif (look1 == "in the lab"):
    print("Where in the lab should I look?")
    look4 = input()
    if(look4 == "on the table"):
      print("Yes! I found my battery!") 
    else:
      print("Found some tools but no battery!") 
  else:
    print("I do not know where that is but I will keep looking.")
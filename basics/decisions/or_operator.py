#using the logical or operator
def run():
  print("What type of adventure should I have?") 
  a1 = input() 
  if ((a1 == "scary") or (a1 == "short")): 
    print("\nEntering the dark forest") 
  elif ((a1 == "safe") or (a1 == "long")):
    print("\nTaking the safe route!") 
  else:
    print("\nNot sure which route to take!")
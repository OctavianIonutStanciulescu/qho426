# Different atribute settings
def run():
  print ("Please enter the number of lives:")
  h = (u"\u2764")
  L = int (input())
  print ("Please enter the energy level:")
  E = int (input())
  d = (u"\u2666")
  print ("Please enter the shield level:")
  S = int( input())
  c = (	u"\u272A")
  print ("Healh has been set!")
  print("\n ") 
  print ("Lives:  " + (h * L))
  print ("Energy: " + (E * d))
  print ("Shield: " + (S * c))

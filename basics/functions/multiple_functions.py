#use of multiple user defined functions
def display_ladder(steps): 
  a = 0
  while a < steps:
    a+=1
    print("| |")
    print("***") 
def create_ladder():
  print("How many steps remain?") 
  steps = int(input())
  display_ladder(steps) 
  print("| |")
create_ladder()
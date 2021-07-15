#using a simple function with a nest
def run():
  def identify(): 
    print("What do you see?")
    a = input( ) 
    if a == "a large boulder":
      print ("It`s time to run!")
    else:
      print("We will be fine.")  
  identify()
#using a user-defined function with a parameter
def run():
  def escape_by(plan): 
    print("What do you see?")
    if plan == "jumping over":
      print ("\nWe cannot escape that way! The boulder is too big!")
    elif plan == "running around":
      print ("\nWe cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper":
      print("\nThat might just work! Let's go deeper!")
    else:
      print("We cannot escape that way! The boulder is in the way!")  
  escape_by("jumping over") 
  escape_by("running around") 
  escape_by("going deeper")
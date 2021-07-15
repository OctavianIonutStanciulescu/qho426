#using a simple defined function
def run():
  def listen(): 
    print("What sound did I hear?")
    sound = input( ) 
    print("\nThat was a loud", sound)
  listen()
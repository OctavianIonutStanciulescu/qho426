#Combining the work i did so far
def run():
  print ("  #######")
  print ("  #  .  #")
  print ("  # --- #     Hello, I`m Beep, please choose my eyes so i can see you!")
  print ("  #######")
  print ("  ()%%%()")
  print (" () %%% ()")
  print ("()  %%%  ()")
  print ("    %%%")
  print ("    \_/")
  eye= input()
  print ("  #######")
  print ("  # " + eye + "." + eye + " #")
  print ("  # --- #   Thank you human! Now what is your name?")
  print ("  #######")
  print ("  ()%%%()")
  print (" () %%% ()")
  print ("()  %%%  ()")
  print ("    %%%")
  print ("    \_/")
  name= input()
  print ("  #######")
  print ("  # " + eye + "." + eye + " #")
  print ("  #\___/#   Nice to meet you " + name + "!")
  print ("  #######")
  print ("  ()%%%() ()")
  print (" () %%% ()")
  print ("()  %%%  ")
  print ("    %%%")
  print ("    \_/")
  print ("What is your height in meters?")
  height= float (input())
  print ("What is your age?")
  age= str (input())
  print ("What is your weight in Kg?")
  weight= float (input())
  BMI = (weight / height**2)
  print ("  #######")
  print ("  # " + eye + "." + eye + " #")
  print ("  # --- #  "+ name + " you are " + age + "years old," + " and your BMI is " +  "{:.2f}".format(BMI) +".")
  print ("  #######")
  print ("  ()%%%()")
  print (" () %%% ()")
  print ("()  %%%  ()")
  print ("    %%%")
  print ("    \_/")
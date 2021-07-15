#BMI input / output
def run():
  print("What is your name?")
  name= input()
  print ("What is your height in meeters?")
  height= float (input())
  print ("What is your age?")
  age= str (input())
  print ("What is your weight in Kg?")
  weight= float (input())
  BMI = weight / height**2
  print("\n")
  print ( name + f" you are {age} years old," + f" and your BMI is {BMI}")

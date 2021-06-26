#BMI input / output
print("What is your name?")
name= input()
print ("What is your height in cm?")
height= float (input())
print ("What is your age?")
age= str (input())
print ("What is your weight in Kg?")
weight= float (input())
BMI = weight / (height/100)**2
print("\n")
print ( name + f" you are {age} years old," + f" and your BMI is {BMI}")
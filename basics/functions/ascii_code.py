print("Program started!")
c = input("Please enter a standard character:")
if len(c) == 1:
  print("The ASCII code for {} is {}".format(c, ord(c)))
else:
  print("Incorrect character enetered!")
print("Program Ended!")
#using chr function
print("Program started!")
potato = abs(int (input("Please enter an ASCCII code:\n")))
if potato in range(32,127):
  print("The character represented by the ASCII code {} is {}". format(potato, chr(potato)))
else:
  print("This is an error! Invalid number code")
print("Program Ended!")
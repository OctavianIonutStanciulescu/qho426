#using the for function with user input to reverse a phrase
def run():
  print("What phrase do you see?") 
  x = input()
  print("\nReversing ...\n\nThe phrase is: ", end ="")
  for position in range(len(x) - 1, -1, -1):
    print(x[position], end = "")
#Using reverse in a for function
def run():
  print("What phrase do you see?")
  a = input()
  print("\nReversing...")
  b = ""
  for c in a:
    b = c + b
  print("\nThe phrase is: ",b)
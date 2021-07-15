# Modulus operator function
def run():
  whole_number = int(input("Please enter a whole number:\n"))
  if (whole_number%2) == 0:
    print ("The number {0} is an even number".format(whole_number))
  else:
    print ("The number {0} is an odd number".format(whole_number))
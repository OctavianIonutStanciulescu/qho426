#using one loop nested in another
def run():
  print("How many rows should I have?") 
  a = int(input())
  print ("How many columns should I have?")
  b = int(input())
  c = ":-)"
  for count in range(0,a,1):
    for number in range (0,b,1):
      print (c, end ="")
    print()
  print ("Done!")
#manipulating an user input list into a set
def observed():
  observations = []
  for i in range(7):
    observations.append(input("Please enter an observation:\n"))
  print(observations)
  return observations
def run():
  print("Counting observations...")
  x = observed()
  y = set(x)
  z = list(y)
  count0 = x.count(z[0])
  count1 = x.count(z[1])
  print(z)
  print(z[0], "observed" , count0 ,"times.")
  print(z[1], "observed" , count1 ,"times.")
run()
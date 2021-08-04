#manipulating an user input list into a set
def observed():
  observations = []
  for i in range(5):
    observations.append(input("Please enter an observation:\n"))
  print(observations)
  return observations

def remove_observations(observations):
  t = observed()
  while True:
    print("Do you wish to remove an observation (yes/no)?")
    rem = input()
    if rem == "yes":
     t.remove(input("What observation do you want to remove?\n"))
     print("Done!")
    else:
      break
  return t


def run():
  
  print("Counting observations...")
  x = remove_observations(1)
  y = set(x)
  z = list(y)
  count0 = x.count(z[0])
  count1 = x.count(z[1])
  print(z)
  print(z[0], "observed" , count0 ,"times.")
  print(z[1], "observed" , count1 ,"times.")
run()


def run():   
  observations = observed()   
  remove_observations(observations)    
  observe_set = set()   
  for observation in observations:     
    data = (observation, observations.count(observation))                     observe_set.add(data)    
  for data in sorted(observe_set):     
    print("{} observed {} times." .format(data[0], (data[1])))
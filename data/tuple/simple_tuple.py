#populating a lists with user input

def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return (min(likelihoods))

def run():
  m = likelihood()
  print("Minimum likelihood of falling: {}%".format(m))
run()
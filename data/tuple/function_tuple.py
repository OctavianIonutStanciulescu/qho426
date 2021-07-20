#selecting specific elements from a tuple

def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return (min(likelihoods), (max(likelihoods)))
def run():
  m = likelihood()
  print("Minimum likelihood of falling: {}%".format(m[0]))
  print("Maximum likelihood of falling: {}%".format(m[1]))
run()

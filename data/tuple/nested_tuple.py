def steps():
  likelihoods = [("step 1", 50), ("step 2", 38),("step 3", 37),("step 4", 99),("step 5", 4)]
  return likelihoods
def run():
  m = steps()
  bad_steps=[number[1] for number in m]
  good_steps=[]
  bad_steps1=[]
  for number in bad_steps:
      if number >= 50 :
        good_steps.append(number)
      else:
        bad_steps1.append(number)
  print ("Good steps: {}, Bad steps: {}".format(len(good_steps),len(bad_steps1)))
run()

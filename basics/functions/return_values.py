#use of multiple user defined functions with return values
def sum_wieghts(w1, w2): 
  return (w1+w2)

def calc_avg_weight(w1, w2):
  return (sum_wieghts(w1,w2)/2)

def run():
  w1 = int(input("Please enter the weight of Beep: "))
  w2 = int(input("Please enter the weight of Bop: "))
  i = input("What would you like tu calculate (sum or average)? ")
  if i == "sum":
    print ("The sum of Beep and Bop`s weight is ", sum_wieghts(w1, w2))
  elif i == "average":
    print("The average weight of Beep and Bop is ", calc_avg_weight(w1, w2))
  else:
    print ("Invalid Input!")
    run()
run()
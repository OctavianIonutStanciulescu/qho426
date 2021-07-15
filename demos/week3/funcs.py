def calc_area(height = 2, base = 1):

  area = 0.5*height*base
  return area
def run():
  h = float(input("Enter hieght of the triange: "))
  b = float(input("Enter Base of the triangle: "))

  #call the function

  print(calc_area(h, b))
  a1 = calc_area()
  a2 = calc_area(10)
  a3 = calc_area(base = 10)

  print(a1+a2+a3)

def run2():
  print(calc_area(r.randrange(1,11)))

def run3():
  x = 10.2
  print(ceil(x))
  print(log(x))
from math import pi


def students_marks():
  name = input("Enter student`s name: ")
  mark = float(input(f"Enter the mark for {name}"))
  return name,mark


# t = students_marks()
# print (t)
# print (type(t))

def area_and_circ(radius):
  area = pi*radius**2
  circ = 2*pi*radius
  return area,circ


def run():
 tuplex = area_and_circ(float(input("Enter radius of your circle")))
 print (f"Thearea of your circle is {tuplex[0]:.2f} and circumference is {tuplex[1]:.2f}")
run()
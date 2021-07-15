#using one loop nested in another
def run():
  a = input("Please enter a sequence:") 
  b = input("Please enter the character for marker:")
  is_counting = False
  count = 0
  for character in a:
    if (is_counting == False and character == b):
      print("Found first marker")
      is_counting = True
    elif (is_counting == True and character == b):
      print("Found last marker")
    elif (is_counting):
      count += 1
  print(f"The distance between the markers is {count}")
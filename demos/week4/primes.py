''' Create functions that can find out if number is prime, can find a prime number within a range of values and compute N, used in RSA encryption'''


def isPrime(number):
  for thing in range(2,number,1):
    if number % thing == 0:
      return False
  return True  

def findPrime (start, end):
  for stuff in range(start, end+1):
   if isPrime(stuff):
     return stuff

def encrypt():
  x= int(input("Povide an integer: "))
  y= int(input("Povide a second integer (larger): "))
  p1 = findPrime(x,y)
  x1= int(input("Povide an integer: "))
  y1= int(input("Povide a second integer (larger): "))
  p2 = findPrime(x1,y1)
  return p1*p2
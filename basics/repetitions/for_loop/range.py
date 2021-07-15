#using the for function with user input
def run():
  print("What level of brightness is required?") 
  i = int(input())
  a = ("\u002A")

  print("\nAdjusting brightness...")
  for i in range(1, i+1, 2):
    print(f"\nBeep`s brightness level: {i*a}")
    print(f"Bop`s brightness level:  {i*a}")
    
  print("\nAdjustments complete!")
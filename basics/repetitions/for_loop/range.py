#using the for function with user input
print("What level of brightness is required?") 
x = int(input())
a = ("\u002A")
y = x*a
print("\nAdjusting brightness...")
for count in range(0, x, 2):
  print(f"\nBeep`s brightness level: {y}")
  print(f"Bop`s brightness level:  {y}")
  
print("\nAdjustments complete!")
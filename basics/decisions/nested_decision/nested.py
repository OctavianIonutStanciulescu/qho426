#Using Nested Decision
print("What type of cover does the book have?\n") 
x = input() 
if (x == "soft"):
 print("Is the book perfect-bound?\n") 
 y = input() 
 if (y == "yes"): 
   print("Soft cover, perfect bound books are very popular!") 
 else: print("Soft covers with coils or stitches are great for short books!")
else: print("Books with hard covers can be more expensive!")
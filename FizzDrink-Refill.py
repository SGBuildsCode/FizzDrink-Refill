# Introductory Exercise - In order to test whether I've been paying attention to the Python Tutorials, the following code below 
# concerns variables and their naming conventions as well as how to declare variables correctly. Using w3schools as a framework,
# take the relevant topic (i.e. that being Variable Names) on w3schools and declare your own variables.

# 1) Variable Names - Must start with a Letter or Underscore character. 
# Examples: 

from typing import Match

# Check if this variable is empty or not. 

# Include a check where the user must enter an integer.

 # Let's assume they finish the drink before they are asked for another.

def ChooseDrink():
  global Wglass 
  DrinkChc = int(input("""Which Drink Would You Like? 
  (0) Coca-Cola
  (1) Fanta
  (2) 7Up
  (3) Lucozade
  (4) Pepsi
  (5) Dr.Pepper 
  (6) Nothing
   """))
   # This is the input procedure/method and as such it will display the string that you have written exactly as you have written it.
 # Nice One ! 
  
  match DrinkChc: 
          case 0: 
            Wglass = "Coca-Cola" 
            print("Here is Your" +" "+ Wglass + "!")
          case 1: 
            Wglass = "Fanta" 
            print("Here Is Your" +" "+ Wglass + "!")   
          case 2: 
            Wglass = "7Up" 
            print("Here is Your" +" "+ Wglass + "!")
          case 3: 
            Wglass = "Lucozade"
            print("Here is Your" +" "+ Wglass + "!")
          case 4: 
            Wglass = "Pepsi"
            print("Here is Your" +" "+ Wglass + "!")
          case 5: 
            Wglass = "Dr Pepper"  
            print("Here is Your" +" "+ Wglass + "!")

ChooseDrink()

while Wglass: 
  Refill = input("Would You Like Another Drink? Y For Yes; N For No")
  if Refill == "Y":
    ChooseDrink() 
  elif Refill == 'N':
    Wglass = "" # This statement is included to exit the while loop.
    exit
  

# Programming Code Status Update : Success! I have worked out this solution! Nice ! Keep It Up!


   







 



     





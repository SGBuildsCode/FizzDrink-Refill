# This file has been extracted from a project in Visual Studio Code and as such the packages within this file (to the best of my knowledge) may not function correctly should other
# development environments be used.
from typing import Match

# In future I wish to include a check where the user must enter an integer.

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
  
 # Within the input procedure/method, utilizing multiline strings this ensures that we can display a vertical menu to the user which will appear exactly as we have written it.  
  
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
    Wglass = "" # This statement is included to exit the while loop. In more detail once the user has entered 'N' for no for the purposes of simplicity 
    exit        # let's assume that they have finished the drinks that they have been served and they no longer wish to have any more (i.e. they are 
                # surfeited)   




   







 



     





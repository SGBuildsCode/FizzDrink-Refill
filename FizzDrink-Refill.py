from ast import Break
from typing import Match
# For testing purposes include a check where the user must enter an integer.

# This program (in accordance with convention and logic) assumes and requires that the customer must 
# finish their drink first before they are asked for another. 



def ChooseDrink():
  try:
    global DrinkChc
    DrinkChc = int(input("""Which Drink Would You Like? 
    (0) Coca-Cola
    (1) Fanta
    (2) 7Up
    (3) Lucozade
    (4) Pepsi
    (5) Dr.Pepper 
    (6) Nothing
    """)) 
    
    global Wglass

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
          case 6: 
            Wglass = None
           # print("Good Bye! Hope You Have A Nice Day! ")
            exit
    if DrinkChc not in range(0,7):
      Wglass = None
      print("The Number You Have Entered Is Not In Range!")
    else:
      pass
  except (ValueError,TypeError):
    Wglass = None
    print("You have Not Entered A Number!") 

# This is the input procedure/method and as such it will display the string within the input statement in the manner that the user 
# has written it. 

ChooseDrink()

while Wglass:
  Refill = input("Would You Like Another Drink? Y For Yes; N For No")
  if Refill == "Y":
    ChooseDrink() 
  elif Refill == 'N':
    Wglass = ""
    # This statement is included to exit the while loop.
    exit
  




   







 



     





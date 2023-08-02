print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("you are decide to direction to move on a TREASURE...")
print("WARNING:you decide a wrong direction the game will be over(your loss)")
direction = str(input("ENTER THE YOUR DECIDING DIRECTION:left ot right="))
if (direction =="left"):
    print("you going to a correct direction")
    print("you reach a next level")
    ocen=str(input("ENTER YOU CHOICE:WAITING FOR BOAT OR SWIM="))
    if(ocen=="wait"):
      print("awesom!you have  a boat ")
      print("using the boat to reach a treasure island")
      door=str(input("ENTER YOUR CHOICE DOOR IN THE TRESSURE ISLAND,RED,BLUE OR YELLOW="))
      if(door=="yellow"):
        print("YOU REACH TREASURE... YOU WON GAME")
      elif(door=="red")or(door=="blue"):
        print("SORRY! YOUR ARE DEATH IN TREASURE ISLAND")
        print("YOUR COME CLOSER TO WON THE BETTER LUCK NEXT TIME")
        print("BUT THIS TIME YOU ARE LOSS!GAME OVER")
    
      
    else:
      print("your death in ocen!GAME OVER")
else:
    print("WRONG DIRECTION SORRY,GAME OVER")
    print("SORRY!GAME OVER")

    
  

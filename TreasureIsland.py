#You can print the arts like below in your output. you can use ascii.co.uk/art and search for treasure for the picture like below. And to print those ascii art you need the write the print statement like print('''   ascii art   ''') otherwise it won't work or gets confused.


print(''' *******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')


print("Welcome to the TREASURE ISLAND.")
print("Your mission is to find out the TREASURE.")
choice1 = input ('You are across the road.Where do you want to go?'
                'Type "left" or "right".\n').lower() 
#we can use single code to wrap the line of the code in single cotes if the double cotes are used inside the strings or double cotes itself.and the backslace inside th string is used if we want to include ' this kinda symbol
#we used .()lower above so that the user can get the result even though they type RIGHT or Right instead of writing right.Same condition applies for left.

if choice1 == "left":
    choice2 = input('You\'ve come to a lake, there is an island in the middle of the lake.'
                    'Type "wait" to wait for a boat.'
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 =input('You have sucessfully arrived at the island.'
                       'Final step to go.There is a house with 3 doors.'
                       'One red, one blue and one yellow.'
                       'Which colour door do you prefer to open?'
                       'Type "red" for red coloured door, type "blue" for blue and "yellow" for yellow.\n').lower()
        if choice3 == "red":
            print("It's a room full of fire.GAME OVER")    
        elif choice3 == "blue":
            print("You have entered a room full of beasts. GAME OVER")
        elif choice3 == "yellow":
            print("Congratulations. You win!:)")
            print('''  __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    miK
             '\/' ''')
        else:
            print("You chose a door that doesn't exist. GAME OVER")
        
    elif choice2 == "swim":
        print("You got attacked by crocodiles. GAME OVER")
    else:
        print("You typed a wrong input.")
if choice1 == "right":
    print("Oops! You fell in to a hole.GAME OVER")



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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************



''')

left_right = input("Left or right?:\n")

if left_right == "right":
    print("Game over, cameras caught you!")
elif left_right == "left":
    swim_wait = input("swim or wait?:\n")
    if swim_wait == "swim":
        print("Game over, guards were alerted")
    elif swim_wait == "wait":
        door = input("Which door red, blue or yellow?:\n")
        if door == "red" or door == "blue":
            if door =="red":
                print("Game over, there was a trap!")
            elif door == "blue":
                print("Game over, there was no treasure in the room")
        elif door == "yellow":
            sneak_kill = input("You saw a guard, would you like to kill or sneak-in? (kill/sneak):\n")
            if sneak_kill == "kill" or sneak_kill == "Kill" or sneak_kill == 'sneak' or sneak_kill == 'Sneak':
                print("Congratulations, you have successfully obtained the treasure!")
            else:
                print("Please enter a valid option!")
        else:
            print("There is no door such that!")
    else:
        print("Please enter a valid option!")
else:
    print("Please enter a valid option!")

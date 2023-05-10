import pygame
import random
import time
play = 1
def intro():
    print("You are in a land full of dragons. In front of you there are three caves. "
          "One cave contains a friendly dragon that will give you his treasure."
          " Another one contains a powerful and wise dragon that will share his power with you. "
          "The last cave contains an evil and greedy dragon that will devour you. ")
    print(" ")

def choosecave():
    cave = " "
    cave = input("Which cave will you go into? 1, 2, or 3")

    return cave

def checkcave(chosencave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in he front you! He opens his jaws and...")
    time.sleep(2)

    friendlycave = random.randint(1,3)
    powerortreasure = random.randint(1,2)



    if chosencave == str(friendlycave) and powerortreasure == 1:
        print("Shares his power!")

    elif chosencave == str(friendlycave) and powerortreasure == 2:
        print("Shares his treasure!")




    else:
        print("Gobbles you up!")

while play == 1:

        intro()
        cavenumber = choosecave()
        checkcave(cavenumber)

        play = int(input("Do you want to play again? Please type 1 for yes or 2 for no"))

        if play == 2:
            print("Thanks for playing!")
            quit()













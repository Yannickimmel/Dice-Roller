import random
"""
This is a  setting the art for the dice
"""
dice_art ={
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),

    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│      ●  │",
       "└─────────┘"),

    3:("┌─────────┐",
       "│  ●      │",
       "│    ●    │",
       "│      ●  │",
       "└─────────┘"),

    4:("┌─────────┐",
       "│  ●   ●  │",
       "│         │",
       "│  ●   ●  │",
       "└─────────┘"),

    5:("┌─────────┐",
       "│  ●   ●  │",
       "│    ●    │",
       "│  ●   ●  │",
       "└─────────┘"),

    6:("┌─────────┐",
       "│  ●   ●  │",
       "│  ●   ●  │",
       "│  ●   ●  │",
       "└─────────┘"),
    }

"""
This is intialising the dice with random numbers between 1 and 6 
"""
dice =[]
total = 0
number_of_dice = int(input("How many dice would you like to roll? "))
for x in range(number_of_dice):
    dice.append(random.randint(1,6))
"""
Prints out art of dice
"""
for line in range(5):
    for x in dice:
        print(dice_art.get(x)[line], end="")
    print()
"""
This is adding up the total of the dice and printing it out
"""
for x in dice:
    total+=x
    print(f"Total; {total}")
 

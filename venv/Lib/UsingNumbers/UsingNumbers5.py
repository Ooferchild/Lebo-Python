#Josh
import random

dice = random.randint(1,6)
dice2 = random.randint(1,6)
print("You rolled a", dice, "and a", dice2, "for a total of", dice + dice2)

if dice == dice2:
    print("Doubles!")
    choice = input("Press yes to go again")
    if choice == "yes":
        dice = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("You rolled a", dice, "and a", dice2, "for a total of", dice+dice2)
        if dice == dice2:
            print("Doubles!")
            choice = input("Press yes to go again")
            if choice == "yes":
                dice = random.randint(1,6)
                dice2 = random.randint(1,6)
                print("You rolled a", dice, "and a", dice2, "for a total of", dice+dice2)
                if dice == dice2:
                    print("Doubles!")
                    choice = input("Press yes to go again")
                    if choice == "yes":
                        dice = random.randint(1, 6)
                        dice2 = random.randint(1, 6)
                        print("You rolled a", dice, "and a", dice2, "for a total of", dice + dice2)
                        print("You lose!")

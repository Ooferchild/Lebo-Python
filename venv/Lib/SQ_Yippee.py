#Josh
import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

turns = 3

while turns > 0:
    game = True
    input("Press enter to roll")
    print("You rolled the dice and got", dice1, "and", dice2, "for a total of", dice1 + dice2)
    if dice1 + dice2 == 7 or dice1 + dice2 == 11:
        print("You win!")
        break
    elif dice1 + dice2 ==2 or dice1 + dice2 ==12:
        print("You lose!")
        break
    else:
        yip = dice1 + dice2
        print("The YIP is now", yip)
        turns = turns - 1
        print("You have", turns, "turns left")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        input("Press enter to roll again")
        print("You rolled the dice and got", dice1, "and", dice2, "for a total of", dice1 + dice2)
        if dice1 + dice2 == yip:
            print("You win!")
            break
        else:
            turns = turns - 1
            print("You have", turns, "turnbb left")
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            input("Press enter to roll again")
            print("You rolled the dice and got", dice1, "and", dice2, "for a total of", dice1 + dice2)
            if dice1 + dice2 == yip:
                print("You win!")
                break
            else:
                print("You lose!")
                break
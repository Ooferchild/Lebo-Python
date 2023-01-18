#Josh

import random

num = random.randint(1,50)

pick = int(input("Pick a number between 1 and 50: "))

#5 tries
#warm/cold test
for i in range(4):
    if pick == num:
        print("You win!")
        break
    elif abs(pick) - abs(num) > 20:
        print("Frozen, more than 20 away")
        pick = int(input("Pick a number between 1 and 50:"))
    elif abs(pick) - abs(num) > 10:
        print("Cold, more than 10 away")
        pick = int(input("Pick a number between 1 and 50:"))
    elif abs(pick) - abs(num) > 10:
        print("Warm, less than 10 away")
        pick = int(input("Pick a number between 1 and 50:"))
    elif abs(pick) - abs(num) < 5:
        print("Hot, less than 5 away")
        pick = int(input("Pick a number between 1 and 50:"))
    else:
        print("You lose!")
        break

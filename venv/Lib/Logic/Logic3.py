#Josh

test1= input("What is your first test score? ")
test2= input("What is your second test score? ")
test3= input("What is your third test score? ")
avg = (int(test1) + int(test2) + int(test3)) // 3
print(f"Your average is {avg}")
if avg >= 90:
    print("You got an A!")
elif avg >= 80:
    print("You got a B!")
elif avg >= 70:
    print("You got a C!")
elif avg >= 65:
    print("You got a D!")
else:
    print("You failed!")

ec = int(input("What is your extra credit score? "))
if ec == 3:
    print("I got have the points")
elif ec == 2:
    print("2 is better than nothing")
elif ec == 1:
    print("You earned some extra credit")
else:
    print("What extra credit?")
#Josh

name = input("What is your name?")
print(f"Hello {name}, how did you do on the test?")
number = input("What is your score?")

if number >= 90:
    print("You got an A!")
elif number >= 80:
    print("You got a B!")
elif number >= 70:
    print("You got a C!")
elif number >= 60:
    print("You failed!")
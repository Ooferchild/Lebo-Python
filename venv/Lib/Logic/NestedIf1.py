#Josh

'''Nested If Statement
We can insert a NEW chain of logic into a true conditional logic
step.
This nested if ONLY happens if the first if is true.
We can nest into ifs, elifs, and elses.
Its like adding more questions, if the first question is true.
'''

num = int(input("Pick a number "))
if num > 0:
    print("Positive")
    print("1) Make it negative\n2) Make it zero\n3) Keep it the same")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"-{num}")
    elif choice == 2:
        print("0")
    elif choice == 3:
        print(num)
    else:
        print("Invalid choice")
elif num < 0:
    print("Negative")
    print("1) Make it positive\n2) Make it zero\n3) Keep it the same")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"+{num}")
    elif choice == 2:
        print("0")
    elif choice == 3:
        print(num)
    else:
        print("Invalid choice")
elif num == 0:
    print("You chose nothing")
    print("1) Make it positive\n2) Make it negative\n3) Keep it the same")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(num+10)
    elif choice == 2:
        print(num-10)
    elif choice == 3:
        print(num)
    else:
        print("Invalid choice")
else:
    print("Invalid number")

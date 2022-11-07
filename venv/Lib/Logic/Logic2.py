#Josh
#11-4

num = int(input("Pick a number 1-10 "))

if num > 5:
    print("Thats a big number!")
elif num <= 5:
    print("Thats a small number!")

num = int(input("Pick a number 1-19 "))
if num >= 13:
    print("Thats a teen number!")
elif num == 12 or num == 11:
    print("Thats a kid number!")
else:
    print("Try again!")
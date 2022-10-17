import math #Tells code you need math tools
#Josh
#10-17 → In Out 3
##################################


#making a menu for calculator
def menu():
    _int = [1,2,3,4,5,6,7,8,9,0]
    numberOne = int(input("First number: "))
    numberTwo = int(input("Second number: "))

    if not numberTwo or numberOne in _int:
        print("Please input a valid integer")

    x = input("a - add\ns - subtract\nm - multiply\nd - divide\n")
    if x == "a":
        add = numberOne + numberTwo
        print(f"{numberOne} + {numberTwo} = {add}")
    elif x == "s":
        subtract = numberOne - numberTwo
        print(f"{numberOne} - {numberTwo} = {subtract}")
    elif x == "m":
        multiply = numberOne * numberTwo
        print(f"{numberOne} * {numberTwo} = {multiply}")
    if x == "d":
        quot = numberOne // numberTwo
        print(f"{numberOne} / {numberTwo} = {quot}")
    else:
        print("That is not a valid option")
        exit()
#for the calculator
#menu()

'''
Setting something to a 'power' of something → ** or pow() or ^
Forcing division to be an integer → //
'''

#pythgorean theorem → a^2 + b^2 = c^2
a = int(input("a: "))
b = int(input("b: "))
c2 = a**2 + b**2
c = math.sqrt(c2)
print(f"A triangle with sides {a} and {b} has a hypotenuse of {c}")
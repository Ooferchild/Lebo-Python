#Josh

name = input("What's your full name? ")
maiden = input("What's your mothers maiden name? ")
city = input("What city were you born in? ")
car = input("What's your car? ")
space = name.find(" ")
first = name[0:space]
last = name[space+1:]
sw_name = first[0:3] + last[0:2] + " " + maiden[0:2] + city[0:3]
print(f"Your Star Wars name is {sw_name}")
print(f"Your Star Wars planet is {last[-2:] + car}")
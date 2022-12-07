#Josh

team = input("What's your favorite sports team? ")
if len(team) >= 4:
    print(f"{team[0:4]}")
elif len(team) <= 3:
    print(f"{team}")
else:
    print("You didnt enter a team")
#last 3
print(f"{team[-3:]}")

food = input("What's your favorite food? ")
foodcut = food[1:-1]
print(f"{foodcut}")

name = input("What's your full name? ")
space = name.find(" ")
first = name[0:space]
last = name[space+1:]
print(f"{first} {last}",sep="*")
comboName = last[0] + first[1:] + " " + first[0] + last[1:]
print(f"{comboName}")
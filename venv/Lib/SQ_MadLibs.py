#Josh
import pyfiglet

#ascii art
ascii_banner = pyfiglet.figlet_format("Mad Libs")
print(ascii_banner)

#setting lists
adjective = []
noun = []
verb = []
pluralNoun = []

#questions
pluralNoun.append(input("Enter a plural noun: "))
pluralNoun.append(input("Enter a plural noun: "))
pluralNoun.append(input("Enter a plural noun: "))
noun.append(input("Enter a noun: "))
noun.append(input("Enter a noun: "))
noun.append(input("Enter a noun: "))
pluralNoun.append(input("Enter a plural noun: "))
adjective.append(input("Enter an adjective: "))
noun.append(input("Enter a noun: "))
adjective.append(input("Enter an adjective: "))

#printing story
print(f"Halloween is my favorite holiday, because we get to dress up as {pluralNoun[0]} and eat {pluralNoun[1]}. I get to visit {pluralNoun[2]} in our {noun[0]}, saying {noun[1]} or {noun[2]}! In exchange, they give me {pluralNoun[3]}! It's the best holiday ever!")
print(f"This year, I'm going to dress up as a {adjective[0]} {noun[3]}. My costume is going to be so {adjective[1]}!")
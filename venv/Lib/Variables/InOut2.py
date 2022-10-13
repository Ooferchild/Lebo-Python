#Josh
#10-13 → In Out 2
##################################

# I am using f strings instead of commas to make it easier

name = input("What is your name: ")
print(f"Hello, {name}")
team = input("What is your favorite sports team: ")
print(f"Really? My favorite sports team is {team} too!")

print("Welcome to Joshua's Sandwich maker!\nWe exel at making the worlds best sandwiches!")
#bread cheese meat veggies sauce
bread = input("what kind of bread would you like? ")
veggies= input("what kind of veggies would you like? ")
meat= input("what kind of meat would you like? ")
cheese= input("what kind of cheese would you like? ")
sauce= input("what kind of sauce would you like? ")
print(f"You ordered a {meat} sandwich with {cheese}, {veggies} and {sauce}.")

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
sum = num1 + num2
diff = num1 - num2
prod = num1*num2
print(num1,"+",num2,"=",sum)
print(num1,"-",num2,"=",diff)
print(num1,"*",num2,"=",prod)
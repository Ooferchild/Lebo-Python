#Josh
import json

#money ranges
LB = ["1LB", "5LB", "25LB", "125LB", "625LB"]
def check_user(user):
    with open('leboville.json') as f:
        data = json.load(f)
        if user in data:
            user = input("Enter your username again: ")
            password = input("Enter your password: ")
            if password >= 8 and any(char.isdigit() for char in password) and any(
                    char.isupper() for char in password) and any(char.islower() for char in password):
                print("Your password is strong")
                if password == data[user]:
                    print("You have been signed in")
                else:
                    print("Incorrect password")
                    exit()
            if user in data:
                if password == data[user]:
                    print(f"Welcome {user}")
                else:
                    pass
        else:
            print("User not found")
            newUser = input("Would you like to create a new account? (y/n) ")
            if newUser == "y":
                newUser = input("Enter your username: ")
                newPass = input("Enter your password: ")
                data[newUser] = newPass
                with open('leboville.json', 'w') as f:
                    json.dump(data, f)
                checkUser(newUser)
            if newUser == "n":
                print("Goodbye")
                exit()
            else:
                print("Invalid input")
                exit()

def login():
    print("Welcome back to the Leboville Bank ATM")
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("leboville.json", "r") as f:
        data = json.load(f)
        if user in data:
            if password == data[user]:
                print("You have been signed in")
                print("Please choose an option")
                print("1. Check Balance")
                print("2. Withdraw Money")
                print("3. Deposit Money")
                print("4. Change Password")
                print("5. Exit")
                choice = int(input("Please enter your choice: "))
                if choice == 1:
                    check_balance()
                if choice == 2:
                    withdraw_money()
                if choice == 3:
                    deposit_money()
                if choice == 4:
                    change_password()
                if choice == 5:
                    exit()
def check_balance():
    with open("leboville.json", "r") as f:
        data = json.load(f)
        print(f"Your current balance is {data['balance']}")
        print("Would you like to make another transaction? (y/n)")
        choice = input("Please enter your choice: ")
        if choice == "y":
            login()
        if choice == "n":
            exit()

def withdraw_money():
    with open("leboville.json", "r") as f:
        data = json.load(f)
        print("Please choose a money range")
        print("1. 1LB")
        print("2. 5LB")
        print("3. 25LB")
        print("4. 125LB")
        print("5. 625LB")
        print("6. Other")
        print("7. Exit")
        choice = int(input("Please enter your choice: "))
        for option in LB:
            if choice == range(1, 6):
                if data["balance"] >= option:
                    data["balance"] -= option
                    print(f"Your new balance is {data['balance']}")
                    print("Would you like to make another transaction? (y/n)")
                    choice = input("Please enter your choice: ")
                    if choice == "y":
                        login()
                    if choice == "n":
                        exit()
                else:
                    print("You do not have enough money to make this transaction")
                    print("Would you like to make another transaction? (y/n)")
                    choice = input("Please enter your choice: ")
                    if choice == "y":
                        login()
                    if choice == "n":
                        exit()
                    data["balance"] -= option
                if data["balance"] >= option:
                    pass

def main():
    print("Welcome to the Leboville Bank ATM")
    print("If this is your first time using this ATM, please press 1")
    print("If you used your ATM before, please press 2")
    print("If you would like to exit, please press 3")
    print()
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        user = input("Enter your username: ")
        check_user(user)
    if choice == 2:
        login()
if __name__ == "__main__":
    main()
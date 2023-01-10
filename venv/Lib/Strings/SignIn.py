#Josh

#Should have json database
#Should have a way to check if the user is in the database
#Should have a way to add the user to the database
#Should have a way to check if the password is correct
#Should have a way to check if the user is already signed in
#Should have a way to sign the user in
#Remember me option
#Should have a way to sign the user out

#code
import json
import os

def checkUser(user):
    with open('data.json') as f:
        data = json.load(f)
        if user in data:
            user = input("Enter your username: ")
            password = input("Enter your password: ")
            if password>=8 and any( char.isdigit() for char in password ) and any( char.isupper() for char in password ) and any( char.islower() for char in password ):
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
                with open('data.json', 'w') as f:
                    json.dump(data, f)
                checkUser(newUser)
            if newUser == "n":
                print("Goodbye")
                exit()
            else:
                print("Invalid input")
                exit()

def changePass(user):
    with open('data.json') as f:
        data = json.load(f)
        if user in data:
            print("Enter your new password")
            newPass = input("Enter your new password: ")
            data[user] = newPass
            with open('data.json', 'w') as f:
                json.dump(data, f)
            print("Your password has been changed")
        else:
            print("User not found")
            exit()

def main():
    print("Welcome to the sign in page")
    print("What would you like to do?")
    print("1. Sign in")
    print("2. Sign out")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        user = input("Enter your username: ")
        checkUser(user)
        print("Would you like to change your password? (y/n) ")
        change = input("Enter your choice: ")
        if change == "y":
            changePass(user)
        if change == "n":
            print("Goodbye")
            exit()
    if choice == "2":
        print("You have been signed out")
        exit()
    if choice == "3":
        print("Goodbye")
        exit()

if __name__ == "__main__":
    main()
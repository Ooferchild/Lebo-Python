#Josh

num = int(input("Enter a number: "))
if num%3 == 0 and num%4 == 0:
    print(num,"is a perfect number")
elif num%3 == 0:
    print(num,"is a cool number")
elif num%4 == 0:
    print(num,"is an ok number")
else:
    print(num,"is a sad number")

#scientific notation
num = int(input("Enter a 3 digit number: "))
temp = num
digit100 = temp//100
temp = temp%100
digit10 = temp//10
temp = temp%10
digit1 = temp
print(f"{digit100} x 100 + {digit10} x 10 + {digit1} x 1 = {num}")
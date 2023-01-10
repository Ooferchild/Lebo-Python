#find remainder of equation
eq = [25//5, 13//4, 18//5,17//9]
for i in eq:
    print(i%1)

num = int(input("Enter a number: "))
if num%2 == 0:
    print(num,"is even")
else:
    print(num,"is odd")

#mixed fraction
num = int(input("Enter the numerator: "))
den = int(input("Enter the denominator: "))
if num%den == 0:
    print(num//den)
else:
    print(num//den," and ",num%den,"/",den, sep="")

#divisable by 3
num = int(input("Enter a number: "))
if num%3 == 0:
    print(num,"is divisible by 3")
else:
    print(num,"is not divisible by 3")
#Josh

#convert numbers to binary
n = int(input("Enter a number: "))
b= []
while(n>0):
    d=n%2
    b.append(d)
    n=n//2
b.reverse()
print("Binary Equivalent is: ",end="")
for i in b:
    print(i,end="")
print()
#convert binary to numbers
n = int(input("Enter a binary number: "))
b= []
while(n>0):
    d=n%10
    b.append(d)
    n=n//10
b.reverse()
print("Number Equivalent is: ",end="")
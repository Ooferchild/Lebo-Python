import math
#Josh

#quadratic equation
#ax^2 + bx + c = 0
#x = (-b ± √(b^2 - 4ac)) / 2a
input = [input("Enter the value of a: "), input("Enter the value of b: "), input("Enter the value of c: ")]
a = float(input[0])
b = float(input[1])
c = float(input[2])
plus = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
minus = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print("The roots are: ", plus,minus)
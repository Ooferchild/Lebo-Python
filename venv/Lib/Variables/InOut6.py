import math
#Josh
#10-20 → InOut 6 → Practicing inputs
##################################

#surface area of a cylinder
radius = input("Enter the radius of the cylinder: ")
height = input("Enter the height of the cylinder: ")
print("The surface area of the cylinder is: ", 2 * math.pi * float(radius) * (float(radius) + float(height)))
#volume of a cylinder
print("The volume of the cylinder is: ", math.pi * float(radius) ** 2 * float(height))

#surface area of a cone
radius = input("Enter the radius of the cone: ")
height = input("Enter the height of the cone: ")
print("The surface area of the cone is: ", math.pi * float(radius) * (float(radius) + math.sqrt(float(height) ** 2 + float(radius) ** 2)))
#volume of a cone
print("The volume of the cone is: ", 1/3 * math.pi * float(radius) ** 2 * float(height))
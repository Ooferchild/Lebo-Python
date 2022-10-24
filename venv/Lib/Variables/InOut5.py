import math
#Josh


radius = int(input("Radius: "))
#surface of a sphere 4πr^2
surface = 4*math.pi*int(radius)**2
#volume of a sphere 4/3πr^3
volume = 4/3*math.pi*int(radius)**3

print(f"The surface area of a sphere with a radius of {radius} is {surface}")
print(f"The volume of a sphere with a radius of {radius} is {volume}")

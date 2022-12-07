#Josh
import numpy as np

time = int(input("What is the time in 24 hour format? "))
if time >= 700 and time <= 1400:
    print("You're in school")
elif time >= 500 and time <= 600:
    print("You're waking up")
elif time >= 1400 and time <= 1500:
    print("You're going home")
elif time >= 1700 and time <= 1800:
    print("You're eating food")
elif time >= 2200 and time <= 2300:
    print("You're hanging out")
elif time in range(2300,2400) or time in range(0,500):
    print("You're sleeping")
elif time > 2400 or time < 0:
    print("You made an error entering the time")

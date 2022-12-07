#Josh
import numpy as np

#Do now
temp = int(input("Enter the temperature: "))
if temp >= 75 and temp <= 90:
    print("Wear shorts.")
elif temp >= 45 and temp <=74:
    print("Shandt sleeves are fine.")
elif temp >= 35 and temp <=44:
    print("Wear a jacket.")
elif temp >= 1 and temp <=34:
    print("It's freezing outside!")
elif temp >= 91 and temp <=99:
    print("It's too hot outside!")
elif temp <=0 or temp >= 100:
    print("DONT GO OUTSIDE!")

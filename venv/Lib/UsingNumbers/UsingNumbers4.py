#Josh

#Do now: After a beautiful family dinner how can we determine who does he dishes?
import random

num = int(input("How many people live in your house? "))
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'black', 'white', 'brown', 'grey', 'cyan', 'magenta']
choice = random.randint(0, num-1)

#spin a wheel
if num > 13:
    print("Put less people")
else:
    print("The wheel has landed on",colors[choice])

sta = int(input("Please select the starting number: "))
end = int(input("Please select the ending number: "))
if sta > end:
    print("The starting number must be less than the ending number")
elif sta == end:
    print("The starting number must be less than the ending number")
else:
    for i in range(sta, end+1):
        num = random.randint(sta, end)
        print(f"{i}. {num}")

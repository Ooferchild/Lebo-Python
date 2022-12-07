#Josh

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


_month = input("What month were you born in (3-letter format)? ")
_day = int(input("What day were you born on? "))

if _day > 31 or _day < 1:
    print("You made an error entering the day")
elif _month == month[0] and _day >= 20 or _month == month[1] and _day <= 18:
    print("You are an Aquarius")
    print(f"Your bday is {_month} {_day}")
elif _month == month[1] and _day >= 19 or _month == month[2] and _day <= 20:
    print("You are a Pisces")
    print(f"Your bday is {_month} {_day}")
elif _month == month[2] and _day >= 21 or _month == month[3] and _day <= 19:
    print("You are an Aries")
    print(f"Your bday is {_month} {_day}")
elif _month == month[3] and _day >= 20 or _month == month[4] and _day <= 20:
    print("You are a Taurus")
    print(f"Your bday is {_month} {_day}")
elif _month == month[4] and _day >= 21 or _month == month[5] and _day <= 20:
    print("You are a Gemini")
    print(f"Your bday is {_month} {_day}")
elif _month == month[5] and _day >= 21 or _month == month[6] and _day <= 22:
    print("You are a Cancer")
    print(f"Your bday is {_month} {_day}")
elif _month == month[6] and _day >= 23 or _month == month[7] and _day <= 22:
    print("You are a Leo")
    print(f"Your bday is {_month} {_day}")
elif _month == month[7] and _day >=23 or _month == month[8] and _day <= 22:
    print("You are a Virgo")
    print(f"Your bday is {_month} {_day}")
elif _month == month[8] and _day >= 23 or _month == month[9] and _day <= 22:
    print("You are a Libra")
    print(f"Your bday is {_month} {_day}")
elif _month == month[9] and _day >= 23 or _month == month[10] and _day <= 21:
    print("You are a Scorpio")
    print(f"Your bday is {_month} {_day}")
elif _month == month[10] and _day >= 22 or _month == month[11] and _day <= 21:
    print("You are a Sagittarius")
    print(f"Your bday is {_month} {_day}")
elif _month == month[11] and _day >= 22 or _month == month[0] and _day <= 19:
    print("You are a Capricorn")
    print(f"Your bday is {_month} {_day}")
else:
    print("You made an error entering the date")

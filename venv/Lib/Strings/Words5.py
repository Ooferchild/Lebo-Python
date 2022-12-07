#Josh

fruit = input("Enter fruit: ")
fruitFixed = fruit.lower()
if fruitFixed == "apples":
    print("Apples are yum yum")
elif fruitFixed == "bannanas":
    print("I'm B-A-N-A-N-A-S for bannanas")
elif fruitFixed[0:6] == "tomato":
    print("Are tomatoes even a fruit?")
elif fruitFixed[0:2] == "ch":
    print("Cherries are yummy")
elif fruitFixed == "cantaloupe":
    print("Cantaloupe is a cute orange melon")
else:
    pass
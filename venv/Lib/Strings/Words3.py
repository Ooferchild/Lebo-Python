#Josh

_word = input("Enter word: ")

if len(_word) >= 3:
    print(f"The first letter is {_word[0]}. The middle letter is {_word[len(_word)//2]} and the last letter is {_word[len(_word)-1]}")
    print(f"Amount of letters: {len(_word)}")
elif len(_word) == 2:
    print(f"The first letter is {_word[0]} and the last letter is {_word[len(_word)-1]}")
    print(f"Amount of letters: {len(_word)}")
elif len(_word) == 1:
    print(f"This word has one letter")
else:
    print("You didnt enter a word")
import random

word_list = ["orange", "banana", "grapes", "mango", "strawberies"]


while True:
    word = random.choice(word_list)
    guess = input("Please enter single letter:")
    if guess in word:
        print(f'Good guess, {guess} is in word')
    else:
        print(f"Sorry, {guess} is not in word")

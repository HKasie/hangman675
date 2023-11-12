import random

word_list = ["orange", "banana", "grapes", "mango", "strawberies"]



def check_guess(guess):
    guess = guess.lower()
    word = random.choice(word_list)
    if guess in word:
        print(f"Good guess, {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in word")

def ask_for_input():
    guess = input("Please enter single letter:")
    while True:
        if len(guess) == 1 and guess.isalpha == True:
            return guess
        else:
            print("Invalid entry, Please try again!")

    check_guess(guess)
ask_for_input()
import random

word_list = ["orange", "banana", "grapes", "mango", "strawberies"]

def print_word(word_list):
    print(word_list)
    word = random.choice(word_list)
    print(word)

def guess_word():
    guess = input("Please enter a single letter:")
    if len(guess) == 1 and guess.isalpha() == True:
        print("Good guess!")
    else:
        print("Oops")

print_word(word_list)
guess_word()
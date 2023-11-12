import random

word_list = ["orange", "banana", "grapes", "mango", "strawberies"]
print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Please enter a single letter:")

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops")

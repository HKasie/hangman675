import random
word_list = ["orange", "banana", "grapes", "mango", "strawberies"]

class Hangman:
    def __init__(self, word_list, num_lives = 5):

        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(set(word_list))
        self.word_guessed = ['_', '_', '_', '_', '_']
        self.word_list = []
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        word = random.choice(word_list)
        if guess in word:
            print(f"Good guess, {guess} is in the word")
            for letter in guess:
                if letter == guess:
                    self.word_guessed[letter] = letter
            self.num_letters -= 1
                              
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in word")
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        guess = input("Please enter single letter:")
        while True:
            if len(guess) == 1 and guess.isalpha == True:
                print("Invalid letter, Please enter a single alphabetical character!")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)



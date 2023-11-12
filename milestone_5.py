import random

word_list = ["orange", "banana", "grapes", "mango", "strawberies"]

class Hangman:
    """
    This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.
    
    """

    def __init__(self, word_list, num_lives = 5):

        """
        A method to initialize the instance of the Hangman class.

        Arguments
        self: this is the instance of the class
        word_list: this is a list of my favorite fruits to randomly choose from
        num_lives: this is the number of elements in the word_list
        word: this is the variable with randomly chose element from the word_list
        num_letters: this is the length of the unique elements in the word_list
        word_guessed: a list of the word whose letters have been guessed.
        list_of_guesses: a list of the letters guesed

        """

        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(set(word_list))
        self.word_guessed = ['_', '_', '_', '_', '_']
        self.word_list = []
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        """
        A method that recieves the guessed letter as argument from the ask_for_input method, randomly chooses a word from the 
        word_list, and checks if the guessed letter is in the word. If the letter is in the word, it prints that it's a good guess.
        Also, it loops through the guesses and checks that the letter is equal to the guess, if it then replaces the elements of the
        that letter in the index where it can be found in the list of word_guessed. Also, num_lives is reduced.

        Arguments
        guess:  is the argument received from the ask_for_input method that has the input entered by users.
        word: is the one of the elements chosen at random form the word_list.
        word_guessed: a list of letters gussed by users.
        num_lives: 
        num_letters: it's the number oof letters left to the entered
        num_lives: number of elemets in the word_list to be chose.

        Returns
        Print statements
    
        
        """
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
        """
        A method to get inputs from  users and validate that the input is a single
        alpbabetical character. Also, the method checks if the guess is in the list of
        guesses and if not it appends it to the list.

        Arguments:
        guess: is a variable that stores the input entered by users.

        Returns:
        The method calls the check_guess methd and passes the returned guess as an 
        argument to it
        
        """
        guess = input("Please enter single letter:")
        while True:
            if len(guess) == 1 and guess.isalpha == True:
                print("Invalid letter, Please enter a single alphabetical character!")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if num_lives == 0:
            print("You lost")
        elif num_letters > 0:
            ask_for_input()
        else:
            print("Congrats, you won the game")

play_game()
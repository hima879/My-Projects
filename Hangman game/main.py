import random
from words import words  # a list of words from the external file/module

import string

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:  # fixed: was checking 'in words' instead of 'in word'
        word = random.choice(words)  # keeps iterating until a valid word is found
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)  # letters in the word
    alphabets = set(string.ascii_uppercase)  # all the letters in the alphabet
    used_letters = set()  # letters that the user has guessed

    lives = 6  # number of lives the user has

    while len(word_letters) > 0 and lives > 0:  # while there are still letters in the word
        print(f"\nYou have {lives} lives left and you have used these letters: {' '.join(used_letters)}")  # print the number of lives left and letters used

        # show the current word progress
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))  # e.g., C - T

        user_letter = input("Enter a letter: ").upper()
        if user_letter in alphabets - used_letters:  # only accept unused valid letters
            used_letters.add(user_letter)  # add to used letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # correct guess
                print(f"Good job! '{user_letter}' is in the word.")
            else:
                lives -= 1  # incorrect guess
                print(f"Oops! '{user_letter}' is not in the word.")
        elif user_letter in used_letters:  # already used letter
            print(f"You have already used the letter '{user_letter}'. Try again.")
        else:
            print(f"'{user_letter}' is not a valid letter. Please enter a valid letter.")

    # End of game: Win or lose
    if lives == 0:
        print(f"\nYou died! The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}!!")

# Run the game
user_input = input("Type something to start the game: ")
print("You typed:", user_input)
hangman()

import random

def guess(x):
    """
    Human guesses a random number between 1 and x (inclusive).
    """
    # Generate a random target number
    random_number = random.randint(1, x)
    # Initialize guess to a value that won't match random_number
    guess = 0

    # Loop until the user guesses correctly
    while guess != random_number:
        # Prompt the user for an integer input
        guess = int(input(f"Guess a number between 1 and {x}: "))

        # Compare the user's guess to the target
        if guess < random_number:
            print("Sorry, too low. Try again!")
        elif guess > random_number:
            print("Sorry, too high. Try again")

    # When loop ends, the guess must be correct
    print("Congratulations! You guessed the number correctly.")


def computer_guess(x):
    """
    Computer tries to guess a human-chosen number between 1 and x.
    The human gives feedback: 'h' for too high, 'l' for too low, or 'c' for correct.
    """
    low = 1         # Lower bound of the range
    high = x        # Upper bound of the range
    feedback = ''   # Initialize feedback variable

    # Keep guessing until feedback is 'c' (correct)
    while feedback != 'c':
        # If the range has more than one possible number, choose randomly
        if low != high:
            guess = random.randint(low, high)
        else:
            # When low == high, there's only one number left
            guess = low

        # Ask the human for feedback
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? ")

        # Update the search range based on feedback
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    # When feedback is 'c', the guess is correct
    print(f"Yay! Computer guessed your number, {guess}, correctly!")


# Start the game: human guesses then computer guesses within the range 1–10
guess(10)
computer_guess(10)

import random

def guess(x):
    """
    Human guesses a random number between 1 and x (inclusive).
    """
    random_number = random.randint(1, x)  # Generate a random target number
    user_guess = 0  # Initialize guess to a value that won't match random_number

    # Loop until the user guesses correctly
    while user_guess != random_number:
        try:
            user_guess = int(input(f"Guess a number between 1 and {x}: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Compare the user's guess to the target
        if user_guess < random_number:
            print("Sorry, too low. Try again!")
        elif user_guess > random_number:
            print("Sorry, too high. Try again!")

    # When loop ends, the guess must be correct
    print("🎉 Congratulations! You guessed the number correctly.")

def computer_guess(x):
    """
    Computer tries to guess a human-chosen number between 1 and x.
    The human gives feedback: 'h' for too high, 'l' for too low, or 'c' for correct.
    """
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Only one number left

        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"🎉 Yay! The computer guessed your number, {guess}, correctly!")

# Start the game
guess(10)
computer_guess(10)


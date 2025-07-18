import random  # Importing the random module to let the computer make random choices

# Function to get the player's and computer's choices
def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")  # Prompt the user to input their choice
  options = ["rock", "paper", "scissors"]  # List of valid choices
  computer_choice = random.choice(options)  # Randomly select one choice for the computer from the options

  # Store both choices in a dictionary and return it
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

# Function to determine the result of the game
def check_win(player, computer):
  # Print what the player and computer chose
  print(f"You chose {player}, computer chose {computer}.")
  
  # If both chose the same, it's a tie
  if player == computer:
    return "It's a tie!"
  
  # Logic for when the player chooses "rock"63
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"  # Rock beats scissors
    else:
      return "Paper covers rock! You lose."  # Rock loses to paper

  # Logic for when the player chooses "paper"
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"  # Paper beats rock
    else:
      return "Scissors cuts paper! You lose."  # Paper loses to scissors

  # Logic for when the player chooses "scissors"
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You win!"  # Scissors beats paper
    else:
      return "Rock smashes scissors! You lose."  # Scissors loses to rock

# ----- Main game execution -----
choices = get_choices()  # Call the function to get both player and computer choices
result = check_win(choices["player"], choices["computer"])  # Determine the result based on the choices
print(result)  # Print the outcome of the game

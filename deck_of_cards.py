import random  # 🔄 Used to shuffle the deck randomly

# 🧱 Card class: represents a single playing card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit      # Suit (e.g., hearts, spades)
        self.rank = rank      # Rank dictionary: {"rank": "A", "value": 11}

    def __str__(self):
        # Returns a string like "A of spades"
        return f"{self.rank['rank']} of {self.suit}"


# 🃏 Deck class: represents a full deck of 52 cards
class Deck:
    def __init__(self):
        self.cards = []  # 📦 List to hold all the cards

        # All suits and ranks in a deck
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]

        # 🧩 Combine each suit with each rank to make 52 cards
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))  # Create a Card object and add to deck

    # 🎲 Shuffle the deck
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)  # Randomly rearrange the cards

    # 🃏 Deal a number of cards
    def deal(self, number):
        cards_dealt = []
        for _ in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()  # Remove the top card from the deck
                cards_dealt.append(card) # Add it to the dealt cards
        return cards_dealt  # Return the list of dealt cards


# ✋ Hand class: represents a player's or dealer's hand
class Hand:
    def __init__(self, dealer=False):
        self.cards = []      # List of Card objects in hand
        self.value = 0       # Total value of the hand
        self.dealer = dealer # 🧑‍💼 Flag to differentiate dealer from player

    def add_cards(self, card_list):
        # Add one or more cards to the hand
        self.cards.extend(card_list)

    # 🧠 Calculate the total value of cards in hand
    def calculate_value(self):
        self.value = 0
        has_ace = False  # Track if hand contains an Ace

        for card in self.cards:
            self.value += int(card.rank['value'])  # Add card value
            if card.rank['rank'] == "A":
                has_ace = True  # Remember if there's an Ace

        # 👑 Ace can be 1 instead of 11 to avoid busting
        if has_ace and self.value > 21:
            self.value -= 10  # Count Ace as 1 instead of 11

    def get_value(self):
        # Calculate and return the hand's value
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        # True if hand is a blackjack (Ace + 10-value card)
        return self.get_value() == 21 and len(self.cards) == 2

    # 👀 Display hand (hides dealer's first card if needed)
    def display(self, show_all_dealer_cards=False):
        owner = "Dealer's" if self.dealer else "Your"
        print(f"{owner} hand:")

        for index, card in enumerate(self.cards):
            # Hide dealer's first card if not showing all cards and not blackjack
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print("🔒 Hidden card")
            else:
                print(card)

        # Show value if not dealer or if all dealer cards are shown
        if not self.dealer or show_all_dealer_cards:
            print("💯 Value:", self.get_value())
        print()


# 🎮 Game class: handles the entire game logic
class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        # Ask user how many games they want to play
        while games_to_play <= 0:
            try:
                games_to_play = int(input("🎲 How many games do you want to play?: "))
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

        # 🔁 Loop through games
        while game_number < games_to_play:
            game_number += 1
            deck = Deck()      # Create a new deck for each game
            deck.shuffle()     # Shuffle the deck

            # ✋ Create hands for player and dealer
            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            # Deal 2 cards to both player and dealer
            for _ in range(2):
                player_hand.add_cards(deck.deal(1))
                dealer_hand.add_cards(deck.deal(1))

            print("\n" + "*" * 30)
            print(f"🕹️ Game {game_number} of {games_to_play}")
            print("*" * 30)

            player_hand.display()  # Show player's hand
            dealer_hand.display()  # Show dealer's hand (with one card hidden)

            # Check for winner at start (blackjack or bust)
            if self.check_winner(player_hand, dealer_hand):
                dealer_hand.display(show_all_dealer_cards=True)
                continue  # Go to next game

            # Player's turn: hit or stand
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["stand", "s"]:
                choice = input("🤔 Do you want to hit or stand? (h/s): ").lower()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("⚠️ Invalid choice. Enter 'h' or 's': ").lower()
                if choice in ["h", "hit"]:
                    player_hand.add_cards(deck.deal(1))
                    player_hand.display()

            # Check if player busted or got blackjack after hitting
            if self.check_winner(player_hand, dealer_hand):
                dealer_hand.display(show_all_dealer_cards=True)
                continue

            # Dealer's turn 🧑‍💼: dealer hits until value is at least 17
            while dealer_hand.get_value() < 17:
                dealer_hand.add_cards(deck.deal(1))

            dealer_hand.display(show_all_dealer_cards=True)  # Show all dealer cards

            # Check for winner after dealer's turn
            if self.check_winner(player_hand, dealer_hand):
                continue

            # 🧾 Final results: compare hand values
            print("📢 Final Results:")
            print("🧑 You:", player_hand.get_value())
            print("🧑‍💼 Dealer:", dealer_hand.get_value())
            self.check_winner(player_hand, dealer_hand, game_over=True)

        print("\n🎉 Thanks for playing! 🎉")

    # ✅ Determines the winner and prints result with emojis
    def check_winner(self, player_hand, dealer_hand, game_over=False):
        # If not final comparison, check for busts and blackjack
        if not game_over:
            if player_hand.get_value() > 21:
                print("💥 You busted! Dealer wins. 😢")
                return True
            elif dealer_hand.get_value() > 21:
                print("🔥 Dealer busted! You win! 🥳")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("🎯 Both have Blackjack! It's a tie! 🤝")
                return True
            elif player_hand.is_blackjack():
                print("🃏 Blackjack! You win! 🏆")
                return True
            elif dealer_hand.is_blackjack():
                print("🃏 Dealer has Blackjack! Dealer wins. 😤")
                return True
        else:
            # Final comparison after both turns
            if player_hand.get_value() > dealer_hand.get_value():
                print("🏆 You win the round! 💪")
            elif player_hand.get_value() < dealer_hand.get_value():
                print("😔 Dealer wins the round. Better luck next time!")
            else:
                print("🤝 It's a tie!")
        return False


# ▶️ Start the game
g = Game()
g.play()

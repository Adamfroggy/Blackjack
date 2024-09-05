import random


class Card:
    """
A class representing a playing card with a suit and rank.

Attributes:
    suit (str): The suit of the card (e.g., Spades, Hearts).
    rank (dict): A dictionary with the rank (name) and value of the card.
"""
    def __init__(self, suit, rank):
        """
        Initializes a Card object with the given suit and rank.

        Args:
            suit (str): The suit of the card.
            rank (dict): A dictionary with the rank name and
            its corresponding value.
        """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        Returns a string representation of the card.

        Returns:
            str: A formatted string displaying the rank and suit of the card.
        """
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    """
    A class representing a deck of playing cards.

    Attributes:
        cards (list): A list of Card objects representing the deck.
    """
    def __init__(self):
        """
        Initializes a deck with 52 cards, one for each combination
        of rank and suit.
        """
        self.cards = []
        suits = ["Spades", "Clubs", "Hearts", "Diamondes"]
        ranks = [
                {"rank": "Ace", "value": 11},
                {"rank": "2", "value": 2},
                {"rank": "3", "value": 3},
                {"rank": "4", "value": 4},
                {"rank": "5", "value": 5},
                {"rank": "6", "value": 6},
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9},
                {"rank": "10", "value": 10},
                {"rank": "Jack", "value": 10},
                {"rank": "Queen", "value": 10},
                {"rank": "King", "value": 10}]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """
        Shuffles the deck if there are more than 1 card in it.
        """
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        """
        Deals a specified number of cards from the deck.

        Args:
            number (int): The number of cards to deal.

        Returns:
            list: A list of Card objects dealt from the deck.
        """
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt


class Hand:
    """
    A class representing a hand of cards in a game.

    Attributes:
        card (list): A list of Card objects in the hand.
        value (int): The total value of the hand.
        dealer (bool): Indicates if this hand belongs to the dealer.
    """
    def __init__(self, dealer=False):
        """
        Initializes a Hand object.

        Args:
            dealer (bool): If True, indicates this hand belongs to the dealer.
        """
        self.card = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        """
        Adds a list of cards to the hand.

        Args:
            card_list (list): List of Card objects to be added to the hand.
        """
        self.card.extend(card_list)

    def calculate_value(self):
        """
        Calculates the total value of the hand, adjusting for
        the presence of Aces.
        """
        self.value = 0
        has_ace = False

        for card in self.card:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "Ace":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        """
        Returns the current value of the hand after recalculating.

        Returns:
            int: The total value of the hand.
        """
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        """
        Checks if the hand is a blackjack (total value of 21 with two cards).

        Returns:
            bool: True if the hand is a blackjack, False otherwise.
        """
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        """
        Displays the hand's cards and value.
        The dealer's first card can be hidden.

        Args:
            show_all_dealer_cards (bool): If False,
            the dealer's first card is hidden.
        """
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.card):
            if index == 0 and self.dealer and not show_all_dealer_cards \
                    and not self.is_blackjack():
                print("Card hidden")
            else:
                print(card)

        if not self.dealer:
            print("Value:", self.get_value())
        print()


class Game:
    """
    A class representing a game of Blackjack.

    Methods:
        play(): Starts and plays the specified number of Blackjack games.
        check_winner(): Checks the winner based on hand values and conditions.
    """
    def play(self):
        """
        Starts and plays a series of Blackjack games based on user input.
        Handles the game loop, dealing cards, and checking for winners.
        """
        game_number = 0
        games_to_play = 0

        # Ask the player how many games they want to play
        while games_to_play <= 0:
            try:
                games_to_play = int(input
                                    ("How many games do you want to play? "))
            except ValueError:
                print("You must enter a number.")

        # Game loop
        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            # Deal initial two cards to both player and dealer
            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            # Display hands
            player_hand.display()
            dealer_hand.display()

            # Check for an initial winner (blackjack or bust)
            if self.check_winner(player_hand, dealer_hand):
                continue

            # Player's turn: Hit or Stay
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stay"]:
                choice = input("Please choose 'Hit' or 'Stay': ").lower()
                print()
                while choice not in ["h", "s", "hit", "stay"]:
                    choice = input("Please enter 'Hit' or \
                                   'Stay' (or H/S) ").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            # Check for winner after player's turn
            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            # Dealer's turn
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(deck.deal(1))

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand, game_over=True):
                continue

            # Final result
            print("End Results...")
            print("Your hand:", player_hand_value)
            print("Dealers hand:", dealer_hand_value)

        print("\nThanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        """
        Checks the winner based on the current value of the player's and
        dealer's hands.

        Args:
            player_hand (Hand): The player's hand object.
            dealer_hand (Hand): The dealer's hand object.
            game_over (bool): If True, checks the final winner. If False,
            checks for blackjack or bust.

        Returns:
            bool: True if the game has ended (due to bust, blackjack, or
            comparison of values).
        """
        # Check conditions before the game is over (busts or blackjack)
        if not game_over:
            if player_hand.get_value() > 21:
                print("Bust! Dealer wins.")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You win!")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Tie game! Both got Blackjack.")
                return True
            elif player_hand.is_blackjack():
                print("Blackjack! You win!")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer got a Blackjack. You lose.")
                return True
        else:
            # When both player and dealer have finished drawing cards
            player_value = player_hand.get_value()
            dealer_value = dealer_hand.get_value()

            print(f"Your hand: {player_value}")
            print(f"Dealer's hand: {dealer_value}")

            if dealer_value > 21:
                print("Dealer busted. You win!")
                return True
            elif player_value > dealer_value:
                print("You win!")
            elif player_value == dealer_value:
                print("Tie game!")
            else:
                print("Dealer wins.")
            return True
        return False


g = Game()
g.play()

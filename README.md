# Blackjack Game

A simple text-based Blackjack game implemented in Python. This game simulates a classic Blackjack card game, where the player competes against the dealer to reach a hand value closest to 21 without exceeding it.

## Table of Contents
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## How to Play

1. At the start of the game, you will be dealt two cards, and the dealer will also get two cards (one card will be hidden).
2. You will be given the choice to either "Hit" (draw a card) or "Stay" (keep your current hand).
3. The goal is to have a hand with a value as close to 21 as possible without going over.
4. After your turn, the dealer will reveal their hidden card and draw cards until their hand's value is 17 or higher.
5. If your hand's value is closer to 21 than the dealer's or the dealer goes bust (exceeds 21), you win.

## Game Rules

- **Card Values**: 
  - Number cards (2-10) are worth their face value.
  - Face cards (Jack, Queen, King) are worth 10.
  - Aces can be worth 11 or 1, depending on which gives the best hand.
  
- **Blackjack**: A hand value of 21 with the first two cards (e.g., Ace + 10-value card) is a Blackjack. If both player and dealer have a Blackjack, the game is a tie.

- **Dealer Rules**: The dealer must draw cards until their hand totals 17 or more. If the dealer's hand exceeds 21, they go bust, and the player wins.

## Features

- Full deck shuffling and dealing mechanics.
- The player can choose to "Hit" or "Stay".
- Dealer automatically plays after the player's turn.
- Detects busts, Blackjack, and determines the winner based on hand values.

## Installation

To play the game on your local machine, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/Blackjack.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Blackjack
    ```

3. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. Install the required dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```

5. Run the game:
    ```bash
    python blackjack_game.py
    ```

## Usage

Once you run the game, you will be prompted to input how many games you would like to play. For each game, you can choose to either "Hit" (draw a card) or "Stay" (keep your hand). The goal is to reach a hand value as close to 21 as possible without going over.

Sample prompt:

Your hand: 8 of Spades 10 of Diamonds Value: 18

Dealer's hand: Card hidden 4 of Clubs

Please choose 'Hit' or 'Stay':


After each game, the results are shown, and you can play additional rounds if desired.

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please fork the repository and create a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
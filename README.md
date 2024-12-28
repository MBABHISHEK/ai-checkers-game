# AI Minimax Checkers

This project is a simple **Checkers** game where one player is human, and the other is controlled by an AI using the **Minimax algorithm**. The AI opponent makes moves based on a search tree, considering all possible moves, and picks the best one.

## Features:
- **Human vs AI Mode**: Play against an AI that uses the **Minimax algorithm** to determine the best moves.
- **AI Difficulty**: The AI's search depth is set to 3, but you can change this to increase/decrease difficulty.
- **Win Condition**: The game ends when one player wins, and a message is displayed showing the winner.
- **Graphical User Interface (GUI)**: The game is displayed on a window using the Pygame library, where the user can click to make their move.

## Requirements

To run the game, you will need:
- **Python 3.x** (recommended version: 3.7 or higher)
- **Pygame library** for creating the GUI.

You can install the required libraries by running the following command:
```bash
pip install pygame
Game Setup and Instructions
Clone or Download the Repository:
You can clone the repository or download the files directly to your local machine.

Run the Game:
After setting up the game, open the terminal/command prompt, navigate to the project folder, and run the following command:

bash
Copy code
python main.py
Playing the Game:

Click on a piece to select it, then click on an empty square to move it.
The game alternates between the human player and the AI.
The AI will move automatically after your turn.
The game will display a message when a player wins.
AI Algorithm:

The AI uses the Minimax algorithm to make decisions. It evaluates the game tree up to a depth of 3 to decide on the best move.
The AI makes the best move based on the current board state and ensures that it minimizes the opponent’s advantage.
Code Overview
main.py: Contains the main logic for the game. It handles user input, updating the board, checking for a winner, and displaying the winner message.
game.py: Implements the rules of the game, including the movement of pieces and determining the game's winner.
algorithm.py: Contains the Minimax algorithm, which the AI uses to make decisions.
constants.py: Defines the constants for board size, colors, and other configurations.
Main Components:
Game Logic: The Game class handles the mechanics of the checkers game, including piece movement, determining valid moves, and checking for a winner.

AI Move (Minimax): The minimax function analyzes the game tree and returns the optimal move for the AI based on the current state of the board.

Graphical Display:

The Pygame library is used for drawing the board, pieces, and displaying messages.
The window size, square size, colors, and fonts are configured in the constants file.
Winner Detection:

After each move, the game checks if a player has won. If a winner is detected, a message is displayed on the screen.
How to Play
Human Player (Red): Uses the mouse to select and move pieces.
AI Player (White): The AI will automatically make a move after the human player.
Notes:
The game allows the human player to play as Red and the AI plays as White.
The game will automatically display a winner after the game ends and wait for a few seconds before quitting.
Customizations
You can change the AI difficulty by adjusting the depth of the Minimax algorithm. A higher depth will make the AI stronger but will take more time to calculate.
Feel free to customize the appearance, such as adding images for the pieces or changing the board colors.

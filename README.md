Name: Oluwajomiloju Okuwobi  
UTA ID: 1002022767  

Project Title: Red-Blue Nim Game Using Minimax Search with Alpha-Beta Pruning  

Programming Language: Python 3.10.7  

## Code Structure

The project is organized into a single Python script file, `red_blue_nim.py`. This file contains two main classes and a `main()` function, structured as follows:

1. **Classes:**
   - **GameState**: Manages the game’s current state, including the number of red and blue marbles, available moves, and state evaluation.
     - `is_terminal()`: Checks if the game has reached an end state (when either pile is empty).
     - `get_possible_moves()`: Generates possible moves based on the pile counts, allowing a player to take 1 or 2 marbles from either pile.
     - `apply_move(move)`: Applies a selected move to transition to a new state.
     - `evaluate(player)`: Calculates the score based on the current player and game version (either maximizing or minimizing score).
   
   - **RedBlueNim**: Controls game flow, player turns, and the Minimax algorithm with alpha-beta pruning.
     - `play_game()`: Manages the game loop, printing the state, getting moves, and checking for a winner.
     - `minmax(state, alpha, beta, maximizing)`: Implements Minimax search with alpha-beta pruning to make efficient, optimal decisions.
     - `get_human_move()`: Prompts the human player to select a move from the list of available moves.
     - `print_game_state()` and `print_winner()`: Outputs the current game state and the game’s result.

2. **Main Function**:
   - The `main()` function parses command-line arguments for initial setup and starts the game.

## Running Instructions

### Requirements:
- Ensure Python 3.10.7 is installed. If using a different version, set up a virtual environment with Python 3.10.7 for compatibility.

### Command Format:

```bash
python red_blue_nim.py <num-red> <num-blue> <version> <first-player>

Game Logic and Strategy
This game applies Minimax search with alpha-beta pruning to make decisions, ensuring optimal play for the computer.

Game Setup and Rules
The game begins with two piles of red and blue marbles. Each turn, a player can pick 1 or 2 marbles from either pile. The objective is based on the chosen version:

Standard Version: The player forced to take the last marble loses.
Misère Version: The player forced to take the last marble wins.
Decision-Making and Strategy
Minimax Search with Alpha-Beta Pruning:
Minimax is a recursive algorithm used for decision-making in zero-sum games (like Nim) to minimize the possible loss in a worst-case scenario.
Alpha-Beta Pruning optimizes Minimax by eliminating branches that do not influence the final decision, thus reducing computational time.
Human and Computer Moves:
Each player alternates turns. The computer uses Minimax to find the optimal move to either maximize its advantage (in standard mode) or increase the likelihood of forcing a loss on the opponent (in misère mode).
Evaluation Function:
The evaluation function assigns a score to each game state, calculated based on the number of marbles remaining. If the game is in a terminal state, the score depends on the game version (standard or misère) and determines the winner.
Player Strategy:
In standard mode, a player tries to avoid the terminal state.
In misère mode, a player aims to reach a terminal state where the opponent is forced to take the last marble.
With this strategic setup, the game becomes a competition of skill, where the computer’s optimal moves provide a challenging opponent for the human player.


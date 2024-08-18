# Tic-Tac-Toe

This project implements a simple Tic-Tac-Toe game in Python, with a single-player mode against the computer. The computer randomly selects moves, making the game interesting and unpredictable.

## Files Description

- `script.py`: Contains the implementation of the Tic-Tac-Toe game.
- `game.py`: Main script to start the game.
- `test_game.py`: Contains unit tests to verify the game's functionality.


## Requirements

- Python 3.7 or higher
- [pytest](https://docs.pytest.org/en/stable/) for running tests (included in `requirements.txt`)


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/m-grande/tictactoe.git
    ```
2. Navigate to the project directory:
    ```bash
    cd tictactoe
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the game, run the following command:

```bash
python game.py
```
Follow the on-screen instructions to play against the computer. Enter the number corresponding to the cell where you want to make your move (1-9).

## Tests

The project includes a test suite to verify the correctness of the implemented features. To run the tests, use the following command:

```bash
pytest -v
```

## How the Code Works

`script.py`
The **TicTacToe** class is the backbone of this project, handling all aspects of the game, including:

- **Game Board Initialization**: The board is represented as a list of strings, initially numbered 1 through 9, representing each cell's position.
- **Player Moves**: The `make_move()` method allows players to select a cell on the board, updating the board state if the move is valid.
- **Computer Moves**: The `computer_move()` method randomly selects an available cell for the computer's move.
- **Winner Check**: The `check_winner()` method checks the board against predefined winning conditions (rows, columns, diagonals) to determine if there is a winner.
- **Draw Check**: The `check_draw()` method verifies if all cells are filled without any player winning, indicating a draw.
- **Player Switching**: The `player_switch_after_move()` method switches turns between the human player and the computer.

`game.py`
The **game.py** script serves as the entry point to the game. It creates an instance of the TicTacToe class and manages the flow of the game:

- It resets the board for each new game.
- It prompts the player for input and manages the computer's move.
- It checks for a winner or a draw after each move and handles the end-of-game scenarios.

`test_game.py`
This file includes a comprehensive set of unit tests for the Tic-Tac-Toe game:

- **Board Printing Test**: `test_print_board()` ensures the game board is displayed correctly.
- **Move Validation** Tests: `test_is_valid_move()` verifies that moves are only allowed in unoccupied cells.
- **Move Execution Tests**: `test_make_valid_move()` and `test_make_invalid_move()` check that moves are correctly executed and rejected if invalid.
- **Winning Condition Tests**: `test_horizontal_win()`, `test_vertical_win()`, and `test_diagonal_win()` confirm that the game correctly identifies winning conditions.
- **Draw Condition Tests**: `test_check_draw_with_draw()` and `test_check_draw_without_draw()` ensure the game correctly identifies when a draw occurs.
- **Computer Move Tests**: `test_computer_move_makes_valid_move()`, `test_computer_move_last_empty_cell()`, and `test_computer_move_no_empty_cells()` validate the computer's ability to make moves.
- **Game Reset and Player Switch Tests**: `test_reset_board()` and `test_player_switch_after_move()` check that the game resets correctly and that players alternate turns as expected.


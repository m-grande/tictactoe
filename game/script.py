import random


class TicTacToe:
    def __init__(self):
        # Initialize the game board with numbers 1-9 representing empty cells
        self.board = [str(i) for i in range(1, 10)]
        # Set the starting player to "X" (the human player)
        self.current_player = "X"

    def print_board(self):
        # Print the current state of the board
        print(f"{self.board[0]}|{self.board[1]}|{self.board[2]}")
        print("-+-+-")
        print(f"{self.board[3]}|{self.board[4]}|{self.board[5]}")
        print("-+-+-")
        print(f"{self.board[6]}|{self.board[7]}|{self.board[8]}")

    def is_valid_move(self, move):
        return self.board[move - 1] not in ["X", "O"]

    def make_move(self, move):
        if self.is_valid_move(move):
            self.board[move - 1] = self.current_player
            return True
        return False

    def check_winner(self):
        # Define winning conditions (rows, columns, and diagonals)
        win_conditions = [
            (0, 1, 2),  # Top row
            (3, 4, 5),  # Middle row
            (6, 7, 8),  # Bottom row
            (0, 3, 6),  # Left column
            (1, 4, 7),  # Center column
            (2, 5, 8),  # Right column
            (0, 4, 8),  # Top-left to bottom-right diagonal
            (2, 4, 6),  # Top-right to bottom-left diagonal
        ]

        # Check each winning condition
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]  # Return the winner ("X" or "O")
        return None  # Return None if there is no winner yet

    def check_draw(self):
        # Check if the board is full and there are no empty cells
        return all(cell in ["X", "O"] for cell in self.board)

    def computer_move(self):
        # Determine the list of empty cells
        empty_cells = [i for i, x in enumerate(self.board) if x not in ["X", "O"]]

        if empty_cells:
            # Randomly choose an empty cell for the computer's move
            move = random.choice(empty_cells) + 1
            self.board[move - 1] = "O"
            print(f"Computer chose {move}")

    def reset_board(self):
        # Reset the board to its initial state and the current player to "X"
        self.board = [str(i) for i in range(1, 10)]
        self.current_player = "X"

    def player_switch_after_move(self):
        # Switch the current player from "X" to "O" or from "O" to "X"
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def play(self):
        # Main game loop
        while True:
            self.reset_board()  # Reset the board for a new game
            while True:
                self.print_board()

                if self.current_player == "X":
                    try:
                        move = int(input("Enter your move (1-9): "))
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 9.")
                        continue

                    if move < 1 or move > 9 or not self.make_move(move):
                        print("Invalid move. Try again.")
                        continue
                else:
                    # Computer's turn
                    self.computer_move()

                # Check for a winner
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    print(f"Player {winner} wins!")
                    break

                # Check for a draw
                if self.check_draw():
                    self.print_board()
                    print("It's a draw!")
                    break

                # Switch player
                self.player_switch_after_move()

            # Ask if the user wants to play another game
            play_again = None

            while play_again not in ["y", "n"]:
                play_again = input("Do you want to play again? (y/n): ").strip().lower()
                if play_again not in ["y", "n"]:
                    print("Invalid input. Please enter 'y' or 'n'")

            if play_again == "n":
                print("Thanks for playing!")
                break

import pytest

from game.script import TicTacToe


@pytest.fixture
def game():
    # Fixture that initializes a new TicTacToe game instance for testing
    return TicTacToe()


def test_print_board(game, capsys):
    # Call the print_board method to display the current state of the board
    game.print_board()

    # Capture the printed output using the capsys fixture
    captured = capsys.readouterr()

    # Define the expected output format of the board in a string representation
    expected_output = "1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n"

    # Assert that the captured output matches the expected output
    assert captured.out == expected_output


def test_is_valid_move(game):
    # Verify that all board positions are initially valid
    assert game.is_valid_move(1)  # Position 1 should be free
    assert game.is_valid_move(5)  # Position 5 should be free
    assert game.is_valid_move(9)  # Position 9 should be free

    # Make a move in position 1 to test if the position becomes invalid
    game.board[0] = "X"

    # Test that the occupied position 1 is no longer valid
    assert not game.is_valid_move(1)  # Position 1 is now occupied
    # Test that other positions are still valid
    assert game.is_valid_move(2)  # Position 2 should still be free

    # Test that other positions are still valid
    game.board[1] = "O"

    # Test that the occupied position 2 is no longer valid
    assert not game.is_valid_move(2)  # Position 2 is now occupied
    # Test that other positions are still valid
    assert game.is_valid_move(3)  # Position 3 should still be free


def test_make_valid_move(game):
    # Test that a valid move updates the board and switches the current player
    move = 1
    success = game.make_move(move)

    # Verify that the move was successful
    assert success

    # Verify that the board has been updated with the current player's move
    assert game.board[move - 1] == game.current_player

    # Verify that the current player has been switched to the opponent (assuming it changes after a move)
    assert game.current_player == "X"  # Update this if the current player changes after a move


def test_make_invalid_move(game):
    # Test that an invalid move (to an already occupied position) is not successful
    game.board[0] = "X"  # Occupy position 1
    move = 1
    success = game.make_move(move)

    # Verify that the move was unsuccessful
    assert not success

    # Verify that the board remains unchanged after the failed move
    assert game.board[0] == "X"


def test_horizontal_win(game):
    # Test horizontal win scenarios for each row

    # Test a win in the 1st row
    game.board = ["X", "X", "X", "4", "5", "6", "7", "8", "9"]
    winner = game.check_winner()
    assert winner == "X"
    assert not game.check_draw()

    # Test a win in the 2nd row
    game.board = ["1", "2", "3", "X", "X", "X", "7", "8", "9"]
    winner = game.check_winner()
    assert winner == "X"
    assert not game.check_draw()

    # Test a win in the 3rd row
    game.board = ["1", "2", "3", "4", "5", "6", "X", "X", "X"]
    winner = game.check_winner()
    assert winner == "X"
    assert not game.check_draw()


def test_vertical_win(game):
    # Test vertical win scenarios for each column

    # Test a win in the 1st column
    game.board = ["X", "2", "3", "X", "5", "6", "X", "8", "9"]
    winner = game.check_winner()
    assert winner == "X"
    assert not game.check_draw()

    # Test a win in the 2nd column
    game.board = ["1", "X", "3", "4", "X", "6", "7", "X", "9"]
    winner = game.check_winner()
    assert winner == "X"
    assert not game.check_draw()

    # Test a win in the 3rd column
    game.board = ["1", "2", "X", "4", "5", "X", "7", "8", "X"]
    winner = game.check_winner()
    assert winner == "X"
    assert not game.check_draw()


def test_diagonal_win(game):
    # Test diagonal win scenarios

    # Test a win from top-left to bottom-right
    game.board = ["X", "2", "3", "4", "X", "6", "7", "8", "X"]
    winner = game.check_winner()
    assert winner == "X"
    assert not game.check_draw()

    # Test a win from top-right to bottom-left
    game.board = ["1", "2", "X", "4", "X", "6", "X", "8", "9"]
    winner = game.check_winner()
    assert winner == "X"
    assert not game.check_draw()


def test_no_winner(game):
    # Test the scenario where no player has won yet
    game.board = ["X", "O", "X", "4", "5", "O", "7", "O", "9"]
    winner = game.check_winner()
    assert winner is None


def test_check_draw_with_draw(game):
    # Test the scenario where the board is completely filled, resulting in a draw
    game.board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    is_draw = game.check_draw()
    assert is_draw
    assert game.check_winner() not in ["X", "O"]


def test_check_draw_without_draw(game):
    # Test the scenario where the board is not completely filled, so no draw
    game.board = ["X", "O", "X", "X", "5", "O", "O", "X", "9"]
    is_draw = game.check_draw()
    assert not is_draw


def test_check_draw_empty_board(game):
    # Test the scenario where the board is completely empty, so no draw
    game.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    is_draw = game.check_draw()
    assert not is_draw


def test_computer_move_makes_valid_move(game, mocker):
    # Test that the computer makes a valid move on a partially filled board
    game.board = ["X", "2", "X", "4", "O", "6", "O", "X", "9"]

    # Mock random.choice to control the computer's move
    mocker.patch("random.choice", return_value=1)  # Mock the random.choice to control the move
    game.computer_move()

    # Verify that the computer made a move in the expected position
    assert game.board[1] == "O"  # Position 2 on the board (index 1) should now be "O"


def test_computer_move_last_empty_cell(game, mocker):
    # Test that the computer correctly chooses the last empty cell
    game.board = ["X", "O", "X", "O", "X", "O", "O", "X", "9"]

    # Mock random.choice to pick the last empty cell
    mocker.patch("random.choice", return_value=8)  # Mock to pick the last empty cell
    game.computer_move()

    # Verify that the computer made a move in the last empty cell
    assert game.board[8] == "O"  # Position 9 on the board (index 8) should now be "O"


def test_computer_move_on_empty_board(game, mocker):
    # Test that the computer can choose any position on an empty board
    game.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Mock random.choice to pick a specific position
    mocker.patch("random.choice", return_value=4)  # Mock to pick position 5
    game.computer_move()

    # Verify that the computer made a move in the chosen position
    assert game.board[4] == "O"  # Position 5 on the board (index 4) should now be "O"


def test_computer_move_no_empty_cells(game):
    # Test that the computer cannot move when no cells are empty
    game.board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
    previous_board = game.board.copy()
    game.computer_move()

    # Verify that the board remains unchanged when no empty cells are available
    assert game.board == previous_board  # Board should remain unchanged


def test_reset_board(game):
    # Test that the board and current player are correctly reset
    game.board = ["X", "O", "X", "4", "5", "O", "7", "X", "O"]
    game.current_player = "O"

    # Call the reset_board method to reset the game
    game.reset_board()

    # Verify that the board has been reset to its initial state
    assert game.board == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Verify that the current player has been reset to "X"
    assert game.current_player == "X"


def test_player_switch_after_move(game):
    # Test that the player switches correctly after a move
    game.make_move(1)

    # Call the method to switch players
    game.player_switch_after_move()

    # Verify that the player has switched to "O"
    assert game.current_player == "O"

    # Call the method again to switch players back
    game.player_switch_after_move()

    # Verify that the player has switched back to "X"
    assert game.current_player == "X"

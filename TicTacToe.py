def print_board(board):
    """Function to print the Tic-Tac-Toe board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    """Function to check if the player has won."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)


def is_draw(board):
    """Function to check if the game is a draw."""
    return all(space in ["X", "O"] for space in board)


def play_game():
    """Main function to run the Tic-Tac-Toe game."""
    board = [str(i+1) for i in range(9)]  # Initialize board with numbers 1-9
    current_player = "X"

    while True:
        print_board(board)

        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] in ["X", "O"]:
                print("Invalid move! That spot is already taken.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        board[move] = current_player  # Update board with player's move

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()

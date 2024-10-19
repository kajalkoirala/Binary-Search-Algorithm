import random

#print the board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

#check for a winner
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # for  Horizontal wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # for Vertical wins
        [0, 4, 8], [2, 4, 6]  # for  Diagonal wins
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

#check if the board is full or the game is being drawn
def check_draw(board):
    return all(space != " " for space in board)

#computer's move
def computer_move(board):
    available_moves = [i for i in range(9) if board[i] == " "]
    return random.choice(available_moves)

# Main function
def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    print("Choose mode: ")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    
    mode = input("Enter 1 or 2: ").strip()
    
    while mode not in ['1', '2']:
        mode = input("Invalid choice ").strip()

    board = [" "] * 9  # 9 empty spaces for the board
    current_player = "X"

    while True:
        print_board(board)
        
        if current_player == "X" or mode == '1':
            # Player's turn
            try:
                move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
                if board[move] == " ":
                    board[move] = current_player
                else:
                    print("That spot is already taken, try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input, please choose a number between 1 and 9.")
                continue
        else:
            # Computer's turn 
            print("Computer's turn")
            move = computer_move(board)
            board[move] = "O"

        # Check for a win
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    tic_tac_toe()

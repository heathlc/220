"""
Name: Lydia Heath
lab10.py
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def display_board(board):
    counter = 0
    print("-" * 13)
    for i in range(3):
        print("| ", end="")
        for j in range(3):
            print(board[counter], end=" | ")
            counter = counter + 1
        print("\n")
    print("-" * 13)


def fill_spot(board, spot, marker):
    board[spot - 1] = marker


def legal_spot(board, spot):
    if (board[spot - 1] == "x" or board[spot - 1] == "o") or (spot < 1 or spot > 9):
        return False
    else:
        return True


def game_won(board):
    win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                      [1, 4, 7], [2, 5, 8], [3, 6, 9],
                      [1, 5, 9], [3, 5, 7]]
    for condition in win_conditions:
        counter = 0
        for spot in condition:
            if board[spot - 1] == "x":
                counter = counter + 1
            if counter == 3:
                return "x wins"
    for condition in win_conditions:
        counter = 0
        for spot in condition:
            if board[spot - 1] == "o":
                counter = counter + 1
            if counter == 3:
                return "o wins"


def game_over(turn_count, board):
    if (game_won(board) == "x wins" or game_won(board) == "o wins") or (turn_count > 9):
        return True
    else:
        return False


def play_game():
    board = build_board()
    display_board(build_board())
    turn_count = 1
    while not game_over(turn_count, board):
        player = input("Who is playing [x or o]: ")
        if player == "x":
            x_spot = eval(input("Enter the spot you would like to place your mark: "))
            if legal_spot(board, x_spot):
                fill_spot(board, x_spot, "x")
                display_board(board)
                turn_count = turn_count + 1
                if game_won(board) == "x wins":
                    print("X wins!")
                if game_won(board) == "o wins":
                    print("O wins!")
        if player == "o":
            o_spot = eval(input("Enter the spot you would like to place your mark: "))
            if legal_spot(board, o_spot):
                fill_spot(board, o_spot, "o")
                display_board(board)
                turn_count = turn_count + 1
                if game_won(board) == "x wins":
                    print("X wins!")
                if game_won(board) == "o wins":
                    print("O wins!")
    if turn_count > 9:
        print("Tie")


def main():
    play_game()


main()

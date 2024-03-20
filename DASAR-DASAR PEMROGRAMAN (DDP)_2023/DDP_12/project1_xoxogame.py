def print_board(board):
    print('\n'.join([''.join(row) for row in board]))

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board)):
        check_col = []
        for row in board:
            check_col.append(row[col])
        if check_col.count(check_col[0]) == len(check_col) and check_col[0] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        print(f"Player {player}, make your move.")
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))

        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()
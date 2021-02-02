def print_board(board):
    row = 2
    while row >= 0:
        for j in range(3):
            if board[row*3+j] == '#':
                continue
            else:
                print(board[row*3+j].upper())





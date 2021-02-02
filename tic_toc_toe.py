def print_board(board):
    row = 2
    while row >= 0:
        for j in range(3):
            if board[row*3+j] == '#':
                continue
            else:
                print(board[row*3+j].upper())
def check_if_one_player_win(board, number_selected):
    row = int(number_selected/3)
    col = int(number_selected%3)
    for i in range(2):
        if (board[row*3+i]) != (board[row*3 + i + 1]):
            break
    else:
        return True
    for i in range(2):
        if(board[i*3+col])!=(board[i*3+col+1]):
            break
    else:
        return True
    if row == col:
        for i in range(2):
                if(board[i][i])!=(board[i+1][i+1]):
                    break
        else:
            return True
    if row==col:
        for i in range(2):
            if(board[i][2-i]) != (board[i+1][1-i]):
                break
        else:
            return True
    return False
def game_initialization():



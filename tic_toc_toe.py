def print_board(board):
    print(f'{board[6]}{board[7]}{board[8]}\n{board[3]}{board[4]}{board[5]}\n{board[0]}{board[1]}{board[2]}')


def check_if_one_player_win(board, number_selected):
    row = int(number_selected / 3)
    col = int(number_selected % 3)
    for i in range(2):
        if (board[row * 3 + i]) != (board[row * 3 + i + 1]):
            break
    else:
        return True
    for i in range(2):
        if (board[i * 3 + col]) != (board[(i + 1) * 3 + col]):
            break
    else:
        return True
    if row == col:
        for i in range(2):
            if (board[i * 3 + i]) != (board[(i + 1) * 3 + i + 1]):
                break
        else:
            return True
    if row + col == 2:
        for i in range(2):
            if (board[i * 3 + 2 - i]) != (board[(i + 1) * 3 + 1 - i]):
                break
        else:
            return True
    return False


def check_validity(player_number, board):
    if board[player_number - 1] != '#':
        return False
    else:
        return True


def one_loop_of_game(player_turn, board, player_symbol):
    x = int(input('hey player' + str(player_turn) + ' please choose a position: '))
    while not (check_validity(x, board)):
        print('that position is already selected')
        x = int(input('hey player' + str(player_turn) + ' please choose a position: '))
    if player_symbol == 'X':
        board[x - 1] = 'X'
    else:
        board[x - 1] = 'O'
    print_board(board)
    return x - 1


def game():
    player1_symbol = str(input('Hello player1 please choose X or O?')).upper()
    if player1_symbol == 'O':
        player2_symbol = 'X'
    else:
        player2_symbol = 'O'
    board = ['#'] * 9
    player_turn = 1
    player_symbol = player1_symbol
    counter = 0
    while not check_if_one_player_win(board, one_loop_of_game(player_turn, board, player_symbol)):
        player_turn = 3 - player_turn
        if player_symbol == player1_symbol:
            player_symbol = player2_symbol
        else:
            player_symbol = player1_symbol
        counter += 1
        if counter == 9:
            break
    else:
        print('player' + str(player_turn) + ' won the game')
        return
    print("the game is draw")

game()

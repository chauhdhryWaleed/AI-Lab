def initial_state():
    board = [['','',''], ['','',''], ['','','']]
    return board


def actions(board):
    moves = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '':
                moves.append((i, j))
    return moves


def player(board):
    countX = 0
    count0 = 0
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == "X":
                countX += 1
            if board[i][j] == "0":
                count0 += 1
    if countX == count0:
        return "X"
    else:
        return "0"


def result(board, action):
    move = player(board)
    new_board=[]

    for i in range(0,3):
        for j in range(0,3):
            new_board[i][j]=board[i][j]

    new_board[action[0]][action[1]] = move
    return new_board


def winner(board):
    if board[0][0] == "X":
        if board[0][1] == "X":
            if board[0][2] == "X":
                return "X"
        elif board[1][0] == "X":
            if board[2, 0] == "X":
                return "X"
        elif board[1][1] == "X":
            if board[2][2] == "X":
                return "X"
    elif board[1][1] == "X":
        if board[0][1] == "X":
            if board[2][1] == "X":
                return "X"
        if board[1][0] == "X":
            if board[1][2] == "X":
                return "X"
        if board[0][2] == "X":
            if board[2][0] == "X":
                return "X"
    elif board[2][2] == "X":
        if board[1][2] == "X":
            if board[0][2] == "X":
                return "X"
        if board[2][0] == "X":
            if board[2][1] == "X":
                return "X"
    elif board[0][0] == "0":
        if board[0][1] == "0":
            if board[0][2] == "0":
                return "0"
        elif board[1][0] == "0":
            if board[2, 0] == "0":
                return "0"
        elif board[1][1] == "0":
            if board[2][2] == "0":
                return "0"
    elif board[1][1] == "0":
        if board[0][1] == "0":
            if board[2][1] == "0":
                return "0"
        if board[1][0] == "0":
            if board[1][2] == "0":
                return "0"
        if board[0][2] == "0":
            if board[2][0] == "0":
                return "0"
    elif board[2][2] == "0":
        if board[1][2] == "0":
            if board[0][2] == "0":
                return "0"
        if board[2][0] == "0":
            if board[2][1] == "0":
                return "0"
    else:
        return None


def terminal(board):
    if winner(board) is None:
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] == "":
                    return False
    else:
        return True


def utility(board):
    if winner(board) is None:
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] == "":
                    return 2
        return 0
    if winner(board) == "X":
        return 1
    elif winner(board) == "0":
        return -1

def min(board):
    moves=actions(board)

    print(moves)


def max(board):
    print("hello")

board=initial_state()
move = actions(board)
min(board)
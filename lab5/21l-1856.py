# Python3 implementation of the
from random import randint

N = 4


# A utility function that configures the 2D array "board" and array "state" randomly to provide a starting point for the algorithm.
def configureRandomly(board, state):
    # Iterating through the column indices
    for i in range(N):
        # Getting a random row index
        state[i] = randint(0, 100000) % N;

        # Placing a queen on the obtained place in chessboard.
        board[state[i]][i] = 1;


# A utility function that prints the 2D array "board".
def printBoard(board):
    for i in range(N):
        print(*board[i])


# A utility function that prints the array "state".
def printState(state):
    print(*state)


# A utility function that compares two arrays, state1 and state2 and returns True if equal and False otherwise.
def compareStates(state1, state2):
    for i in range(N):
        if (state1[i] != state2[i]):
            return False;

    return True;


# A utility function that fills the 2D array "board" with values "value"
def fill(board, value):
    for i in range(N):
        for j in range(N):
            board[i][j] = value;
        # This function calculates the objective value of the state(queens attacking each other) using the board by the following logic.


def calculateObjective(board, state):
    # For each queen in a column, we check for other queens falling in the line of our current queen and if found,
    # any, then we increment the variable attacking count. Number of queens attacking each other, initially zero.
    attacking = 0;

    # Variables to index a particular
    # row and column on board.
    for i in range(N):

        # At each column 'i', the queen is placed at row 'state[i]', by the definition of our state.

        # To the left of same row(row remains constant and col decreases)
        row = state[i]
        col = i - 1;
        while (col >= 0 and board[row][col] != 1):
            col -= 1

        if (col >= 0 and board[row][col] == 1):
            attacking += 1;

        # To the right of same row (row remains constant and col increases)
        row = state[i]
        col = i + 1;
        while (col < N and board[row][col] != 1):
            col += 1;

        if (col < N and board[row][col] == 1):
            attacking += 1;

        # Diagonally to the left up (row and col simultaneously decrease)
        row = state[i] - 1
        col = i - 1;
        while (col >= 0 and row >= 0 and board[row][col] != 1):
            col -= 1;
            row -= 1;

        if (col >= 0 and row >= 0 and board[row][col] == 1):
            attacking += 1;

        # Diagonally to the right down (row and col simultaneously increase)
        row = state[i] + 1
        col = i + 1;
        while (col < N and row < N and board[row][col] != 1):
            col += 1;
            row += 1;

        if (col < N and row < N and board[row][col] == 1):
            attacking += 1;

        # Diagonally to the left down (col decreases and row increases)
        row = state[i] + 1
        col = i - 1;
        while (col >= 0 and row < N and board[row][col] != 1):
            col -= 1;
            row += 1;

        if (col >= 0 and row < N and board[row][col] == 1):
            attacking += 1;

        # Diagonally to the right up (col increases and row decreases)
        row = state[i] - 1
        col = i + 1;
        while (col < N and row >= 0 and board[row][col] != 1):
            col += 1;
            row -= 1;

        if (col < N and row >= 0 and board[row][col] == 1):
            attacking += 1;

    # Return pairs.
    return int(attacking / 2);


# A utility function that generates a board configuration given the state.
def generateBoard(board, state):
    fill(board, 0);
    for i in range(N):
        board[state[i]][i] = 1;


# A utility function that copies contents of state2 to state1.
def copyState(state1, state2):
    for i in range(N):
        state1[i] = state2[i];
    # This function gets the neighbour of the current state having the least objective value amongst all neighbours as well as the current state.


def getNeighbour(board, state):
    neighbour_state = state.copy()

    # Select a random column
    col = randint(0, N - 1)

    neighbour_state[col] = randint(0, N - 1)

    return neighbour_state


def hillClimbing(board, state):
    current_state = state.copy()
    while True:
        best_neighbour_state = None
        best_neighbour_value = float('inf')

        # Iterate through each column
        for col in range(N):

            for row in range(N):
                neighbour_state = current_state.copy()
                neighbour_state[col] = row

                neighbour_value = calculateObjective(board, neighbour_state)

                if neighbour_value < best_neighbour_value:
                    best_neighbour_value = neighbour_value
                    best_neighbour_state = neighbour_state

        if best_neighbour_value >= calculateObjective(board, current_state):
            break

        current_state = best_neighbour_state

    return current_state


def printPositions(state):
    print("The Position of queens are:")
    for i in range(N):
        print(f"{i + 1} - {{{i + 1}, {state[i] + 1}}}")


# Driver code
state = [0] * N
board = [[0 for _ in range(N)] for _ in range(N)]
configureRandomly(board, state);
final_state = hillClimbing(board, state);
generateBoard(board, final_state)
printBoard(board)
printPositions(final_state)

"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x, count_o = 0, 0
    for row in board:
        count_x += row.count(X)
        count_o += row.count(O)

    if count_x <= count_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for ri, r in enumerate(board):
        for ci, item in enumerate(r):
            if item == EMPTY:
                possible_moves.add((ri, ci))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception
    else:
        new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for plyer in (X, O):
        for row in board:
            if row == [plyer] * 3:
                return plyer

        for i in range(3):
            col = [board[x][i] for x in range(3)]
            if col == [plyer] * 3:
                return plyer

        if [board[i][i] for i in range(0, 3)] == [plyer] * 3:
            return plyer
        elif [board[i][~i] for i in range(0, 3)] == [plyer] * 3:
            return plyer

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -5
            for action in actions(board):
                minval = min_value(result(board, action))[0]
                if minval > v:
                    v = minval
                    optimal_move = action
            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 5
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < v:
                    v = maxval
                    optimal_move = action
            return v, optimal_move

    if terminal(board):
        return None

    if player(board) == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]

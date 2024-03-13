"""
Tic Tac Toe Player
"""

import math
import copy

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
    # since X is first, if O count is not equal to X count, its Os turn
    x_count = 0
    o_count = 0
    for row in board:
        for item in row:
            if item == X:
                x_count += 1
            elif item == O:
                o_count += 1

    if x_count != o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item is None:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a valid action.")
    elif terminal(board):
        raise Exception("Game Over")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        #checking row match
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]

        #checking column match
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    # diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or len(actions(board)) == 0:
        return True 
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    if game_winner is None:
        return 0
    elif game_winner == O:
        return -1
    elif game_winner == X:
        return 1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            optimal_action = None
            v = float("-inf")
            for action in actions(board):
                min_val = min_value(result(board, action))
                if min_val > v:
                    v = min_val
                    optimal_action = action
        else:
            optimal_action = None
            v = float("inf")
            for action in actions(board):
                max_val = max_value(result(board, action))
                if max_val < v:
                    v = max_val
                    optimal_action = action
        return optimal_action


def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
 
    return v

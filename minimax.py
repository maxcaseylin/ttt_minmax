import game
import copy
import sys

#created an evaluation function using minimax.
#usage: create a GameNode() with the initial board and "X" to play,
# then call minimax() with the node and player to use.
# 0 means the position evals to a tie with best play, 1 if X wins, 2 if Y wins

class GameNode():
    def __init__(self, board, move, player):
        self.evaluation = 0
        self.move = move
        self.board = board
        self.positions = board.gen_moves(player)

init_board = game.Board()

initial_node = GameNode(init_board, "", "X")



def game_eval(board):
    if board.check_winner() == 1:
        return 1
    elif board.check_winner() == 2:
        return -1
    else:
        return 0

def is_terminal_state(board):
    if board.check_winner() == 1 or board.check_winner() == 2:
        return True
    elif board.gen_moves("X") == []:
        return True
    else:
        return False

def minimax(node, player):
    #generate game tree
    if is_terminal_state(node.board):
        return game_eval(node.board)
    if player == "X":
        #print(node.positions)
        value = -100000
        for pos in node.positions:
            new_board = copy.deepcopy(node.board)
            new_board.make_move(pos)
            value = max(value, minimax(GameNode(new_board, pos, "Y"), "Y"))
        return value
    else:
        value = 100000
        for pos in node.positions:
            new_board = copy.deepcopy(node.board)
            new_board.make_move(pos)
            value = min(value, minimax(GameNode(new_board, pos, "X"), "X"))
        return value


# print(minimax(initial_node, "X"))       

# test_board1 = game.Board()
# test_board1.board = [
#     [1,0,2],
#     [0,1,2],
#     [0,0,0]
# ]
# test1 = GameNode(test_board1, "", "X")
# print(test1.board.check_winner())
# print(is_terminal_state(test1.board))

# print(minimax(test1, "X"))       
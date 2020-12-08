import game
import copy
import minimax as m
import re

#small implementation - play with ai



def gen_best_move(board, player):
    #create a gameNode with the board
    eval_pos = m.GameNode(board, "", player)
    pot_positions = eval_pos.positions
    evaluations = []
    for p in pot_positions:
        temp_pos = copy.deepcopy(eval_pos.board.board)
        new_board = game.Board()
        new_board.board = temp_pos
        new_board.make_move(p)
        #print(p)
        #print(eval_pos)
        #print(new_board.board)
        #create new gameNode
        new_node = m.GameNode(copy.deepcopy(new_board), p,"Y" if player == "X" else "X")
        #print(new_node.board)
        #print(new_node.positions)
        temp_eval = m.minimax(new_node, "Y" if player == "X" else "X")
        #print(temp_eval)
        evaluations.append(temp_eval)
    
    #go through the list, find the first best move, and then play it
    #keep a move that keeps parity
    #if all moves are losing just pick a random move
    #print(pot_positions)
    #print(evaluations)
    keep_parity_move = None
    if player == "X":
        for i in range(0, len(evaluations)):
            if evaluations[i] == 0:
                keep_parity_move = pot_positions[i]
            elif evaluations[i] == 1:
                return pot_positions[i]
    else:
        for i in range(0, len(evaluations)):
            if evaluations[i] == 0:
                keep_parity_move = pot_positions[i]
            elif evaluations[i] == -1:
                return pot_positions[i]
    if keep_parity_move == None:
        return pot_positions[0]
    else:
        return keep_parity_move



def main():
    #print(gen_best_move(game_board, "X"))
    #initialize actual Game Board + other variables
    game_board = game.Board()
    exit_game = "N"
    while exit_game == "N":
        player = ""
        while player != "X" and player != "Y":
            player = input("Player: X or Y?").upper()
        
        if player == "X":
            while not m.is_terminal_state(game_board):
                print("board: ")
                print(game_board)
                hmove = ""
                while not bool(re.match(r"X@[1-3]( )*,( )*[1-3]", hmove)):
                    hmove = input("make a move: format: X@ROW,COL ")
                game_board.make_move(hmove)

                if(m.is_terminal_state(game_board)):
                    break

                cmove = gen_best_move(game_board, "Y")
                print("computer move: " + cmove)
                game_board.make_move(cmove)
                print(game_board)       
            
        else:
            while not m.is_terminal_state(game_board):
                print("board: ")
                print(game_board)
                

                cmove = gen_best_move(game_board, "X")
                print("computer move: " + cmove)
                game_board.make_move(cmove)
                print(game_board)  

                if(m.is_terminal_state(game_board)):
                    break

                hmove = ""
                while not bool(re.match(r"Y@[1-3]( )*,( )*[1-3]", hmove)):
                    hmove = input("make a move: format: Y@ROW,COL ")
                game_board.make_move(hmove) 

        if m.game_eval(game_board) == 1:
            print("X wins")
        elif m.game_eval(game_board) == -1:
            print("Y wins")
        else:
            print("tie")
        print(game_board)
        

        exit_game = input("exit: y(es) or n(o)?").upper()[0]

main()
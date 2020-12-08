import re

class Board:
    board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    char_map = {
        0: ".",
        1: "X",
        2: "Y"
    }

    def __str__(self):
        output = ""
        for i in range(0, 3):
            for j in range(0, 3):
                output = output + " " + self.char_map[self.board[i][j]] + " "
            output += "\n"

        return output;

    def check_winner(self):
        #check diagonals
        diagonalWinner = (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board [2][2]) or (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board [2][0])
        if diagonalWinner:
            if self.board[1][1] == 1:
                return 1
            elif self.board[1][1] == 2:
                return 2
        
        horizontalWinner = False
        verticalWinner = False
        for i in range(0, 3):
            
            horizontalWinner = (self.board[i][0] == self.board[i][1]) and (self.board[i][1] == self.board[i][2])
            verticalWinner = (self.board[0][i] == self.board[1][i]) and (self.board[1][i] == self.board[2][i])
            
            if horizontalWinner:
                if self.board[i][1] == 1:
                    return 1
                elif self.board[i][1] == 2:
                    return 2

            if verticalWinner:
                if self.board[1][i] == 1:
                    return 1
                elif self.board[1][i] == 2:
                    return 2
        
        return 0
    
    #move format: char@X,Y where
    #
    #  Y 1 2 3
    #  
    #  X 
    #  1
    #  2
    #  3
    #
    def make_move(self, move):
        m = re.split(",|@| ", move)
        m = [x for x in m if x != ""]
        self.board[int(m[1]) - 1][int(m[2]) - 1] = 1 if m[0] == "X" else 2
    
    def gen_moves(self, player):
        #we use the naive approach, iterate over every element and check if 0, then return array of all potential moves
        output = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == 0:
                    output.append("{}@ {}, {}".format(player, i+1, j+1))
        return output

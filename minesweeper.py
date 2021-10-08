import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        #helper function make_board to create board and plant bombs
        self.board = self.make_board()
        #assigns values to the board abot the bombs in neighbouring squares
        self.assign_val()
        #set to keep record of the places already dug
        self.dug = set() #if we dig at 0,0 then self.dug = {(0,0)}
    
    def make_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        #planting bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0,self.dim_size**2 - 1) #random loaction from 0-99
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue
            else:
                board[row][col] = '*'
                bombs_planted +=1
            
        return board

    def assign_val(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighbouring_bombs(r,c)
    
    def get_num_neighbouring_bombs(self,row,col):
        num_bombs =0
        for r in range( max(0,row-1), min(self.dim_size - 1, row +1 ) +1 ): #######
            for c in range ( max(0,col-1), min(self.dim_size - 1, col+1 ) +1 ):  ######
                if r==row and c==col:
                    continue
                if self.board[r][c] == '*':
                    num_bombs +=1

        return num_bombs

    def dig(self, row, col):
        #dig at a location
        # return true on successful dig and false if a bomb is dug
        
        #few scenarios 
        # hit a bomb --> GAME OVER
        # dig at location with neighouring bombs --> finish dig
        # dig at location with no neighbouring bombs --> recursively dig neighbours

        self.dug.add((row,col)) # to keep track of locations 

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        for r in range( max(0,row-1), min(self.dim_size - 1, row + 1) + 1 ): #######
            for c in range ( max(0,col-1), min(self.dim_size - 1, col + 1) + 1):  ######
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)
        return True
        
    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        s='    '
        s +='   ' +'   '.join(str(i) for i in range(self.dim_size))+'\n'
        for r in range(self.dim_size):
            s +=f'   {r}'
            for c in range(self.dim_size):
                s +=f'|  {visible_board[r][c]}'
            s +='|\n'

        return s

      
        
        



def play(dim_size = 10, num_bombs = 10):
    
    #create board 
    board  =  Board(dim_size, num_bombs)
    
    #show user board and ask them where to dig


    #if loaction is a bomb GAME OVER
    #if location is not bomb dig recursively until each square is atleast next to a bomb
    #repeat steps until there are no more places to dig
    safe = True
    while len(board.dug) < board.dim_size **2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*',input("where would you like to dig? input as row,col: "))
        row, col = int(user_input[0]) , int(user_input[-1])
        if row<0 or row>=board.dim_size or col<0 or col>=board.dim_size:
            print("Invalid Input, Try Again!")
            continue
        safe = board.dig(row,col)
        if not safe: 
            break

    if safe:
        print("VICTORY :)")
        
    else:
        print("GAME OVER")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()
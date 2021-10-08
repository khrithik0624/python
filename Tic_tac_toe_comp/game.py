import time
from player import HumanPlayer,RandomComputerPlayer,GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #list represents the board
        self.current_winner = None # keep track of winner!

    def print_board(self):
        for row in [ self.board [i*3:(i+1)*3] for i in range(3) ]:
            print('| '+' | '.join(row)+' |')

    @staticmethod
    def printBoardNum():
        # tells what number corresponds to what box
        numberBoard= [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| '+' | '.join(row)+' |')
    
    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']
        '''
        moves=[]
        for i,spot in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves
        '''
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self,square,letter):
        
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                 self.current_winner = letter
            return True
        return False

    def winner(self,square,letter):
        # check winner row wise
        row_index = square // 3
        row = self.board[row_index*3:(row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # check winner column wise
        col_index =square % 3
        col = [self.board[i*3 + col_index] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        
        # Check winner diagonalwise
        if square % 2 ==0:
            diagonal1=[self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2=[self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False

def play(game,x_player,o_player,print_game=True):
    if print_game:
        game.printBoardNum()
    letter = 'X'
    while game.empty_squares():
        # get move from player
        if letter == 'O':
            square = o_player.getMove(game)
        else:
            square = x_player.getMove(game)
        
        if game.make_move(square,letter):
            if print_game:
                print(f"{letter} makes move to {square}")
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f"{letter} wins game!")
                    return letter
                return letter

            letter = 'O' if letter == 'X' else 'X'
        
        # small delay
        if print_game:
            time.sleep(0.8) 
    
    if print_game:
        print("It's a tie")
        return None
    return None


if __name__ == '__main__':
    x_player = HumanPlayer('X') 
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t,x_player,o_player,print_game=True)
    x_wins = 0
    o_wins =0
    ties =0
    for i in range(100):
        x_player = RandomComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        print(f"*********{i}th game*********")
        result = play(t, x_player, o_player, print_game= False)
        if result == 'X':
            x_wins = x_wins + 1
        elif result == 'O':
            o_wins = o_wins + 1
        else:
            ties = ties + 1            
    print(f"After 100 iterations we see {x_wins} x wins, {o_wins} o_wins, {ties} ties")
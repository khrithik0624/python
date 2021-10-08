import itertools
from colorama import Fore,Back,Style,init
init()
def display(game):
    print("   0  1  2  ")
    for count, row in enumerate(game):
        colored_row = ""
        for i in row:
            if i==0:
                colored_row += "   "
            elif i==1:
                colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
            else:
                colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
        print(count,colored_row)


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if just_display:
            display(game_map)
            return game_map,False
        if game_map[row][column] != 0:
            print("Place is already occupied")
            display(game_map)
            return game_map, False
        game_map[row][column] = player
        display(game_map)
        return game_map, True
    except IndexError as e:
        print("ERROR Make sure row/col input is 0 1 or 2:", e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong!!", e)
        
        


def win(current_game):
    #horizontal
    for row in current_game:
        if row.count(row[0]) == len(row) and row[0] !=0:
            print(f"Player:{row[0]} is the winner horizontally")
            return True
    #vertical
    for col in range(len(current_game)):
        check=[]
        for row in current_game:
            check.append(row[col])
        if check.count(check[0])==len(check) and check[0]!=0:
            print(f"Player:{check[0]} is the winner vertically")
            return True
    #diagonal
    diag1=[]
    diag2=[]
    for ix in range(len(current_game)):
        diag1.append(current_game[ix][ix])
        diag2.append(current_game[ix][len(current_game)-1-ix])
    if diag1.count(diag1[0]) == len(diag1) and diag1[0]!=0:
        print(f"Player:{diag1[0]} is the winner diagonally")
        return True
    if diag2.count(diag2[0]) == len(diag2) and diag2[0]!=0:
        print(f"Player:{diag2[0]} is the winner diagonally")
        return True
    return False
       
    

play = True
players = [1,2]
while play:
    game = [[0,0,0],
            [0,0,0],
            [0,0,0],]
    
    game_won = False
    game, _ = game_board(game,just_display=True)
    player_choice = itertools.cycle([1,2])

    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False
        while not played:
            row_choice = int(input("What row do you want to play? [0,1,2] : "))
            column_choice = int(input("What column do you want to play? [0,1,2] : "))
            game,played = game_board(game,current_player,row_choice,column_choice)

        if win(game):
            game_won=True
            again = input("The game is over. Do you want to play again (y/n): ")
            if again.lower == "y":
                print("restarting")
            else:
                print("bye")
                play= False
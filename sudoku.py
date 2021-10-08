def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None,None
def is_valid(puzzle,guess,row,col):
    #checking for row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #checking for column
    col_vals = [puzzle[r][col] for r in range(9)]
    if guess in col_vals:
        return False
    
    #checking for 3x3 box
    #      0 1 2    3 4 5    6 7 8
    #    0|     |  |     |  |     |
    #    1|     |  |     |  |     |
    #    2|     |  |     |  |     |
    #   
    #    3|     |  |     |  |     |
    #    4|     |  |     |  |     |
    #    5|     |  |     |  |  *  |
    #    
    #    6|     |  |     |  |     |
    #    7|     |  |     |  |     |
    #    8|     |  |     |  |     |
    row_start = (row // 3 )*3  # 5 // 3 = 1 --> 1*3 = 3
    col_start = (col // 3 )*3  # 7 // 3 = 2 --> 2*3 = 3
    box_vals = [puzzle[r][c] for r in range(row_start,row_start+3) for c in range(col_start,col_start+3)]
    if guess in box_vals:
        return False
    
    return True


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)
    if row == None:
        return True

    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col): 
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
    
        puzzle[row][col] = -1
    
    return False

def __str__(puzzle):
    s = ''
    for r in range(9):
        s += ' ' + ' '.join(str(i) for i in puzzle[r]) +'\n'
    return s
            


if __name__ == '__main__':
    
    puzzle =[
        [3,9,-1, -1,5,-1, -1,-1,-1],
        [-1,-1,-1, 2,-1,-1, -1,-1,5],
        [-1,-1,-1, 7,1,9, -1,8,-1],

        [-1,5,-1, -1,6,8, -1,-1,-1],
        [2,-1,6, -1,-1,3, -1,-1,-1],
        [-1,-1,-1, -1,-1,-1, -1,-1,4],

        [5,-1,-1, -1,-1,-1, -1,-1,-1],
        [6,7,-1, 1,-1,5, -1,4,-1],
        [1,-1,9, -1,-1,-1, 2,-1,-1]
    ]
    print(__str__(puzzle))
    print(solve_sudoku(puzzle))
    print(__str__(puzzle))

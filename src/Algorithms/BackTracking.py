def FindEmpty(Sudoku):
    for row in range(len(Sudoku)):
        for col in range(len(Sudoku)):
            if Sudoku[row][col] == 0 :
                return (row , col)
    return None

def isValid(Sudoku, num, pos):
    for row in range(len(Sudoku)):
        if Sudoku[pos[0]][row] == num and pos[1] != 0 :
            return False

    for col in range(len(Sudoku)):
        if Sudoku[pos[1]][col] == num and pos[0] != 0 :
                    return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3 , box_y *3 + 3):
        for j in range(box_x *3 , box_x *3 + 3):
            if Sudoku[i][j] == num and (i,j) != pos :
                return False

    return True


def BackTracking(Sudoku):
    Find = FindEmpty(Sudoku)
    if not Find:
        return True
    else:
        row , col = Find
        for i in range(len(Sudoku)):
            if isValid(Sudoku , i , (row,col)):
                Sudoku[row][col] = i 

                if BackTracking(Sudoku):
                    return True
                Sudoku[row][col] = 0
    return False
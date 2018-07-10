# 6 rows
# 7 columns

test = [[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [1,1,2,0,0,0,0]]

def board_print(board):
    print(" -0- -1- -2- -3 -4- -5- -6- ")
    for row in range(6):
        cur = "| "
        for col in range(7):
            if board[row][col] == 0:
                fill = " "
            elif board[row][col] == 1:
                fill = "X"
            else: fill = "O"
            cur += "{} | ".format(fill)
        print(cur)
    print(" ---"*7)
    
def play(board, col, player):
    # If the top row is full, return -1, indicating you can't play there
    if(board[0][col]!= 0):
        return -1
    else:
        # otherwise, start at the bottom row (6), and fill in the first empty you find
        for row in range(5, -1, -1):
            if board[row][col] == 0:
                board[row][col] = player
                return 1

def check_rows(board):


board_print(test)
play(test, 1, 1)
board_print(test)
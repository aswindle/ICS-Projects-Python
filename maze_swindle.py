import random
board = [[0,0,"X",0,0],
         ["X",0,"X",0,"X"],
         [0,0,"X",0,0],
         [0,"X","X","X",0],
         [0,0,0,0,"X"],]
top = "----------   ----"

def print_board(board):
    print(top)
    for r in range(0, 5):
        row = ""
        if r == 0 or r == 3:
            row += " "
        else:
            row+= "|"
        for c in range(0, 5):
            if board[r][c]== 0:
                row += "   "
            else:
                row += " " + str(board[r][c]) + " "
        if r == 0 or r == 3:
            row += " "
        else:
            row+= "|"
        print(row)
    print(top)
    
def start():
    first_r = random.randrange(0,4)
    first_c = random.randrange(0,4)
    while board[first_r][first_c] == "X":
        first_r = random.randrange(0,4)
        first_c = random.randrange(0,4)
    board[first_r][first_c] = "P"
    return [first_r, first_c]

def winner():
    win_r = random.randrange(0,4)
    win_c = random.randrange(0,4)
    while board[win_r][win_c] == "X" or board[win_r][win_c] == "P":
        win_r = random.randrange(0,4)
        win_c = random.randrange(0,4)
    board[win_r][win_c]= "G"
    return [win_r, win_c]

def move(r, c, direction):
    if direction == "w":
        if r == 0:
            if c == 3:
                board[4][3] = "P"
                board[r][c] = " "
                r = 4
        else:
            if board[r-1][c] != "X":
                board[r-1][c] = "P"
                board[r][c] = " "
                r -=1
    elif direction == "a":
        if c == 0:
            if r == 0 or r == 3:
                board[r][4] = "P"
                board[r][c] = " "
                c = 4
        else:
            if board[r][c-1] != "X":
                board[r][c-1] = "P"
                board[r][c] = " "
                c -= 1
    elif direction == "s":
        if r == 4:
            if c == 3:
                board[0][3] = "P"
                board[r][c] = " "
                r = 0
        else:
            if board[r+1][c] != "X":
                board[r+1][c] = "P"
                board[r][c] = " "
                r += 1
    else: #direction = d = right
        if c == 4:
            if r == 0 or r == 3:
                board[r][0] = "P"
                board[r][c] = " "
                c = 0
        else:
            if board[r][c+1] != "X":
                board[r][c+1] = "P"
                board[r][c] = " "
                c += 1
    return [r, c]

current = start()
win = winner()

while(win != current):
    print_board(board)
    next = input("Move choice: w, a, s, d: ")
    current = move(current[0], current[1], next)
print_board(board)
print("You win!")
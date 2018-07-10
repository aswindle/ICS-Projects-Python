def print_border(cols, border):
    row = " "
    for x in range(cols):
        row += border * 3 + " "
    print(row)

def print_row(cur_row):
    row = "|"
    for i in range(len(cur_row)):
        row += " "
        if(cur_row[i]==0):
            row += " "
        elif(cur_row[i] == 1):
            row += "X"
        elif(cur_row[i] == 2):
            row += "O"
        row += " |"
    print(row)

def board_print(board):
    print_border(len(board[0]), '-')
    for row in range(len(board)):
        print_row(board[row])
        print_border(len(board[0]), '-')
        
    


b1 = [[0,0,0], [1,0,1], [2,2,2]]
b2 = [[1,1,1], [2,2,2], [0,0,0]]
b3 = [[1,2,1], [2,1,2], [1,2,1]]
board_print(b1)
board_print(b2)
board_print(b3)
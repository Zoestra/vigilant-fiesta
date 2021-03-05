'''
Connect 4

ask for player names
load blank board
accept player inputs for column placement
place counter in lowest position in column
check for win state vertically, horizontally, and diagonally
if win, print boardstate to file.

what is needed:

boardstate array
winstate check functions
player move function

'''


board =[[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]] 

def displayBoard():
    for i in board:
        print(str(i))

def place(col,plyr):
    c=0
    for i in board:
        if board[5][col-1] == 0:
            board[5][col-1] = plyr
        elif board[c][col-1] != 0:
            board[c-1][col-1] = plyr
        else:
            c+=1


'''
def check_win:


winstate = check_win(board)
def main:

while winstate == False:
'''

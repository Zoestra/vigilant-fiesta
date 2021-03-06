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

import datetime
board =[[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]] 
key = []
for i in range(len(board)+1):
    key.append(i + 1)

def displayBoard():
    print(key)
    for i in board:
        print(str(i))
def place(col,plyr):
    c=0
    for i in board:
        if board[-1][col] == 0:
            board[-1][col] = plyr
        elif board[c][col] != 0:
            board[c-1][col] = plyr
        else:
            c+=1
def vertScan():
    a,b,c = 0,0,0
    for x in range(len(board)):
        for y in board:
            if y[x] == 1:
                a+=1
                b=0
            elif y[x] == 2:
                b+=1
                a=0     
    if a >= 4 or b >= 4:
        return(True)
    else:
        return(False)
def horizScan():
    a,b=0,0
    for y in range(len(board)):
        for x in board[y]:
            if x == 1:
                a+=1
                b=0
            elif x == 2:
                b += 1
                a = 0
    if a >= 4 or b >= 4:
        return(True)
    else:
        return(False)
def diagScan():
    for i in range(3,len(board)):
        for j in board[i]:
            if j <= (len(board[0])/2):  #righthand checks
                if board[i][j] == 1 and board[i-1][j+1] ==1 and board[i-2][j+2] == 1 and board[i-3][j+3] == 1:
                    return(True)  
                elif board[i][j] == 2 and board[i-1][j+1] == 2 and board[i-2][j+2] == 2 and board[i-3][j+3] == 2 :
                    return(True) 
            if j >= (len(board[0])/2): #lefthand checks    
                if board[i][j] == 1 and board[i-1][j-1] ==1 and board[i-2][j-2] == 1 and board[i-3][j-3] == 1:
                    return(True)
                elif board[i][j] == 2 and board[i-1][j-1] == 2 and board[i-2][j-2] == 2 and board[i-3][j-3] == 2:
                    return(True)
    return(False)
def checkWin():
    if vertScan() or horizScan() or diagScan():
        return(True)
    else:
        return(False)

def main():
    print('Welcome to Connect 4!')
    plyr1 = input('Please enter name of Player 1: ')
    plyr2 = input('Please enter name of Player 2: ')
    plyrname = 0
    turn = False
    plyr = 0
    displayBoard()
    c = 0
    while not checkWin() or c == ((len(board)*len(board[0]))):
        turn = not turn
        if turn:
            plyr=1
            plyrname = plyr1
        else:
            plyr=2
            plyrname = plyr2
        col = (int(input(f'{plyrname}: pick a column: '))-1)
        place(col,plyr)
        displayBoard()
        c+=1
        checkWin()
    wintime = datetime.datetime.now()
    if c != ((len(board)*len(board[0]))):
        print(f'{plyrname} wins!')
        file = open('Game Records.txt','a')
        file.write(f'*******\n {wintime}\n{displayBoard()}\n{plyrname} wins!\n*******\n')
    elif c == ((len(board)*len(board[0]))) and not checkWin():
        print('Stalemate!')
        file = open('Game Records.txt','a')
        file.write(f'*******\n {wintime}\n{displayBoard()}\nStalemate\n*******\n')
main()
        


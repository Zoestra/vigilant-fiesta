from graphics import *
import datetime
win=GraphWin('Connect 4', 800,700)  #initializes window and board
win.setCoords(0,0,8,7)
win.setBackground('beige')
board =[[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]] 
key = []
for i in range(len(board)+1):
    key.append(i + 1)
7
class triBut:
    def __init__(self, x1, x2, x3, y1, y2, y3, label, color):
        self.x1, self.x2, self.x3 = x1, x2, x3
        self.y1, self.y2, self.y3 = y1, y2, y3
        self.point1 = Point(x1,y1)
        self.point2 = Point(x2,y2)
        self.point3 = Point(x3,y3)
        self.label = label
        self.color = color
        self.center = Point((x1+.25), 6.78)

    def drawBut(self):
        but = Polygon(self.point1, self.point2, self.point3)
        but.setFill(f'{self.color}')
        l = Text(self.center,self.label)
        but.draw(win)
        l.draw(win)#triangular column buttons
class sqrBut:
    def __init__(self, x1, y1, x2, y2, label, color):
        self.point1 = Point(x1, y1)
        self.point2 = Point(x2, y2)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.label = label
        self.color = color
        self.textAnchr = Point(((x2 + x1) / 2 ), ((y2 + y1) / 2 ) )

    def drawBut(self):
        but= Rectangle(self.point1, self.point2)
        but.setFill(self.color)
        label = Text(self.textAnchr, self.label)
        but.draw(win)
        label.draw(win)
    def checkBut(self, x, y):
        return(self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2)
class screenTxt:
    def __init__(self, text, ancx, ancy, bkx1, bky1, bkx2, bky2, bkcolor):
        self.ancx , self.ancy = ancx , ancy 
        self.bkx1, self.bky1, self.bkx2, self.bky2 = bkx1, bky1, bkx2, bky2
        bkcolor = bkcolor
        self.anchor = Point(ancx, ancy)
        self.bkP1 , self.bkP2 = Point(bkx1, bky1), Point(bkx2, bky2)
        self.bkcolor = bkcolor
        self.text = text
        self.textObject = Text( self.anchor, self.text)
        self.background = Rectangle(self.bkP1, self.bkP2)
    def drawTxt(self):
        self.background.setFill(self.bkcolor)
        self.background.draw(win)
        self.textObject.draw(win)
    def undrawTxt(self):
        self.background.undraw()
        self.textObject.undraw()

def printBoard(): 
    print('~~~~~~~~~~')
    for i in board:
        print(str(i))#prints boardstate into console
    print('~~~~~~~~~~')
def place(col,currentPlayer):
    c=0
    for i in board:
        if board[-1][col] == 0:
            board[-1][col] = currentPlayer
        elif board[c][col] != 0:
            board[c-1][col] = currentPlayer
        else:
            c+=1#places token of current player in lowest position in column
def drawBoardstate(board,circList):
    for i in range(len(board)):
        for j in range(len(board[0])):
            circList[i][j].undraw()
            if board[i][j] == 1:
                circList[i][j].setFill('black')
            elif board[i][j] == 2:
                circList[i][j].setFill('red')
            circList[i][j].draw(win)
    
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
        return(False)#searches vertically for a win
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
            elif a >= 4 or b >= 4:
                return(True)
    return(False)#searches horizontally for a win
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
    return(False)#searches diagonally for a win
def checkWin():
    if vertScan() or horizScan() or diagScan():
        return(True)
    else:
        return(False)#combines scans to search whole board for win
def drawEmptyBoard():
    boardBkg = Rectangle(Point(.5,.5),Point(7.5,6.5))
    boardBkg.setFill('blue')
    boardBkg.draw(win)
    circList = [[],[],[],[],[],[],[]]
    for i in range(len(board)):
        for j in range(len(board[0])):
            x , y = j+1, 6-i
            tempCircle = Circle(Point(x,y),.45)
            tempCircle.setFill('white'), tempCircle.draw(win)
            circList[i].append(tempCircle)
    return(circList)#initializes graphical board 
def createTri():    
    y = 6.9
    triList = []
    for i in range(7):
        x = i + 1
        a,b,c = (x-.25), x+.25, y-.3
        p1, p2, p3 = Point(a,y), Point(b,y), Point(x,c)
        tri = triBut(a,b,x,y,y,c,i+1,'green')
        tri.drawBut()
        triList.append(tri)
    return(triList) #draws triangle buttons 
def area(x1, y1, x2, y2, x3, y3): 

	return abs((x1 * (y2 - y3) + x2 * (y3 - y1) 
				+ x3 * (y1 - y2)) / 2.0) #finds area of triangle, for mousechecks
def pointInTriangle(x1, y1, x2, y2, x3, y3, x, y):
    denominator = ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    a = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3))/denominator
    b = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3))/denominator
    c = 1 - a - b
    return 0 <= a and a <= 1 and 0 <= b and b <= 1 and 0 <= c and c <= 1#determines if click is inside of a triangle
def tributcheck(x,y,triList):
    for i in range(len(triList)):
        if pointInTriangle(triList[i].x1, triList[i].y1, triList[i].x2, triList[i].y2, triList[i].x3, triList[i].y3, x, y):
            print(f'clicked {i}')
            return(True, i)
    return(False)   #checks if click is inside triangle buttons, returns bool and index of button

def main():
    circList = drawEmptyBoard()
    triList = createTri()
    exitBut = sqrBut(7.5,6.5,8,7,'EXIT', 'red')
    exitBut.drawBut()
    welcome = screenTxt('Welcome to Connect 4', 4, 3.5, 2.5, 2.5, 5.5, 4.5, 'beige')    
    welcome.drawTxt()
    print('Welcome to Connect 4!')
    win.getMouse()
    entry = Entry(Point(4, 3.5) , 15)
    welcome.undrawTxt()
    
    player1entrytxt = screenTxt(f'Player 1, enter your name', 4, 4, 2.5, 2.5, 5.5, 4.5, 'beige')
    player1entrytxt.drawTxt()
    entry.draw(win)
    clickdone = screenTxt('click when done', 4,3, 3.25,2.75, 4.75,3.25, 'green' )
    clickdone.drawTxt()
    plyr1 = entry.getText()
    
    
    win.getMouse()
    player1entrytxt.undrawTxt()
    player2entrytxt =  screenTxt(f'Player 2, enter your name', 4, 4, 2.5, 2.5, 5.5, 4.5, 'beige')
    player2entrytxt.drawTxt()
    clickdone.undrawTxt()
    clickdone.drawTxt()
    plyr2 = entry.getText()
    win.getMouse()
    player2entrytxt.undrawTxt()
    clickdone.undrawTxt()
    entry.undraw()
    if plyr1 == '':
        plyr1 == 'Black'
    if plyr2 == '':
        plyr2 == 'Red'
    currentPlayerName = 0
    turn = False
    currentPlayer = 0
    printBoard()
    c = 0
    '''while not checkWin() or c == ((len(board)*len(board[0]))):
        turn = not turn
        if turn:
            currentPlayer=1
            currentPlayerName = plyr1
        else:
            currentPlayer=2
            currentPlayerName = plyr2
        col = (int(input(f'{currentPlayerName}: pick a column: '))-1)
        place(col,currentPlayer)
        printBoard()
        c+=1
        checkWin()
    wintime = datetime.datetime.now()
    if c != ((len(board)*len(board[0]))):
        print(f'{currentPlayerName} wins!')
        file = open('Game Records.txt','a')
        file.write(f'*******\n {wintime}\n{printBoard()}\n{currentPlayerName} wins!\n*******\n')
    elif c == ((len(board)*len(board[0]))) and not checkWin():
        print('Stalemate!')
        file = open('Game Records.txt','a')
        file.write(f'*******\n {wintime}\n{printBoard()}\nStalemate\n*******\n')'''
    click = Point(0,0)
    gameWon = checkWin()
    while gameWon == False or c == ((len(board)*len(board[0]))):
        
        
        if exitBut.checkBut(click.getX(),click.getY()) == True:
            break

        if turn:
            currentPlayer, currentPlayerName= 1, plyr1
        else:
            currentPlayer, currentPlayerName= 2, plyr2

        if tributcheck(click.getX(),click.getY(),triList):
            turn = not turn #flips turn indicator
            columnChoice = tributcheck(click.getX(),click.getY(), triList)[1]
            place(columnChoice, currentPlayer )
            drawBoardstate(board, circList)
            printBoard()
            gameWon = checkWin()
            print(f'gameWon = {gameWon}\n')
        click = win.getMouse()

        
        print(f'x = {click.getX()}, y = {click.getY()}')
    
        
        
        
    win.close()

main()

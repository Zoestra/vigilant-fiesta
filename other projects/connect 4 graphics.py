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
from graphics import *
import datetime
win=GraphWin('Connect 4', 800,700)
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
        l.draw(win)

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
        print(self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2)
        return(self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2)
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
            elif a >= 4 or b >= 4:
                return(True)
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
def drawBoard():
    boardBkg = Rectangle(Point(.5,.5),Point(7.5,6.5))
    boardBkg.setFill('blue')
    boardBkg.draw(win)
    circList = [[],[],[],[],[],[],[]]
    for i in range(7):
        for j in range(6):
            x , y = i+1, j+1
            z = Circle(Point(x,y),.5)
            z.setFill('white'), z.draw(win)
            circList[i].append(z)
    return(circList)
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
    return(triList)  
def area(x1, y1, x2, y2, x3, y3): 

	return abs((x1 * (y2 - y3) + x2 * (y3 - y1) 
				+ x3 * (y1 - y2)) / 2.0) 
def pointInTriangle(x1, y1, x2, y2, x3, y3, x, y):
    denominator = ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    a = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3))/denominator
    b = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3))/denominator
    c = 1 - a - b
    return 0 <= a and a <= 1 and 0 <= b and b <= 1 and 0 <= c and c <= 1
    #Barycentric Way to check if a point is in a triangle 
def tributcheck(x,y,triList):
    for i in range(len(triList)):
        if pointInTriangle(triList[i].x1, triList[i].y1, triList[i].x2, triList[i].y2, triList[i].x3, triList[i].y3, x, y):
            return(True, i)
    return(False)   

def main():
    circList = drawBoard()
    triList = createTri()
    exitBut = sqrBut(7.5,6.5,8,7,'EXIT', 'red')
    exitBut.drawBut()
    test = triList[0]
    print(test.x1, test.x2, test.x3, test.y1, test.y2, test.y3)
    
    '''
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
        file.write(f'*******\n {wintime}\n{displayBoard()}\nStalemate\n*******\n')'''
    click = Point(0,0)

    while checkWin() == False or c == ((len(board)*len(board[0]))):
        if exitBut.checkBut(click.getX(),click.getY()) == True:
            break
        click = win.getMouse()
        print(f'x = {click.getX()}, y = {click.getY()}')
    '''while tributcheck(click.getX(),click.getY(),triList) == False:
        click = win.getMouse()
        print(f'x = {click.getX()}, y = {click.getY()}')
        print(tributcheck(click.getX(),click.getY(),triList))'''
    win.close()

main()
        


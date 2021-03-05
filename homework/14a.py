#0w0
'''Homework 14 part a
Due: 2021-03-04 23:59:00
Description: Rectangles; Draw dice
Draw 6 rectangles in a graphics window. Make the rectangles a different color from the background. 
The tops of your rectangles should conform to the linear function y=x, creating a diagonal pattern 
up-and-to-the-right. In order to receive full credit you must use a for loop, a clone command, and 
a .move(dx,dy) command. Do not simply paste six different rectangles in six different places.
'''

from graphics import *
def main():
     win= GraphWin('win',600,600)
     win.setCoords(0,0,5,5)
     background = Rectangle(Point(0,0),Point(5,5))
     background.setFill('purple')
     background.draw(win)
     square = Rectangle(Point(0,0),Point(1,1))
     square.setFill('gold')
     square.draw(win)
     for i in range(4):
          squarei = square.clone()
          squarei.move(1,1)
          squarei.draw(win)
          square = squarei

     win.getMouse()
main()

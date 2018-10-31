# Trevor Cardoza
# CS 21, Fall 2018
# Program: cardoza_archery.py

from graphics import *
from math import sqrt

def main():
    my_win = create_target_window()
    Score = Text(Point(200,365),"Current Score: 0")
    Score.draw(my_win)
    pnt = 0
    while True:
        p = my_win.checkMouse()
        quit_Program = my_win.checkKey()
        if quit_Program == "q":
            break
        elif p != None:
            pt = Point(199,199)
            points = get_score(p)
            pnt += points
            p.draw(my_win)
            current_score = ("".join(["Current Score:",str(pnt)]))
            Score.setText(current_score)
    my_win.close()
        
def create_target_window():
    win = GraphWin("Archery Target",400,400)
    win.setBackground("grey")
    circ = Circle(Point(199,199),125)
    circ.setFill("white")
    circ.draw(win)
    circ1 = Circle(Point(199,199),100)
    circ1.setFill("black")
    circ1.draw(win)
    circ2 = Circle(Point(199,199),75)
    circ2.setFill("blue")
    circ2.draw(win)
    circ3 = Circle(Point(199,199),50)
    circ3.setFill("red")
    circ3.draw(win)
    circ4 = Circle(Point(199,199),25)
    circ4.setFill("yellow")
    circ4.draw(win)
    return win

def get_score(p):
    points = int()
    x = p.getX()
    y = p.getY()
    distance = sqrt((Point(199,199).getX()-x)**2+(Point(199,199).getY()-y)**2)
    while True:
        if distance <= 25:
            points += 9
            return points
        elif distance <= 50 and distance >= 25:
            points += 7
            return points
        elif distance <= 75 and distance >= 50:
            points += 5
            return points
        elif distance <= 100 and distance >= 75:
            points += 3
            return points  
        elif distance <= 125 and distance >= 100:
            points += 1
            return points
            
main()

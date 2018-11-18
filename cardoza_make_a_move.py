# Trevor Cardoza
# CS 21, Fall 2018
# Program: cardoza_make_a_move.py

from graphics import *
from math import sqrt
from time import sleep
from random import *

def create_window():
    win = GraphWin("Snake",900,900)
    win.setBackground("light grey")
    win.setCoords(-50,-50,50,50)
    Point(0,0).draw(win)
    return win

def create_creature(win, x, y):
    n = 0
    body_parts=[0,1,2,3,4,5,6,7,8,9]
    creature=[]
    head=Rectangle(Point(-0.5,-0.5),Point(0.5,0.5))
    head.move(x,y)
    head.setFill("yellow")
    for i in body_parts:
        i = head.clone()
        i.move(n,0)
        if n > 0:
            i.setFill("red")
        creature.append(i)
        i.draw(win)
        n += 1
    return creature

def main():
    my_win = create_window()
    border = Rectangle(Point(-50,-50),Point(50,50))
    border.setOutline("yellow")
    border.setWidth(3)
    border.draw(my_win)
    creature = create_creature(my_win,randint(-48,48),randint(-48,48))
    v = 0
    h = 0
    Speed = 0.1
    Apple = Rectangle(Point(-0.5,-0.5),Point(0.5,0.5))
    Apple.setFill("red")
    Apple.setOutline("green")
    Apple.setWidth(2)
    Apple.move(randint(-48,48),randint(-48,48))
    Apple.draw(my_win)
    Start = Text(Point(0,0), "PRESS I, J, K, or M TO START!")
    Start.setSize(20)
    Start.draw(my_win)
    print(Apple)
    while True:
        try:
            button_Press = my_win.checkKey()
        except GraphicsError:
            return None
        if button_Press == "q":
            try:
                my_win.close()
            except GraphicsError:
                return None
        else:
            if button_Press != None:
                p = creature[0].getCenter()
                x = p.getX()
                y = p.getY()
                body_line = Line(Point(x,y),creature[len(creature)-1].getCenter())
                bls = body_line.getP1().getX()-0.1
                ble = body_line.getP2().getX()-0.1
                body_line.draw(my_win)
                body_line.undraw()
                time.sleep(Speed)
                if x >= border.getP2().getX() or x <= border.getP1().getX() or y >= border.getP2().getY() or y <= border.getP1().getY():
                    v = 0
                    h = 0
                    game_Over = Text(Point(0,0), "Game Over")
                    game_Over.setSize(20)
                    game_Over.draw(my_win)
                    for l in creature:
                        l.undraw()
                    for x in range(3,0,-1):
                        count_Down = Text(Point(0,-5), x)
                        count_Down.setSize(30)
                        count_Down.draw(my_win)
                        time.sleep(0.8)
                        count_Down.undraw()
                        time.sleep(0.4)
                    game_Over.undraw()
                    count_Down.undraw()
                    my_win.close()
                    main()
                d = sqrt((Apple.getCenter().getX()-x)**2+(Apple.getCenter().getY()-y)**2)
                if d == 0:
                    Apple.undraw()
                    creature.append(Rectangle(Point(-0.5,-0.5),Point(0.5,0.5)))
                    creature[0].setFill("yellow")
                    Speed = Speed*0.5
                    print(Speed)
                    Apple.draw(my_win)
                    av = randint(-48,48)
                    ah = randint(-48,48)
                    Apple.move(av,av)
                    while (Apple.getCenter().getX() >= 48 or Apple.getCenter().getX() <= -48 or Apple.getCenter().getY() >= 48 or Apple.getCenter().getY() <= -48):
                        Apple.move(randint(-30,30),randint(-30,30))
                        time.sleep(0.3)
                    print("Apple",Apple)
            if h == 1 or button_Press == "i" and h != -1:
                Start.undraw()
                creature[len(creature)-1].undraw()
                creature.pop()
                creature.insert(0,Rectangle(Point(-0.5,-0.5),Point(0.5,0.5)))
                creature[0].setFill("yellow")
                creature[0].move(creature[1].getCenter().getX(),creature[1].getCenter().getY()+1)
                creature[0].draw(my_win)
                v = 0
                h = 1
            if v == 1 or button_Press == "k" and v != -1:
                Start.undraw()
                creature[len(creature)-1].undraw()
                creature.pop()
                creature.insert(0,Rectangle(Point(-0.5,-0.5),Point(0.5,0.5)))
                creature[0].setFill("yellow")
                creature[0].move(creature[1].getCenter().getX()+1,creature[1].getCenter().getY())
                creature[0].draw(my_win)
                v = 1
                h = 0
            if v == -1 or button_Press == "j" and v != 1:
                Start.undraw()
                creature[len(creature)-1].undraw()
                creature.pop()
                creature.insert(0,Rectangle(Point(-0.5,-0.5),Point(0.5,0.5)))
                creature[0].setFill("yellow")
                creature[0].move(creature[1].getCenter().getX()-1,creature[1].getCenter().getY())
                creature[0].draw(my_win)
                v = -1
                h = 0
            if h == -1 or button_Press == "m" and h != 1:
                Start.undraw()
                creature[len(creature)-1].undraw()
                creature.pop()
                creature.insert(0,Rectangle(Point(-0.5,-0.5),Point(0.5,0.5)))
                creature[0].setFill("yellow")
                creature[0].move(creature[1].getCenter().getX(),creature[1].getCenter().getY()-1)
                creature[0].draw(my_win)
                v = 0
                h = -1
main()

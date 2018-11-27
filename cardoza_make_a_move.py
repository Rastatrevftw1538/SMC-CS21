# Trevor Cardoza
# CS 21, Fall 2018
# Program: cardoza_make_a_move.py

from graphics import *
from math import sqrt
from time import sleep
from random import *

#This function creates the window by setting the graphic window to
#900 by 900, sets the background to light grey, and setting the
#coordinates to -25,-25 and 25,25 so the center of the screen is equal
#to 0,0. Then return the window created.
def create_window():
    win = GraphWin("Snake",900,900)
    win.setBackground("light grey")
    win.setCoords(-25,-25,25,25)
    Point(0,0).draw(win)
    return win

#This function creates the player by grabbing the window and the x and y
#coordinates set by the random int function in main. Then the function creates
#a list called body parts that has a length of 4. The next list called creature
#is used to turn the ints in body parts into yellow rectangles to make the body.
#In the for loop, it creates clones of the head, moves them 1 spot to the right,
#and attachs the rectangle to the list creature.
def create_creature(win, x, y):
    n = 0
    body_parts=[0,1,2,3]
    creature=[]
    head=Rectangle(Point(-0.5,-0.5),Point(0.5,0.5))
    head.move(x,y)
    head.setFill("yellow")
    for i in body_parts:
        i = head.clone()
        i.move(n,0)
        creature.append(i)
        i.draw(win)
        n += 1
    return creature

#The main function starts by setting variables and creating
#the border that shows where the out of bounds is. This is also
#where the Apple is created, colored and centered in the middle
#of the screen. Another purpose for this is to creates the UI
#retaining to which buttons to press to begin. Then inside a
#while loop equaling true, there is a try-except operator that
#signifies if Q is pressed, then close the window. Also it is
#to prevent any exception errors.
highestScore = [0]
def main():
    my_win = create_window()
    creature = create_creature(my_win,randint(-20,20),randint(-20,20))
    border = Rectangle(Point(-25,-25),Point(25,25))
    border.setOutline("yellow")
    border.setWidth(3)
    border.draw(my_win)
    v = 0
    h = 0
    Speed = 0.2
    Apple = Rectangle(Point(-0.5,-0.5),Point(0.5,0.5))
    Apple.setFill("red")
    Apple.setOutline("green")
    Apple.setWidth(2)
    Apple.draw(my_win)
    L = 0
    Score = Text(Point(-5,22),"Score: ")
    Number = Text(Point(-3,22),L)
    highScore = Text(Point(5,22),"High Score: ")
    highNumber = Text(Point(8.5,22),highestScore[0])
    Score.setSize(20)
    Number.setSize(20)
    highScore.setSize(20)
    highNumber.setSize(20)
    highNumber.setText(highestScore[0])
    Score.draw(my_win)
    Number.draw(my_win)
    highScore.draw(my_win)
    highNumber.draw(my_win)
    Start = Text(Point(0,0), "PRESS I, J, K, or M TO START!")
    Start.setSize(20)
    Start.draw(my_win)
    while True:
        try:
            button_Press = my_win.checkKey()
        except GraphicsError:
            return None
        if button_Press == "q":
            break
        else:
#When the game is running, it will get the center and x and y coordinates of the head of the snake.
            if button_Press != None:
                p = creature[0].getCenter()
                x = p.getX()
                y = p.getY()
                time.sleep(Speed)
                if x >= border.getP2().getX() or x <= border.getP1().getX() or y >= border.getP2().getY() or y <= border.getP1().getY():
                    v = 0
                    h = 0
                    game_Over = Text(Point(0,0), "Game Over")
                    game_Over.setSize(30)
                    game_Over.draw(my_win)
                    for l in creature:
                        l.undraw()
                        time.sleep(0.1)
                    for x in range(3,0,-1):
                        count_Down = Text(Point(0,-2), x)
                        count_Down.setSize(30)
                        count_Down.draw(my_win)
                        time.sleep(0.8)
                        count_Down.undraw()
                        time.sleep(0.4)
                    game_Over.undraw()
                    count_Down.undraw()
                    my_win.close()
                    if L > highestScore[0]:
                        highestScore.pop()
                        highestScore.append(L)
                    main()
                d = sqrt((Apple.getCenter().getX()-x)**2+(Apple.getCenter().getY()-y)**2)
                if d == 0:
                    creature.append(Rectangle(Point(-0.5,-0.5),Point(0.5,0.5)))
                    creature[0].setFill("yellow2")
                    Speed = Speed*0.5
                    av = randint(-10,10)
                    ah = randint(-10,10)
                    Apple.move(av,av)
                    L += 1
                    Number.setText(L)
                    while (Apple.getCenter().getX() >= 25 or Apple.getCenter().getY() >= 25):
                        Apple.move(randint(-20,-19),randint(-20,-19))
                    while (Apple.getCenter().getX() <= -25 or Apple.getCenter().getY() <= -25):
                        Apple.move(randint(19,20),randint(19,20))
#Depending on the direction it is going in (either left[v=-1], right[v=1],
#up[h=1] and down[h=-1]) the rectangle at the end of the snake will move to
#the front of the snake.
            if h == 1 or button_Press == "i" and h != -1:
                Start.undraw()
                creature[len(creature)-1].undraw()
                creature.pop()
                creature.insert(0,Rectangle(Point(-0.5,-0.5),Point(0.5,0.5)))
                creature[0].setFill("yellow")
                creature[0].move(creature[1].getCenter().getX(),creature[1].getCenter().getY()+1)
                v = 0
                h = 1
                creature[0].draw(my_win)
            if v == 1 or button_Press == "k" and v != -1:
                Start.undraw()
                creature[len(creature)-1].undraw()
                creature.pop()
                creature.insert(0,Rectangle(Point(-0.5,-0.5),Point(0.5,0.5)))
                creature[0].setFill("yellow")
                creature[0].move(creature[1].getCenter().getX()+1,creature[1].getCenter().getY())
                v = 1
                h = 0
                creature[0].draw(my_win)
            if v == -1 or button_Press == "j" and v != 1:
                Start.undraw()
                creature[len(creature)-1].undraw()
                creature.pop()
                creature.insert(0,Rectangle(Point(-0.5,-0.5),Point(0.5,0.5)))
                creature[0].setFill("yellow")
                creature[0].move(creature[1].getCenter().getX()-1,creature[1].getCenter().getY())
                v = -1
                h = 0
                creature[0].draw(my_win)
            if h == -1 or button_Press == "m" and h != 1:
                Start.undraw()
                creature[len(creature)-1].undraw()
                creature.pop()
                creature.insert(0,Rectangle(Point(-0.5,-0.5),Point(0.5,0.5)))
                creature[0].setFill("yellow")
                creature[0].move(creature[1].getCenter().getX(),creature[1].getCenter().getY()-1)
                v = 0
                h = -1
                creature[0].draw(my_win)
    my_win.close()
main()

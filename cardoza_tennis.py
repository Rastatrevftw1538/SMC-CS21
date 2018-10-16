# Trevor Cardoza
# CS 21, Fall 2018
# Program: cardoza_tennis.py

from random import random

def play_game(num_games, prob_a):
    plr_A = 0
    plr_B = 0
    A = 0
    B = 0
    a_wins = 0
    b_wins = 0
    points = ["0", "15", "30", "40", "Win"]
    deuce_Points = ["Deuce", "Advantage", "Win"]
    Win = False
    Deuce = False
    Winner = ""
    for x in range(num_games):
        #print(x)
       # print("Wins", a_wins, "-", b_wins)
        #print("Points", plr_A, "-", plr_B)
        Win = False
        Deuce = False
        A = 0
        B = 0
        plr_A = deuce_Points[A]
        plr_B = deuce_Points[B]
        plr_A = points[A]
        plr_B = points[B]
        if x+1 == num_games:
            print("Done")
            if a_wins > b_wins:
                return print("Player A won", a_wins, "out of",num_games)
            if a_wins < b_wins:
                return print("Player B won", b_wins, "out of",num_games)
        else:
            while ( Win != True):
                if (plr_A == plr_B and plr_A == points[3]):
                    Deuce = True
                    A = 0
                    B = 0
                    plr_A = deuce_Points[A]
                    plr_B = deuce_Points[B]
                    #print("Deuce: ", plr_A,"-",plr_B)
                    while Deuce == True:
                        if (random() < prob_a):
                            print(random())
                            A += 1
                            plr_A = deuce_Points[A]
                           # print("Deuce: ", plr_A,"-",plr_B)
                        elif (random() > prob_a):
                            print(random())
                            B += 1
                            plr_B = deuce_Points[B]
                           # print("Deuce: ", plr_A,"-",plr_B)
                        if (plr_A == deuce_Points[1] and plr_A == plr_B):
                            A = 0
                            B = 0
                            plr_A = deuce_Points[A]
                            plr_B = deuce_Points[B]
                           # print("Deuce: ", plr_A,"-",plr_B)
                        if plr_A == deuce_Points[2]:
                            Win = True
                            a_wins += 1
                            A = 0
                            B = 0
                            plr_A = deuce_Points[A]
                            plr_B = deuce_Points[B]
                            break
                        if plr_B == deuce_Points[2]:
                            Win = True
                            b_wins += 1
                            break
                else:   
                    if (random() < prob_a):
                        print(random())
                        A += 1
                        plr_A = points[A]
                       # print("Score: ", plr_A,"-",plr_B)
                    elif (random() > prob_a):
                        print(random())
                        B += 1
                        plr_B = points[B]
                       # print("Score: ", plr_A,"-",plr_B)
                    if plr_A == points[4]:
                        Win = True
                        a_wins += 1
                        A = 0
                        B = 0
                        plr_A = points[A]
                        plr_B = points[B]
                    if plr_B == points[4]:
                        Win = True
                        b_wins += 1
                        A = 0
                        B = 0
                        plr_A = points[A]
                        plr_B = points[B]

# Trevor Cardoza
# CS 21, Fall 2018
# Program: cardoza_tennis.py

from random import random

def print_intro():
    print("This is a tennis simulator")
    print("")
    print("This program will play through a set amount")
    print("of games with a set probability for Player A")
    print("and will show every game, who wins, the amount")
    print("each player wins and the percentage that Player A")
    print("won. Have fun!!!")
    print("")
    
def get_inputs():
    while True:
        try:
            num_games = int(input("Please enter the amount of games:"))
            if num_games >= 0:
                break
            else:
                print("Please enter a positive number")
        except (ValueError, TypeError):
            print("Please enter a int")
    while True:
        try:
            prob_a = float(input("please enter the percentage Player A will win:"))
            if prob_a >= 0.0 and prob_a <= 1:
                break
            else:
                print("Please enter a percentage between 0 and 1")
        except (ValueError, TypeError):
            print("Please enter a float")
    return num_games, prob_a

def play_game(prob_a):
    num_games = 0
    plr_A = 0
    plr_B = 0
    A = 0
    B = 0
    points = ["0", "15", "30", "40", "Win"]
    deuce_Points = ["Deuce", "Advantage", "Win"]
    Win = False
    Deuce = False
    W = ""
    while (Win != True):
        while Deuce == True:
            if plr_A == deuce_Points[2] or plr_B == deuce_Points[2]:
                if plr_B == deuce_Points[2]:
                    Win = True
                    W = "B"
                    print("Winner: Player B")
                    return W
                elif plr_A == deuce_Points[2]:
                    Win = True
                    W = "A"
                    print("Winner: Player A")
                    return W
                
            if (random() < prob_a):
                A += 1
                plr_A = deuce_Points[A]
                if plr_A == deuce_Points[1]:
                    if (plr_A == deuce_Points[1] and plr_B == deuce_Points[1]):
                        A = 0
                        B = 0
                        plr_A = deuce_Points[A]
                        plr_B = deuce_Points[B]
                        print("Current score: deuce")
                    else:
                        if plr_B == deuce_Points[2]:
                            Win = True
                            W = "B"
                            print("Winner: Player B")
                            return W
                        else:
                            print("Current score: advantage Player A")
            if (random() > prob_a):
                B += 1
                plr_B = deuce_Points[B]
                if plr_B == deuce_Points[1]:
                    if (plr_A == deuce_Points[1] and plr_B == deuce_Points[1]):
                        A = 0
                        B = 0
                        plr_A = deuce_Points[A]
                        plr_B = deuce_Points[B]
                        print("Current score: deuce")
                    else:
                        if plr_A == deuce_Points[2]:
                            Win = True
                            W = "A"
                            print("Winner: Player A")
                            return W
                        else:
                            print("Current score: advantage Player B")
        else:
            if plr_A == points[4]:
                Win = True
                W = "A"
                print("Winner: Player A")
                return W
            if plr_B == points[4]:
                Win = True
                W = "B"
                print("Winner: Player B")
                return W
            else:
                if (random() < prob_a):
                    A += 1
                    plr_A = points[A]
                    if plr_A == points[4]:
                        Win = True
                        W = "A"
                        print("Winner: Player A")
                        return W
                    if (plr_A == points[3] and plr_B == points[3]):
                        Deuce = True
                        A = 0
                        B = 0
                        plr_A = deuce_Points[A]
                        plr_B = deuce_Points[B]
                        print("Current score: deuce")
                        continue
                    else:
                        print("Current score: ", plr_A, "-", plr_B)
                if (random() > prob_a):
                    B += 1
                    plr_B = points[B]
                    if plr_B == points[4]:
                        Win = True
                        W = "B"
                        print("Winner: Player B")
                        return W
                    if (plr_A == points[3] and plr_B == points[3]):
                        Deuce = True
                        A = 0
                        B = 0
                        plr_A = deuce_Points[A]
                        plr_B = deuce_Points[B]
                        print("Current score: deuce")
                        continue
                    else:
                        print("Current score: ", plr_A, "-", plr_B)

def play_games(num_games, prob_a):
    num_a_wins = 0
    num_b_wins = 0
    for x in range(num_games):
        W = play_game(prob_a)
        print("")
        if W == "A":
            num_a_wins += 1
        if W == "B":
            num_b_wins += 1
    return num_a_wins, num_b_wins

def print_summary(num_a_wins, num_b_wins):
    total_games = num_a_wins + num_b_wins
    v = num_a_wins/total_games
    percent = v * 100
    print("Here are the results:")
    print("Player A won", num_a_wins, "games.")
    print("Player B won", num_b_wins, "games.")
    print("Player A won", percent,"% of the games.")

def main():
    print_intro()
    num_games,prob_a = get_inputs()
    num_a_wins, num_b_wins = play_games(num_games, prob_a)
    print_summary(num_a_wins, num_b_wins)
    
main()

# Trevor Cardoza
# CS 21, Fall 2018
# Program: number puzzle

'''
Program that finds all 3-digit numbers that are sums of each individual
number in it cubed.
'''

import math
import sys

def main():
    amt = 0
    #Check for numbers 1-9 in the first spot.
    x = input("type in enter to begin: ")
    for x in range(1,10):
        #Check for numbers 0-9 in the second spot.
        for y in range(0,10):
            #Check for numbers 0-9 in the third spot.
            for z in range(0,10):
                #This is the equation of each number cubed.
                sum_of_cubes = (x**3)+(y**3)+(z**3)
                #if the answer is equal to 100*x + 10*y + z, then print
                #the answer.
                if sum_of_cubes == x*100 + y*10 + z:
                    amt += 1
                    print(sum_of_cubes)
                else:
                    amt += 1
                    if amt >= 900:
                        print("finished")
                        main()
                        
                        
main()

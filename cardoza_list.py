# Trevor Cardoza
# CS 21, Fall 2018
# Program: lists

"""
    Module description:
    
    File that sorts and reverses numbers.
"""

"""
    Description of reverse function:

    grabs numbers in list, sorts then spits in decreasing order.

"""
#Reverse is currently broken and dosent work as intended
def reverse(my_list, if_greater=False):
    for i in range(0,9):
        if not isinstance(my_list, list):
            return None
        if if_greater != True:
            my_list.sort()
            my_list.reverse()
        else:
            return None
    return my_list
def main():
    new_list = reverse([1,3,6,2,1,7])
    print (new_list)
    
main()

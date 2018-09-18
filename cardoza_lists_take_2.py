# Trevor Cardoza
# CS 21, Fall 2018
# Program: lists, take 2

"""
    Module description:
    
    File that sorts and reverses numbers.
"""

"""
    Description of reverse function:

    grabs numbers in list, sorts then spits in decreasing order.

"""

"""
    Description of isolate function:

    grabs an array and places all the ints in the array on the left side
    of the array and leaves the value on the right side.
    
"""
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

def isolate(array, value):
    for i in array:
        if i == value:
            array.remove(i)
            array.append(i)
    return array
def main():
    if_greater = False
    my_list = [1,2,3]
    print("The input list was: ", my_list)
    new_list = reverse(my_list, if_greater)
    print("The reverse function returns: ", new_list)
    array = [0,1,2,3]
    value = 2
    print("The input array was: ", array)
    new_array = isolate(array, value)
    print(new_array)

# Run the main function.
main()

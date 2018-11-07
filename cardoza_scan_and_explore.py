# Trevor Cardoza
# CS 21, Fall 2018
# Program: scan and explore

def scan(matrix, num_rows, num_cols):
    a=[]    #Odd rows.
    b=[]    #Even rows.
    l = False   #Whether it is a even(True) or odd(False) column.
    q = 0   #Num of columns.
    r = 0   #NUm of rows.
    if (len(matrix) != num_rows * num_cols
        or all(isinstance(x,int) for x in matrix) == False):
        return None
        #If any of these errors are met then
        #this program will return None.
    while r != num_rows:
    #Keeps going until out of rows.
        if num_cols != q:
        #Only passes if not equal to columns in each row.
            for x in matrix:
                q += 1
                #Move over one column.
                if l == False:
                #If Odd, then add to a.
                    a.append(x)
                elif l == True:
                #If Even, then add to b.
                    b.append(x)
                if q == num_cols and l == False:
                #When you have reached the end of the column
                #and it's Odd, then move down a row and make
                #it a Even row.
                    q = 0
                    r += 1
                    l = True
                    continue
                elif q == num_cols and l == True:
                #When you have reached the end of the column
                #and it's Even, then move down a row and make
                #it a Odd row.
                    q = 0
                    r += 1
                    l = False
                    b.reverse()
                    #Also, reverse the Even row to
                    #align with the matrix.
                    for s in b:
                        a.append(s)
                        #Combine the Even and Odd rows together
                        #going Odd then Even then Odd etc..\
                        continue
                    b.clear()
    return a
    #Return the completed list.
def explore(matrix, num_rows, num_cols):
    turn = 0    #Amount of turns.
    explore_pass = []   #Explore list of past nums.
    explore = []    #Explore list.
    q = 0   #Num of columns.
    r = 0   #Num of rows.
    if (len(matrix) != num_rows * num_cols or all(isinstance(x,int) for x in matrix) == False):
        return None
        #If any of these errors are met then
        #this program will return None.
    for e in matrix:    #makes the explore_pass list full of true.
            explore_pass.append(True)
    while r != num_rows: 
        if matrix[(r)*(num_cols) + q] % 2 == 0 and turn == 0:
        #Checks to see if the number is even or odd
        #then it will order it based on if it has been
        #passed or not.
        #This turn makes the curser go right.
            if q != num_cols-1:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    q += 1
                    continue
            if q == num_cols-1:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    return explore
        if matrix[(r)*(num_cols) + q] % 2 != 0 and turn == 0:
            if q != num_cols-1 or q == 0:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    r += 1
                    turn = 1
                    continue
            if q == num_cols-1 or q <= num_cols-num_cols:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    r += 1
                    turn = 1
                    continue
        if matrix[(r)*(num_cols) + q] % 2 == 0 and turn == 1:
        #This turn makes the curser go down.
            if q != num_cols-1 or q == 0:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    r += 1
                    continue
            if q == num_cols-1 or q <= num_cols-num_cols:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    r += 1
                    continue
        if matrix[(r)*(num_cols) + q] % 2 != 0 and turn == 1:
            if q != num_cols-1 or q == 0:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    q -= 1
                    turn = 2
                    continue
            if q == num_cols-1:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    q -= 1
                    turn = 2
                    continue
        if matrix[(r)*(num_cols) + q] % 2 == 0 and turn == 2:
        #This turn makes the curser go left.
            if q != 0:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    q -= 1
                    continue
            if q == 0:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    return explore
        if matrix[(r)*(num_cols) + q] % 2 != 0 and turn == 2:
            if q != num_cols-1 or q == 0:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    r -= 1
                    turn = 3
                    continue
            if q == num_cols-1:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    r -= 1
                    turn = 3
                    continue
        if matrix[(r)*(num_cols) + q] % 2 == 0 and turn == 3:
        #This turn makes the curser go up.
            if q != num_cols-1 or q == 0:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    r -= 1
                    continue
            if q == num_cols-1 or q <= num_cols-num_cols:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    r -= 1
                    continue
        if matrix[(r)*(num_cols) + q] % 2 != 0 and turn == 3:
            if q != num_cols-1 or q == 0:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    q += 1
                    turn = 0
                    continue
            if q == num_cols-1:
                if explore_pass[(r)*(num_cols) + q] == False:
                #if the index is equal to False return
                    return explore
                if explore_pass[(r)*(num_cols) + q] == True:
                    explore.append(matrix[(r)*(num_cols) + q])
                    explore_pass[(r)*(num_cols) + q] = False
                    q += 1
                    turn = 0
                    continue
    return explore

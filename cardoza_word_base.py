# Trevor Cardoza
# CS 21, Fall 2018
# Program: cardoza_word_base

'''
This program will take any sentence and remove all irrelevent words except
the code words. Then it will assign base-4 notation to each word then combine
them. After that, the program will transform the base-4 notation into base-10
notation.
'''

def convert(in_string):
    print(in_string)
    #This finds and deletes symbols that are not alphanumerical.
    outtab =  "                  "
    intab = "!@#$%^&*()_+<>?,./"
    trantab = in_string.maketrans(intab, outtab)
    in_string = (in_string.translate(trantab))
    my_word = ['the', 'quick', 'fox', 'dog']        #Code words
    my_base = [0, 1, 2, 3]      #Base-4 numbers
    equ_list = []       #Equation list
    #Combines the Code words and Base-4 numbers to create
    #a chart defining the words with the numbers.
    zipob = zip(my_word, my_base)
    dictofword = dict(zipob)
    print("code of string to base-4:",dictofword)
    #Runs through the split up words and checks to see if it is in the
    #list of code words.
    for i in in_string.split():
        if i in dictofword:
            if i in in_string.split():
                #This grabs the code words and assigns there base-4 code
                #number to the equation list.
                if i == my_word[0]:
                    w = str(my_base[0])
                    equ_list.append(w)
                elif i == my_word[1]:
                    x = str(my_base[1])
                    equ_list.append(x)
                elif i == my_word[2]:
                    y = str(my_base[2])
                    equ_list.append(y)
                elif i == my_word[3]:
                    z = str(my_base[3])
                    equ_list.append(z)

    print("base-4 equivalent","".join(equ_list))
    #Reverses numbers in list for easier calculating.
    equ_list.reverse()
    #Joins numbers in equation list together to create on number.
    thing = "".join(equ_list)
    var = (thing)
    pw = int(0)
    one = int(1)
    for r in (var):
        r = int(r)
        #This will take then reversed numbers in the list and times them by
        #4 to a increasing power.
        var = r * 4**(pw)
        r = int(var)
        #Removes the old number and replaces with the new base converted number.
        equ_list.remove(equ_list[-1 + 1])
        var = int(var)
        equ_list.append(var)
        pw += one
    t = 0
    for num in equ_list:
        #This line of code grabs the numbers from above and adds them together.
        #(var)+(var)...etc
        t += num
    out_num = t
    return out_num

string = input("type in a sentence that includes the, quick, fox or dog: ")
print(convert(string))

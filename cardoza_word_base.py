# Trevor Cardoza
# CS 21, Fall 2018
# Program: cardoza_word_base
 

#This program will take any sentence and remove all irrelevent words except
#the code words. Then it will assign base-4 notation to each word then combine
#them. After that, the program will transform the base-4 notation into base-10
#notation.


def convert(in_string):
    no_no = ["!", "@", "#", "$", "%", "^", "&","*", "(", ")", "_","+",
             "<", ">", "?", ",", ".", "/", "0", "1", "2","3","4","5","7",
             "8","9"] #non-alphanumerical
    my_word = ['the', 'quick', 'fox', 'dog'] #Code words
    equ_list = [] #Equation list
    for m in in_string:    #This finds and deletes symbols that are not
            if m in no_no: #alphanumerical.
                in_string = in_string.replace(m, "")
    for i in in_string.split(): #Runs through the split up words and
        if i in my_word:        #checks to see if it is in the
            if i == my_word[0]: #list of code words.
                equ_list.append(str(0))
            elif i == my_word[1]:
                equ_list.append(str(1))
            elif i == my_word[2]:
                equ_list.append(str(2))
            elif i == my_word[3]:
                equ_list.append(str(3))
        else:
            in_string = in_string.replace(i, "")
    equ_list.reverse() #Reverses numbers in list for easier calculating.
    thing = ""
    for t in equ_list: #Joins numbers in equation list together
        thing += str(t) #to create on number.
    var = (thing)
    pw = int(0)
    one = int(1)
    for r in (var):
        r = int(r)
        var = r * 4**(pw) #This will take then reversed numbers in the
        r = int(var)      #list and times them by 4 to a increasing power.
        equ_list.remove(equ_list[-1 + 1]) #Removes the old number and
        equ_list.append(int(var))         #replaces with the new base
        pw += one                         #converted number.
    t = 0
    for num in equ_list: #This line of code grabs the numbers from
        t += num         #above and adds them together.
    out_num = t          #Example: (var)+(var)...etc
    print(out_num)
    return out_num
convert("the quick fox jumps over the lazy dog")

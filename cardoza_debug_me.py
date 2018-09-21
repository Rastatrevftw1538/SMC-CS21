# Debugged by: Trevor Cardoza
# CS 21, Fall 2018
# Program: debug me

"""
    Module description:
    
    This program contains a collection of 4 functions:
    last_multiple(), censor(), transform(), and decimal_to_hexadecimal().
    Each accomplishes its own task, which is described in the block
    comment that precedes it. Each comment block also lists test cases
    that the function should pass.
    
"""

"""   
    The last_multiple() function takes 2 parameters, m and n, which are
    assumed to be positive integers. It returns the largest multiple of
    m that is less than or equal to n.

    Test cases:

    last_multiple(1, 5) should return 5
    last_multiple(3, 9) should return 9
    last_multiple(3, 10) should return 9
    last_multiple(7, 20) should return 14
        
"""

def last_multiple(m, n):
    
    # Enforce the assumption that m and n are positive integers.
    # If bad input is given, do not continue.
    assert(type(m) == int and type(n) == int)
    assert(n > 0 and m > 0)

    # Return the largest multiple of m that is less than or equal to n
    return n - (n % m)


"""
    The censor() function obscures 4-letter words in a string.
    The function has one parameter, in_string, which is assumed to be
    a string. All 4-letter words in the string are replaced by **** and
    the resulting string is returned. Words may include numbers and
    non-alphanumeric characters.

    Test cases:

    censor("I like my cat.") should return 'I **** my ****'
    censor("my book is here") should return 'my **** is ****'
    censor("No bad words here.") should return 'No bad words here.'
    censor("%%%% 2j*#n") should return '**** 2j*#n'
    
"""

def censor(in_string):
    
    # Enforce the assumption that in_string is a string.
    # If bad input is given, do not continue.
    assert(type(in_string) == str)

    # Initialize the output.
    out_string = " "

    # Iterate through all of the words in the input string.
    # If a word is a 4-letter word replace it by **** in the output.
    words = []
    for word in in_string.split():
        if len(word) == 4:
            words.append(4*"*")
        else:
            words.append(word)

    # Join together the new words and add them to the output.
    out_string = " ".join(words)

    return out_string


"""
    The transform() function transforms a given phrase into a coded
    sequence that is determined by shifting each letter in the phrase
    by a constant amount in the alphabet. The shift preserves
    capitalization and is done in a circular manner so that the letter
    after "z" is "a" and the letter after "Z" is "A". The transformed
    phrase is returned.

    The input phrase is assumed to be a string of letters and spaces,
    and the shift amount is assumed to be an integer.

    Test cases:

    transform("a", 0) should return 'a'
    transform("abc xyz", 1) should return 'bcd yza'
    transform("ABC XYZ", 2) should return 'CDE ZAB'
    transform("AbC xYz", -1) should return 'ZaB wXy
    transform("I love bagels", 20) should return 'C fipy vuayfm'
    transform("iemawum", 200) should return 'awesome'
    
"""

def transform(phrase, shift_amt):

    # Set up the allowed characters.
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    # Enforce the assumptions that the phrase parameter is a string made
    # up of letters and spaces and shift_amt is an integer.
    # If bad input is given, do not continue.
    assert(type(phrase) == str)
    for word in phrase.split():
        for letter in word:
            assert(letter in chars)
    assert(type(shift_amt) == int)

    # Initialize the output.
    transformed_phrase = ""

    # For each letter in the phrase, shift it in the alphabet by
    # the shift_amt and add the result to the output.
    for letter in phrase:
        if letter == " ":
            transformed_phrase += " "
        else:
            pos = chars.find(letter)
            if pos >= 26:
                base = 26
            else:
                base = 0
            newpos = base + (pos + shift_amt) % 26
            transformed_phrase += chars[newpos]

    return transformed_phrase


"""
    The decimal_to_hexadeimal() function performs a decimal (base-10)
    to hexadecimal (base-16) conversion. It takes one parameter, which
    is called value. The input is assumed to be a nonnegative integer
    that is expressed in decimal notation. It returns the hexadecimal
    representation of the input as a string that is prefixed by the
    convention "0x".

    The algorithm reduces the specified value by converting
    the remainder of its division by 16 to one of the following symbols:
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, or F.
    The quotient is then divided by 16 and a symbol is extracted again
    until the entire value is converted to hexadecimal.

    Test cases:

    decimal_to_hexadecimal(0) should return '0x0'
    decimal_to_hexadecimal(10) should return '0xA'
    decimal_to_hexadecimal(1000) should return '0x3E8'
    decimal_to_hexadecimal(10000) should return '0x2710'

"""

def decimal_to_hexadecimal(value):

    # Enforce the assumption that value is a positive integer.
    # If bad input is given, do not continue.
    assert type(value) is int
    assert value >= 0
    
    # Initialize the output.
    out = ""

    # If the value is positive then divide by 16 and convert the remainder
    # to a hexadecimal symbol.
    while value > 0.1:
        
        # Compute the remainder that results by performing integer division
        # by 16 on the value.
        remainder = value % 16

        # If the remainder is between 0 and 9 use it as the hexadecimal
        # symbol. If it is between 10 and 15 then use a letter instead,
        # where 10 maps to "A", 11 maps to "B", ... , and 15 maps to "F".
        if remainder < 10:
            out += "%d" % remainder
        else:
            out += chr(ord("A") + int(remainder) - 10)
            
        # Perform integer division by 16 on the value. This is
        # equivalent to moving one hexadecimal symbol to the left.
        value /= 16
    if value == 0.0:
        return "0x0"
    # Since symbols were appended right to left, the output string
    # must be reversed before returning it.
    return "0x"+ out[-2::-1]

#!/usr/bin/python3
''' A function that adds 2 intergers '''


def add_integer(a, b=98):

    ''' return an interger after adding a and b '''

    if type(a) == int:
        pass
    elif type(a) == float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) == int:
        pass
    elif type(b) == float:
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return a + b

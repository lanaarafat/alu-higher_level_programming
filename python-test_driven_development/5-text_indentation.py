#!/usr/bin/python3
''' prints a text with 2 /n after each character '''

def text_indentation(text):
    ''' print 2 lines after each character '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    c = 0
    for a in text:
        if c == 0:
            if a == ' ':
                continue
            else:
                c = 1
        if c == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                c = 0
            else:
                print(a, end="")

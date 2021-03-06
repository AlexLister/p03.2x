"""
Problem:

    The function 'balance' divides a piece of text into two equal halves.
    For example:  'turtle' -> 'tur' and 'tle'

    If words have an odd number of characters, it ignores the middle one:
    For example:  'turtles' -> 'tur' and 'les'

    Each letter is given a score, A=1, B=2 and so on, and a total score
    found for each half.

    If the first half has a greater score, it should print "Start"
    If the second half has a greater score, it should print "End"
    If they are the same, it should print "Balanced"


Tests:

    >>> balance("turtle")
    Start
    >>> balance("elephant")
    End
    >>> balance("gorilla")
    Start
    >>> balance("horse")
    End 
    >>> balance("kayak")
    Balanced

"""

# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code:
def balance(text):


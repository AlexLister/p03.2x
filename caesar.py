"""
Problem:

    Julius Caesar is credited with inventing one of the first ways
    of encrypting messages for transmission. A Caesar cipher works
    by replacing each of the characters in a piece of text with the
    character a certain number of spaces along in the alphabet.

    For example, if we moved 'APE' 3 along it would become 'DSH'.
    
    Moving past 'Z' should take us back to 'A'.

    The function 'encode' takes a piece of text and should move
    it along the alphabet n spaces.

    The function 'decode' should do the opposite.

    All text will be given in uppercase. No punctuation will be
    included, other than spaces - these should not be encoded.

Tests:

    >>> encode("APE", 3)
    DSH
    >>> encode("HELLO WORLD", 12)
    TQXXA IADXP
    >>> encode("JULIUS CAESAR", 9)
    SDURDB LJNBJA
    >>> decode("DSH", 3)
    APE
    >>> decode("SDURB LJNBJA", 9)
    JULIS CAESAR
    >>> decode("TQXXA IADXP", 12)
    HELLO WORLD

"""

# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code:
def encode(text, n):
    pos = 0
    order = 0
    newword = "" 
    length = len(text)
    for letter in range (length):
        pos = text[letter]
        if pos == " ":
            newword = newword + pos 
        else:
            order = ord(pos) + n
            if order > 90:
                order = (ord(pos) + n) - 26
            newletters = chr(order)
            newword = newword + newletters

    print(newword)
    
def decode(text, n):
    pos = 0
    order = 0
    newword = "" 
    length = len(text)
    for letter in range (length):
        pos = text[letter]
        if pos == " ":
            newword = newword + pos 
        else:
            order = ord(pos) - n
            if order < 65:
                order = (ord(pos) - n) + 26
            newletters = chr(order)
            newword = newword + newletters

    print(newword)

            


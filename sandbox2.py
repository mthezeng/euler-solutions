"""This sandbox serves as a dumping ground for random code and is not meant to be executed."""


"""
Before we remove the repeats from the list, we know there are 9801 terms in
this list, since there are 99 bases and 99 exponents to check, forming a square.
"""
def find_repeats():
    """repeatable_bases are bases <= 100 that themselves can be created by
    other exponents"""
    repeats = []
    repeatable_bases2 = [9**2, 8**2, 7**2, 6**2, 5**2, 4**2, 3**2, 2**2]
    repeatable_bases3 = [4**3, 3**3, 2**3]
    repeatable_bases4 = [3**4, 2**4]
    repeatable_bases5 = [2**5]
    repeatable_bases6 = [2**6]
    repeatable_bases = [repeatable_bases2, repeatable_bases3, repeatable_bases4,
        repeatable_bases5, repeatable_bases6]
    count = 0
    for b in repeatable_bases:
        for i in range(2, ):
            repeated_value = b ** i
            repeats.append(repeated_value)
    return 9801 - len(repeats)

def find_repeats():
    """repeatable_bases are bases <= 100 that themselves can be created by
    other exponents"""
    repeats = []
    repeatable_bases = [81, 64, 49, 36, 32, 27, 25, 16, 9, 8, 4]
    count = 0
    for b in repeatable_bases:
        for i in range(2, 51):
            repeated_value = b ** i
            if repeated_value not in repeats:
                repeats.append(repeated_value)
    return 9801 - len(repeats)


"""
Before we remove the repeats from the list, we know there are 9801 terms in
this list, since there are 99 bases and 99 exponents to check, forming a square.
"""
from copy import deepcopy

def find_repeats():
    """repeatable_bases are bases <= 100 that themselves can be created by
    other exponents"""
    repeats = []
    repeatable_bases = [81, 64, 49, 36, 32, 27, 25, 16, 9, 8, 4]
    count = 0
    #for b in repeatable_bases:
    return 9801 - len(repeats)

def generate_bases():
    bases = []
    for a in range(2,10):
        for b in range(2,7):
            current = []
            if a ** b < 100:
                current.append((a,b))
            bases.append(deepcopy(current))
    print(bases)
    return bases


if coins_available == [1]:
    # only 1 way to make 2 pounds using only 1 pc coins
    return 1
elif coins_available == [1, 2]:
    s, count = 2, 1
    while s < 200:

else:
    del coins_available[-1]
    return coin_sums(coins_available)

def tetration(value, tetronent):
    """tetronent refers to the length of the tetration tower

    >>> print(tetration(3,3))
    7625597484987
    """
    exp, digit = 0, value
    if tetronent != 1:
        exp = tetration(digit, tetronent-1)
        """builds new frames of tetration() with decreasing values
        until tetronent becomes 1 (i.e. until number of frames equals
        tetronent), passing digit each time"""
        digit = digit**exp
        """returns digit multiplied by exponent, going up each frame"""
    return digit

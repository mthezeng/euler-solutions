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

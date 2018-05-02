from timer import timed
from math import log10, floor

@timed
def champernowne():
    result = 1
    current = 0
    position = 1
    prev_position = position
    while prev_position <= 1000000:
        current += 1
        position += floor(log10(current)) + 1
        i = 0
        while prev_position != position:
            if log10(prev_position).is_integer():
                # print(current, prev_position, i)
                result *= int(str(current)[i])
            prev_position += 1
            i += 1 # tells us which digit in the number is interesting
    return result

print(champernowne())

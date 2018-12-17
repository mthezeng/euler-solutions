from timer import timed

"""
Returns the result of raising x to the yth power modulo m
Attribution: CS 70 notes on modular arithmetic:
http://www.eecs70.org/static/notes/n6.pdf
"""
def mod_exp(x, y, m):
    if y == 0:
        return 1
    else:
        z = mod_exp(x, y // 2, m)
        if y % 2 == 0:
            return (z * z) % m
        else:
            return (x * z * z) % m

"""
Returns the last 10 digits of the following sum:
(1 ** 1) + (2 ** 2) + ... + (n ** n)
"""
def self_powers(n):
    s = 0
    for i in range(1, n + 1):
        s += mod_exp(i, i, 10 ** 10)
    return s % (10 ** 10)

@timed
def main():
    print(self_powers(1000))

main()

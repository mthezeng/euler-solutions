from timer import timed

"""
Returns the last 10 digits of the following sum:
(1 ** 1) + (2 ** 2) + ... + (n ** n)
"""
def self_powers(n):
    s = 0
    for i in range(1, n + 1):
        s += pow(i, i, 10 ** 10)
    return s % (10 ** 10)

@timed
def main():
    print(self_powers(1000))

main()

from timer import timer

# Improved #

def sum_of_naturals_upto(n):
    return (n * (n + 1)) // 2

def improved(n):
    fives = 5 * sum_of_naturals_upto((n - 1) // 5)
    threes = 3 * sum_of_naturals_upto((n - 1) // 3)
    fifteens = 15 * sum_of_naturals_upto((n - 1) // 15)
    return fives + threes - fifteens

def main0():
    print(improved(1000))

timer(main0)

# Legacy #

def three_five_multiples(n):
    s = 0
    for i in range(n):
        if i % 5 == 0 or i % 3 == 0:
            s = s + i
    return s

def main1():
    print(three_five_multiples(1000))

timer(main1)

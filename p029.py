from timer import timer

def garbage():
    # fully brute-force solution to problem 29 of Project Euler
    distinct_powers = set()
    for a in range(2,101):
        for b in range(2,101):
            cur = a ** b
            distinct_powers.add(cur)
    print(len(distinct_powers))

timer(garbage)

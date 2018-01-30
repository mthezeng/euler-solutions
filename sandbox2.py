from timer import timer

def evenly_divisible():
    composite_divisors = [10,12,14,16,18]
    result = 0
    done = False
    while not done:
        result = result + 19*17*13*11*7*5*3*2 #prime numbers < 20
        for i in composite_divisors:
            if result % i != 0:
                done = True
    print(result)

timer(evenly_divisible)

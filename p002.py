from timer import timer
from fibonacci import fib_tree

def even_fibs(value):
    """returns sum of fibonacci numbers
    whose values do not exceed value"""
    s = 0
    current_fib = 1
    i = 1
    while current_fib < value:
        if current_fib % 2 == 0:
            s = s + current_fib
        current_fib = fib_tree(i)
        i += 1
    return s

def main():
    print(even_fibs(4000000))

timer(main)

# TV
def improved_fibby():
    """generator or something?"""
    def fibonacci(n):
        a,b = 1, 2
        for i in range(n):
            yield a
            a, b = b, a + b

    s = 0
    for f in fibonacci(100000):
        if f > 4000000:
            break
        elif f % 2 == 0:
            s += f

    print("Sum:", s)
    return s

timer(improved_fibby)

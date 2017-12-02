def fibonacci(n):
    #returns the nth fibonacci number
    x = 1
    if n > 0:
        x = fibonacci(n-1) + fibonacci(n-2)
    return x

def even_fibs(value):
    """returns sum of fibonacci numbers
    whose values do not exceed value"""
    s = 0
    current_fib = 1
    i = 1
    while current_fib < value:
        current_fib = fibonacci(i)
        if current_fib % 2 == 0:
            print(s,' ',current_fib)
            s = s + current_fib
        i += 1
    return s

print(even_fibs(4000000))


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

improved_fibby()

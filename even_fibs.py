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

from math import factorial as fact

def digit_factorials():
    result = []
    for x in range(10, 100000):
        if fact_digits_equal(x):
            result.append(x)
    print(result)
    return result

def fact_digits_equal(n):
    digits = list(map(int, str(n)))
    s = 0
    for d in digits:
        s += fact(d)
    return s == n

print(sum(digit_factorials()))

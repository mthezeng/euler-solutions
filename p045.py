from math import sqrt
triangle = lambda n: (n * (n + 1)) // 2
pentagonal_inverse = lambda y: (1 + sqrt(24*y + 1)) / 6
hexagonal_inverse = lambda y: (1 + sqrt(8*y + 1)) / 4

def check(y, t):
    p = pentagonal_inverse(y)
    h = hexagonal_inverse(y)
    if p.is_integer() and h.is_integer():
        print('T_{0}, P_{1}, and H_{2} is a solution!'.format(t, int(p), int(h)))
        return True
    else:
        return False

def main():
    n = 286
    while not check(triangle(n), n):
        n += 1
    print(triangle(n))

main()

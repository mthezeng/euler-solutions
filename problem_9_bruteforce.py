"""This is a brute-force solution using Euclid's formula for
finding Pythagorean triples"""

def pythagorean_triplet():
    a, b, c = 0, 0, 0
    m, n = 2, 1
    k = 25

    found = False
    while k < 100:
        a = k*((m**2) - (n**2))
        b = k*(2*m*n)
        c = k*((m**2) + (n**2))
        #print('({0}, {1}, {2})'.format(a,b,c))
        #print(a+b+c)
        if (a + b + c) == 1000:
            found = True
            break
        #elif (a + b + c) > 900 and (a+b+c) < 1200:
            #print(a, b, c, a + b + c)
        if m < 101 and n < 100:
            m += 1
        elif m == 101 and n < 100:
            n += 1
            m = n + 1
        elif n == 100:
            k += 1
            m, n = 2, 1
    if found:
        print("The solution is found!!!")
        return a*b*c
    else:
        print("The solution was not found within the constraints coded.")
        return None

print(pythagorean_triplet())

import numpy as np
from timer import timed

@timed
def pythongorean_triplet():
    r = np.arange(1, 499)
    x, y = np.meshgrid(r, r)
    z = np.sqrt(x**2 + y**2)

    for i in z.flatten():
        if float(i).is_integer() and 334.0 < i < 500.0:
            ar = x[np.where(z == i)]
            i = int(i)
            for j in range(len(ar)//2):
                if ar[j] + ar[-1-j] + i == 1000:
                    print('Found the triplet:', ar[j], ar[-1-j], i)
                    return ar[j] * ar[-1-j] * i
    # the function should never reach this case
    return 1

pythongorean_triplet()

# MZ

@timed
def inferior_triplet():
    def pythagorean_triplet():
        a, b, c = 0, 0, 0
        m, n = 2, 1
        k = 1

        found = False
        while k < 100:
            a = k*((m**2) - (n**2))
            b = k*(2*m*n)
            c = k*((m**2) + (n**2))
            if (a + b + c) == 1000:
                found = True
                break
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

inferior_triplet()

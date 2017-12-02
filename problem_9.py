import numpy as np


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

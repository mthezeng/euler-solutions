from math import sqrt
from math import ceil
import progressbar

def is_abundant(n):
    abundant = False
    divisors = [1]
    for i in range(2,ceil(sqrt(n))):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    if sum(divisors) > n:
        abundant = True
    return abundant

def non_abundants_list():
    bar = progressbar.ProgressBar()
    abundants = []
    non_abundant_sums = list(range(1,28124))
    for i in bar(range(12,28124)):
        if is_abundant(i):
            abundants.append(i)
            #print(abundants)
            for a in abundants:
                if (a + i) in non_abundant_sums:
                    del non_abundant_sums[non_abundant_sums.index(a + i)]
                #print(non_abundant_sums)
    return non_abundant_sums

print(sum(non_abundants_list()))

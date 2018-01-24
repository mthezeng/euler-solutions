import progressbar

def is_abundant(n):
    abundant = False
    divisors = [1]
    for i in range(2,n):
        if n % i == 0:
            divisors.append(i)
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
            for a in abundants:
                if (a + i) in non_abundant_sums:
                    del non_abundant_sums[non_abundant_sums.index(a + i)]
    return non_abundant_sums

print(sum(non_abundants_list()))

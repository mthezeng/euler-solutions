def two_abundants(abundant_numbers):
    """returns the sum of all numbers below 28123 that cannot be written
    as the sum of two abundant numbers"""
    bar = progressbar.ProgressBar()
    abundant_sums = []
    for x in abundant_numbers:
        for y in range(abundant_numbers.index(x),len(abundant_numbers)):
                abundant_sums.append(x + abundant_numbers[y])
                #print(abundant_sums)
    non_abundant_sums = list(range(1,28123))
    for n in bar(range(1,28123)):
        if n in abundant_sums:
            del non_abundant_sums[non_abundant_sums.index(n)]
    return sum(non_abundant_sums)

from timer import timed

def pythagorean_triples(upper):
    '''based on p009.py
    returns a dictionary of all pythagorean triples up to upper (noninclusive),
    with keys representing perimeters'''
    triples = {}
    a, b, c = 0, 0, 0
    m, n = 2, 1
    k = 1

    def reset(constant=1):
        """Euclid's formula
        https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
        """
        nonlocal a, b, c
        a = constant * ((m ** 2) - (n ** 2))
        b = constant * (2 * m * n)
        c = constant * ((m ** 2) + (n ** 2))

    while m < upper:
        n = 1
        reset()
        while m > n and n < upper:
            k = 1
            reset()
            sum = a + b + c
            while sum <= upper:
                reset(k)
                sum = a + b + c
                if sum >= upper:
                    break
                triple = [a, b, c]
                triple.sort()
                if sum in triples.keys():
                    if triple not in triples[sum]:
                        triples[sum].append(triple)
                else:
                    triples[sum] = [triple]
                k += 1
            n += 1
        m += 1

    return triples

@timed
def main():
    triples_dict = pythagorean_triples(1000)
    result = max(triples_dict, key=lambda x: len(triples_dict[x]))
    result_triples = triples_dict[result]
    print('{0} has {1} triples: {2}'.format(result, len(result_triples), result_triples))

main()

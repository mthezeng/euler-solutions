from timer import timed

def pythagorean_triples():
    # based on p009.py
    triples = {}
    a, b, c = 0, 0, 0
    m, n = 2, 1
    k = 1

    def reset():
        nonlocal a, b, c
        a = ((m ** 2) - (n ** 2))
        b = (2 * m * n)
        c = ((m ** 2) + (n ** 2))

    while m < 998:
        n = 1
        reset()
        while m > n and n < 998:
            k = 1
            reset()
            while (a + b + c) <= 1000:
                a = k * ((m ** 2) - (n ** 2))
                b = k * (2 * m * n)
                c = k * ((m ** 2) + (n ** 2))
                sum = a + b + c
                if sum >= 1000:
                    break
                triple = [a, b, c]
                triple.sort()
                #print(sum, k, triple)
                if sum in triples.keys():
                    if triple not in triples[a + b + c]:
                        triples[sum].append(triple)
                else:
                    triples[sum] = [triple]
                k += 1
            n += 1
        m += 1

    return triples

@timed
def main():
    triples_dict = pythagorean_triples()
    result = max(triples_dict, key=lambda x: len(triples_dict[x]))
    result_triples = triples_dict[result]
    print('{0} has {1} triples: {2}'.format(result, len(result_triples), result_triples))

main()

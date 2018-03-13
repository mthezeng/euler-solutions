from timer import timer

def is_pandigital_multiple(x):
    product = ''
    for n in range(1, 10):
        value = str(x * n)
        # check whether value contains duplicates
        if len(list(value)) != len(set(value)):
            return False, '', 0
        # check whether any of the digits of value are already in product
        # also check whether any of the digits of value are zero
        for d in value:
            if d in product or int(d) == 0:
                return False, '', 0
        # update product
        product += value
        if len(product) == 9:
            return True, product, n

def main():
    pandigital_multiples = []
    for x in range(1, 10000):
        # 10000 * 2 produces a five-digit number, taking the concatenated product beyond the 9-digit limit
        candidate, multiple, n = is_pandigital_multiple(x)
        if candidate:
            pandigital_multiples.append((x, multiple, n))
    result = max(pandigital_multiples, key=lambda s: s[1])
    print('{0} is the concatenated product of {1} with (1, ..., n) where n = {2}'.format(result[1], result[0], result[2]))

timer(main)

def is_pandigital(n1, n2, product):
    all_digits = list(range(1,10))
    combined_str = str(n1) + str(n2) + str(product)
    combined_str = list(map(int, combined_str))
    combined_str.sort()
    return all_digits == combined_str

def add_to_products(a, b, products):
    if is_pandigital(a, b, a * b):
        print('{0} * {1} = {2}'.format(a, b, a * b))
        products.add(a * b)

def pandigital_products():
    products = set()
    for a in range(1,10):
        for b in range(1000, 10000):
            add_to_products(a, b, products)
    for a in range(10, 100):
        for b in range(100, 1000):
            add_to_products(a, b, products)
    print(products)
    return products

print(sum(pandigital_products()))

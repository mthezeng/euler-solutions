def evenly_divisible(num):
    for i in range(2,21):
        if num % i != 0:
            return False
    return True

def smallest_multiple():
    x = 2520
    while True:
        if evenly_divisible(x):
            break
        x += 20
    return x

print(smallest_multiple())

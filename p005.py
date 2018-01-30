from timer import timer

def evenly_divisible(num):
    for i in range(2,21):
        if num % i != 0:
            return False
    return True

def smallest_multiple():
    x = 2520
    while not evenly_divisible(x):
        x += 20
    return x

def main():
    print(smallest_multiple())

timer(main)

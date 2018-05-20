from prime import prime_factors
from timer import timed

@timed
def main():
    print(max(prime_factors(600851475143)))

main()

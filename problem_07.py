from timer import timer

def primes(n):
    primes_list = [2,3,5,7,11,13]
    if n <= 6:
        return primes_list[0:n]
    i = primes_list[-1] + 1
    while len(primes_list) < n:
        prime = True
        for x in primes_list:
            if i % x == 0:
                prime = False
                break
        if not prime:
            i += 1
        else:
            primes_list.append(i)
    return primes_list

def get_user_n():
    user_value = 0
    while True:
        try:
            user_value = int(input('nth prime: '))
            break
        except ValueError:
            print('n must be an integer.')
    while user_value <= 0:
        print('Enter a value greater than 0.')
        user_value = int(input('nth prime: '))
    return user_value

def find_prime(nth):
    list_of_primes = primes(nth)
    nth_prime = list_of_primes[-1]
    print(nth_prime)

def main():
    nth = get_user_n()
    timer(find_prime,[nth])

if __name__ == "__main__":
    main()

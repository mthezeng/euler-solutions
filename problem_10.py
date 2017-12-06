from sys import stdout

def primes(primes_list):
    #Modified from problem_7.py
    s = sum(primes_list)
    i = primes_list[-1] + 1
    while primes_list[-1] < 1999992:
        #1999993 is the last prime number before 2000000
        prime = True
        for x in primes_list:
            if i % x == 0:
                prime = False
                break
        if not prime:
            i += 1
        else:
            digits = len(str(primes_list[-1]))
            delete = "\b" * (digits)
            print('{0}{1}'.format(delete,i), end="")
            stdout.flush()
            primes_list.append(i)
            s = s + i
    return s

list_of_primes = [2,3,5,7,11,13]
print('\n'+str(primes(list_of_primes)))

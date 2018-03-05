from timer import timer

def is_palindrome(n):
    # returns whether a given number n is a palindrome
    num_string = str(n)
    return num_string == num_string[::-1]

def to_binary(n):
    # converts the given integer in base 10 to base 2
    # source: https://stackoverflow.com/questions/3528146/convert-decimal-to-binary-in-python
    return int(bin(n)[2:])

def main():
    double_base_palindromes = []
    for i in range(int(1e6)):
        if is_palindrome(i) and is_palindrome(to_binary(i)):
            double_base_palindromes.append(i)
    print(sum(double_base_palindromes))

timer(main)

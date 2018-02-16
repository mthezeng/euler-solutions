from timer import timer

def is_palindrome(num_string):
    return num_string == num_string[::-1]

def three_digit_palindrome():
    list_palindromes = []
    for x in range(999,99,-1):
        for y in range(999,99,-1):
            if is_palindrome(str(x*y)):
                list_palindromes.append(x*y)
                #print('{0} times {1} is {2}'.format(x,y,x*y))
    return max(list_palindromes)

def main():
    print(three_digit_palindrome())

timer(main)

def is_palindrome(num_string):
    for i in range(len(num_string)//2):
        if num_string[i] != num_string[-i-1]:
            return False
    return True

def three_digit_palindrome():
    list_palindromes = []
    for x in range(999,99,-1):
        for y in range(999,99,-1):
            if is_palindrome(str(x*y)):
                list_palindromes.append(x*y)
                if x*y == 906609:
                    print('{0} times {1} is {2}'.format(x,y,x*y))
    return max(list_palindromes)

print('Largest is: ',three_digit_palindrome())

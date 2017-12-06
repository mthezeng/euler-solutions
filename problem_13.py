def addition_algorithm(numb3rs):
    """the elementary school addition algorithm
    numb3rs is a file object
    returns a list of digits corresponding to the sum of all numbers in numb3rs
    the list is in reverse order: the last digit appears first in the list
    
    Indeed, since python no longer has a maximum integer size, this can be brute-forced
    more straight-forwardly by adding the numbers directly. This solution is
    purely for the experience of coding the addition algorithm, and it can probably
    be flexibly translated into other programming languages that do have a
    maxmimum integer size."""
    sum_digits = []
    column_pos, row_pos = 1, 1
    carryover = 0
    current_column = []
    for c in range(50):
        for r in range(100):
            numb3rs.seek((51 * r) + (50 - (c + 1)))
            current_column.append(int(numb3rs.read(1)))
        current_sum = int(sum(current_column))
        if current_sum > 10:
            carryover = int((current_sum - (current_sum % 10)) / 10)
            if c < 49:
                current_sum = current_sum % 10
        sum_digits.append(current_sum)
        current_column = [carryover]
    return sum_digits

def first_ten_digits(sum_list):
    first_ten = ''
    i = -1
    stop = -11
    while i > stop:
        if sum_list[i] < 10:
            first_ten = first_ten + str(sum_list[i])
            i -= 1
        else:
            a_string = str(sum_list[i])
            digits = 0
            if sum_list[i] >= 100:
                digits = 3
                stop += 2
                i -= 1
            else:
                digits = 2
                stop += 1
                i -= 1
            for x in range(digits):
                first_ten = first_ten + a_string[x]
    return first_ten

fifty_digit_nums = open('50_digit_numbers.txt')
digit_list = addition_algorithm(fifty_digit_nums)
print(first_ten_digits(digit_list))

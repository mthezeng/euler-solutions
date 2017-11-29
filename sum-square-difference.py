def square(num):
    return num * num

def sum_100squares():
    s = 0
    for i in range(1,101):
        s = s + square(i)
    return s

def square_100sum():
    s = 0
    for i in range(1,101):
        s = s + i
    s = square(s)
    return s

sum_of_squares = sum_100squares()
square_of_sum = square_100sum()
diff = sum_of_squares - square_of_sum
print('{0} minus {1} equals {2}'.format(sum_of_squares, square_of_sum, diff))

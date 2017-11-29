import numpy as np

def sum_100squares():
    return int((100*101*201)/6)

def square_100sum():
    return int((101*100)/2) ** 2

sum_of_squares = sum_100squares()
square_of_sum = square_100sum()
diff = sum_of_squares - square_of_sum
print('{0} minus {1} equals {2}'.format(sum_of_squares, square_of_sum, diff))
# use absolute value

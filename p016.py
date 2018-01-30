def power_digit_sum(base, power):
    x = base ** power
    x_digits = str(x)
    x_digits = list(map(int, x_digits))
    return sum(x_digits)

print(power_digit_sum(2, 1000))

def power_digit_sum(base, power):
    x = 1
    for i in range(power):
        x = x * base
    x_digits = str(x)
    x_digits = list(map(int, x_digits))
    return sum(x_digits)

print(power_digit_sum(2, 1000))

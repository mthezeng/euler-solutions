def sum_digit_fifth_powers(n):
    s = 0
    num = n
    while num > 0:
        s = s + ((num % 10) ** 5)
        num = (num - (num % 10)) // 10
    return s

s = []
for i in range(2,354295):
    if i == sum_digit_fifth_powers(i):
        s.append(i)
print(sum(s))

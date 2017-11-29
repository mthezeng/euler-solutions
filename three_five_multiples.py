def three_five_multiples(n):
    s = 0
    for i in range(n):
        if i % 5 == 0 or i % 3 == 0:
            s = s + i
    return s

print(three_five_multiples(1000))

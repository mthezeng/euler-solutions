import progressbar

def collatz(num):
    #returns length of collatz sequence beginning with num
    counter = 1
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        counter += 1
    return counter

bar = progressbar.ProgressBar()
last_max, last_max_i = 0, 0
for i in bar(range(2, 1000000)):
    collatz_length = collatz(i)
    if collatz_length > last_max:
        last_max = collatz_length
        last_max_i = i
print('{0} has a chain with length {1}'.format(last_max_i, last_max))

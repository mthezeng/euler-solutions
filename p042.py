import string
from timer import timer

def words_gen():
    words_file = open('p042_words.txt')
    next_letter = words_file.read(1)
    while len(next_letter) > 0:
        word = ''
        next_letter = words_file.read(1) # drop the first quotation mark
        while next_letter != '\"': # stop building word at the second quotation mark
            word += next_letter
            next_letter = words_file.read(1)
        yield word
        words_file.read(1) # drop the comma
        next_letter = words_file.read(1) # get first letter of next word

def coded_sum(word):
    result = 0
    characters = list(word)
    for c in characters:
        result += string.ascii_uppercase.index(c) + 1
    return result

def triangle_numbers():
    n = 0
    while True:
        yield (n * (n+1)) / 2
        n += 1

def is_triangle_number(x):
    for t_num in triangle_numbers():
        if t_num == x:
            return True
        elif t_num > x:
            return False

def main():
    result = 0
    words = words_gen()
    for w in words:
        if is_triangle_number(coded_sum(w)):
            result += 1
    print(result)

timer(main)

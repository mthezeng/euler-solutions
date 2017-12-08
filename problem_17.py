def fundamental_num_letter(num):
    #num must be an integer between 0 and 19 inclusive for this function
    num_letters = 0
    if num == 0:
        #zero is never written unless it is by itself
        num_letters = 0
    elif num == 1 or num == 2 or num == 6 or num == 10:
        #one, two, six, and ten each have three letters
        num_letters = 3
    elif num == 4 or num == 5 or num == 9:
        #four, five, and nine each have four letters
        num_letters = 4
    elif num == 3 or num == 7 or num == 8:
        #three, seven, and eight each have five letters
        num_letters = 5
    elif num == 11 or num == 12:
        #eleven and twelve have six letters
        num_letters = 6
    elif num == 15 or num == 16:
        #fifteen and sixteen have seven letters
        num_letters = 7
    elif num == 13 or num == 14 or num == 18 or num == 19:
        #thirteen, fourteen, eighteen, and nineteen each have eight letters
        num_letters = 8
    elif num == 17:
        #seventeen has nine letters
        num_letters = 9
    return num_letters

def tens_num_letter(num):
    #num must be below 100 for this function
    num_letters = 0
    if num < 20:
        num_letters = fundamental_num_letter(num)
    elif num >= 40 and num < 70:
        #forty, fifty, sixty has five letters
        num_letters = 5 + fundamental_num_letter(num % 10)
    elif num < 40 or (num >= 80 and num < 100):
        #twenty, thirty, eighty and ninety have six letters
        num_letters = 6 + fundamental_num_letter(num % 10)
    elif num < 80:
        #seventy has seven letters
        num_letters = 7 + fundamental_num_letter(num % 10)
    return num_letters

def number_letter_count(n):
    #returns the number of letters in a given num written out
    num_letters = 0
    if n < 100:
        num_letters = tens_num_letter(n)
    elif n < 1000:
        #'hundred' has seven letters
        num_letters = fundamental_num_letter(int((n - (n % 100)) / 100)) + 7
        if n % 100 != 0:
            #'and' has three letters
            num_letters = num_letters + 3 + tens_num_letter(n % 100)
    elif n == 1000:
        #'one thousand' has eleven letters
        num_letters = 11
    return num_letters

def user_input_mode():
    # alternate version of the program to find lengths of individual numbers
    # chiefly debugging purposes
    x = int(input('Integer less than or equal to 1000: '))
    print(number_letter_count(x))

s = 0
end = int(input('Integer less than or equal to 1000: '))
for i in range(1, end + 1):
    s = s + number_letter_count(i)
print(s)
"""while True:
    user_input_mode()"""

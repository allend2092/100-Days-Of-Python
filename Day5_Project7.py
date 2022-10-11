# Day 5 project 7 - password generator
import random

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num_letters = int(input('How many letters would you like in your password?\n'))
    num_symbol = int(input('How many symbols would you like in your password?\n'))
    num_numbers = int(input('How many numbers would you like in your password?\n'))

    print(num_letters)
    print(num_symbol)
    print(num_numbers)

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '~']

    password = ''

    i = 0
    while i < (num_letters + num_symbol + num_numbers):
        lns_value = random.randint(1,4)
        if lns_value == 1:
            password = password + str(letters[random.randint(0,25)])
        elif lns_value == 2:
            password = password + str(numbers[random.randint(0,9)])
        elif lns_value == 3:
            password = password + str(symbols[random.randint(0,13)])
        else:
            password = password + str(letters[random.randint(0,25)].lower())
        i += 1

    print(password)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

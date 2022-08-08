import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '`', '~', '/', '.', ',', '<', '>', '?', '/', ':', ';', '[', ']', '{', '}', '|', '^', '-', '_']


letter_count = int(input("How many letters would you like in your password?"))
symbols_count = int(input("How many symbols would you like?"))
numbers_count = int(input("How many numbers would you like?"))

password = ''

def generate_passwrod(number, type):
    global password
    for _ in range(0, number):
        password += random.choice(type)

generate_passwrod(letter_count, letters)
generate_passwrod(numbers_count, numbers)
generate_passwrod(symbols_count, symbols)


pass_list = list(password)
random.shuffle(pass_list)
new_password = ''.join(pass_list)

print(new_password)
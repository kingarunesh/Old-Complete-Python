from random import choice

names = input("Give me everybody's name, seperated by a comma.\n")

name_list = names.split(', ')

name = choice(name_list).capitalize()


print(f"{name} is going to buy the meal today!")
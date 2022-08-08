import random

print("Welcome to the Love Calculator!")
your_name = input("What is your name?\n")
her_name = input("What is their name?\n")

both_name = your_name + her_name

t = both_name.count('t')
r = both_name.count('r')
u = both_name.count('u')
e = both_name.count('e')
 
l = both_name.count('l')
o = both_name.count('o')
v = both_name.count('v')
e = both_name.count('e')

true = t + r + u + e
love = l + o + v + e
love_score = f"{true}{love}"


# love_score = random.randint(0, 3)


print(f"Your score is {love_score}, you are alright together.")
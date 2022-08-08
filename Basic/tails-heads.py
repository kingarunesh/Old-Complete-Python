from random import randint


# 0 = tails
# 1 = heads

num = randint(0, 1)

if num == 0:
    print("Tails")
else:
    print("Heads")
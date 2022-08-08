a = 1

# normal while loop
while a < 6:
    print(a)
    a += 1


print()

# break
b = 1
while b < 6:
    print(b)
    if b == 3:
        break
    b += 1

print()

# continue
c = 0
while c < 6:
    c += 1
    if c == 3:
        continue
    print(c)
    

print()

# else
d = 0
while d < 6:
    print(d)
    d += 1
else:
    print("Loop end")
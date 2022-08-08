import math

height_list = input("Input a list of student heights: ")

heights = height_list.split(' ')


total = 0

for height in heights:
    total += float(height)


average_height = math.ceil(total / len(heights))

print(average_height)
from asyncio.windows_events import INFINITE

numbers = [73, 97, 72, 13, 94, 34]

max_value = 0
min_value = INFINITE


for number in numbers:
    # max value find
    if max_value < number:
        max_value = number
    # min value find
    if min_value > number:
        min_value = number


print(min_value)
print(max_value)

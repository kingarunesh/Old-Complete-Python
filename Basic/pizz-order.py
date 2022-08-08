size = input("What size pizza do you want? S, M, or L?\n").lower()
pepperoni = input("Do you want pepperoni? Y or N?\n").lower()
cheese = input("Do you want extra cheese? Y or N?\n").lower()


bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25


if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if cheese == "y":
    bill += 1


print(f"Your final bill is: ${bill}")

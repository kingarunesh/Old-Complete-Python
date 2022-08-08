print("Welcome to Tip Calculator")

bill = float(input("What was the total bill? "))
tip = float(input("How much bill would you like to give? 10, 12 or 15? "))
people = float(input("How many people to split the bill?"))


percentage_tip = (tip / 100) * bill

total_bill = percentage_tip + bill

bill_split = round(total_bill / people, 2)


print(f"Each person should pay: ${bill_split}")

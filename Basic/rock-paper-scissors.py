import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rps = [rock, paper, scissors]

computer_choose = random.choice(rps)

chose = int(input("Waht do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

user_rps = rps[chose]

print(user_rps)
print("Computer chose:")
print(computer_choose)


if computer_choose == user_rps:
    print("It's a draw")
elif user_rps == rock and computer_choose == scissors:
    print("You win!")
elif user_rps == paper and computer_choose == rock:
    print("You win!")
else:
    print("You lose")
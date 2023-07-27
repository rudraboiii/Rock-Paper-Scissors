# Rock, Paper Scissors Game
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

#Write your code below this line 👇
RPS_List = [rock, paper, scissors]

RPS_user_input = int(input("Press 0 for Rock, 1 for Paper and 2 for scissors\n"))
print(f"You choose: \n {RPS_List[RPS_user_input]}")

RPS_compuer_input = random.randint(0, 2)
print(f"Computer choose: \n {RPS_List[RPS_compuer_input]}")

# Rock

if RPS_user_input == 0 and RPS_compuer_input == 2:
    print("You Win")

elif RPS_user_input == 0 and RPS_compuer_input == 0:
    print("It's a draw")

elif RPS_user_input == 0 and RPS_compuer_input == 1:
    print("Tou Lose")



# Paper

if RPS_user_input == 1 and RPS_compuer_input == 0:
    print("You Win")

elif RPS_user_input == 1 and RPS_compuer_input == 1:
    print("It's a draw")

elif RPS_user_input == 1 and RPS_compuer_input == 2:
    print("Tou Lose")


# Scissors

if RPS_user_input == 2 and RPS_compuer_input == 1:
    print("You Win")

elif RPS_user_input == 2 and RPS_compuer_input == 2:
    print("It's a draw")

elif RPS_user_input == 2 and RPS_compuer_input == 0:
    print("Tou Lose")
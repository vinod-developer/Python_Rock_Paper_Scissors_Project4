import random

def rockPaperScissors(num):
    if num == "0":
        print(rock)
    elif num == "1":
        print(paper)
    elif num == "2":
        print(scissors)

print("Welcome to rock paper scissors game")
number = input("Pls type your number? 0,1 ,2 ")

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
rockPaperScissors(number)

computer_number = random.randint(0, 2)

print(f"Computer Chose {computer_number} ")

rockPaperScissors(str(computer_number))
computer_number_in_string = str(computer_number)
if number == computer_number_in_string:
    print("it's a tie")
elif number == "0":
    if computer_number_in_string == "1":
         print("You lose")
    elif computer_number_in_string == "2":
        print("You win")
elif number == "1":
    if computer_number_in_string == "2":
        print("You lose")
    elif computer_number_in_string == "0":
        print("You win")
elif number == "2":
    if computer_number_in_string == "0":
        print("You lose")
    elif computer_number_in_string == "1":
        print("You win")



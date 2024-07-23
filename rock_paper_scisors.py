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

"""
options = (rock, paper, scissors)


print('''
Welcome to the Rock, Paper, Scisors game.
These are the rules: 

Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
Please choose one when asked to.
Good luck.     
''')

user_choice = input("Choose your weapon: Rock, Paper or Scisors:\n ").lower()
computer_choice = random.choice(options)

print(f"Users chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

version1 = ("Rock wins against scissors.")
version2 = ("Scissors win against paper.")
version3 = ("Paper wins against rock.")


if computer_choice == scissors:
    print (version1)
elif computer_choice == paper:
    print (version2)
elif computer_choice == rock:
    print (version3)
    
"""
    
    
    
    
#Angela version

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

    


    






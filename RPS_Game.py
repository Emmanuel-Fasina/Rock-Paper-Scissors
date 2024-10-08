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

# Lists for choices and symbols respectively
choices = ["Rock", "Paper", "Scissors"]
symbols = [rock, paper, scissors]


# Function to determine the winner of a round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It is a draw!"
    elif user_choice == 0 and computer_choice == 2:
        return "You Win!"
    elif user_choice == 2 and computer_choice == 1:
        return "You Win!"
    elif user_choice == 1 and computer_choice == 0:
        return "You Win!"
    else:
        return "You LOSE!"


# Function to play the game for multiple rounds
def play_game(number_of_rounds):
    user_wins = 0
    computer_wins = 0

    for round_num in range(1, number_of_rounds + 1):
        print(f"Round {round_num}:")
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
        computer_choice = random.randint(0, 2)

        print("You choose:")
        print(choices[user_choice])

        if user_choice == 0:
            print(rock)
        elif user_choice == 1:
            print(paper)
        if user_choice == 2:
            print(scissors)

        print("Computer choose:")
        print(choices[computer_choice])
        if computer_choice == 0:
            print(rock)
        elif computer_choice == 1:
            print(paper)
        else:
            print(scissors)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "Win" in result:
            user_wins += 1
        elif "LOSE" in result:
            computer_wins += 1

        print(f"Your Wins: {user_wins}")
        print(f"Computer Wins: {computer_wins}")

        rounds_left = number_of_rounds - round_num
        if user_wins > rounds_left:
            print("Congratulations! You win!")
            break
        elif computer_wins > rounds_left:
            print("Sorry! You lose!")
            break


# Main program
num_rounds = int(input("How many rounds do you want to play? "))
play_game(num_rounds)

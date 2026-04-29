import random

def stone_paper_scissors(user_choice):
    options = ["stone", "paper", "scissors"]
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "Draw"
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You Win"
    else:
        result = "Computer Wins"

    return computer_choice, result


def dice_game():
    user = random.randint(1, 6)
    computer = random.randint(1, 6)

    if user > computer:
        result = "You Win"
    elif user < computer:
        result = "Computer Wins"
    else:
        result = "Draw"

    return user, computer, result
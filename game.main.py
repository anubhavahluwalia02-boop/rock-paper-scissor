from services import game_service

while True:
    print("\n====== GAME MENU ======")
    print("1. Stone Paper Scissors")
    print("2. Dice Roll Game")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user = input("Enter stone/paper/scissors: ").lower()
        if user not in ["stone", "paper", "scissors"]:
            print("Invalid choice")
        else:
            comp, result = game_service.stone_paper_scissors(user)
            print("Computer chose:", comp)
            print("Result:", result)

    elif choice == "2":
        user, comp, result = game_service.dice_game()
        print("You rolled:", user)
        print("Computer rolled:", comp)
        print("Result:", result)

    elif choice == "3":
        print("Game exited")
        break

    else:
        print("Invalid choice")
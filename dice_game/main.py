from game_service import single_player, two_player, multiple_rounds

def menu():
    print("\n====== 🎲 DICE GAME MENU ======")
    print("1. Single Player")
    print("2. Two Player")
    print("3. Multiple Rounds")
    print("4. Exit")

while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        single_player()

    elif choice == "2":
        two_player()

    elif choice == "3":
        multiple_rounds()

    elif choice == "4":
        print("👋 Thanks for playing!")
        break

    else:
        print("❌ Invalid choice!")
from dice import roll_dice

def single_player():
    print("\n🎲 Rolling Dice...")
    result = roll_dice()
    print(f"You rolled: {result}")

def two_player():
    print("\n🎲 Player 1 Rolling...")
    p1 = roll_dice()
    print(f"Player 1 rolled: {p1}")

    print("\n🎲 Player 2 Rolling...")
    p2 = roll_dice()
    print(f"Player 2 rolled: {p2}")

    if p1 > p2:
        print("\n🏆 Player 1 Wins!")
    elif p2 > p1:
        print("\n🏆 Player 2 Wins!")
    else:
        print("\n🤝 Match Draw!")

def multiple_rounds():
    rounds = int(input("Enter number of rounds: "))

    p1_score = 0
    p2_score = 0

    for i in range(1, rounds + 1):
        print(f"\n--- Round {i} ---")

        p1 = roll_dice()
        p2 = roll_dice()

        print(f"Player 1: {p1}")
        print(f"Player 2: {p2}")

        if p1 > p2:
            p1_score += 1
        elif p2 > p1:
            p2_score += 1

    print("\n📊 Final Scores")
    print(f"Player 1: {p1_score}")
    print(f"Player 2: {p2_score}")

    if p1_score > p2_score:
        print("🏆 Player 1 Wins the Game!")
    elif p2_score > p1_score:
        print("🏆 Player 2 Wins the Game!")
    else:
        print("🤝 It's a Tie!")
import random

choices = ["r", "p", "s"]


def play_game():
    wins = 0
    loses = 0
    ties = 0

    is_playing = True

    while is_playing:

        print("===============================================")
        user_choice = input(
            "Enter rock(r), paper(p), or scissors(s): ").lower()

        computer_choice = random.choice(choices)

        print(f"Player: '{user_choice}'")
        print(f"Computer: '{computer_choice}'")

        if user_choice == computer_choice:
            ties += 1
            print("Tie")
        elif user_choice == "r" and computer_choice == "p":
            loses += 1
            print("You lose.")
        elif user_choice == "p" and computer_choice == "s":
            loses += 1
            print("You lose.")
        elif user_choice == "s" and computer_choice == "r":
            loses += 1
            print("You lose.")
        elif user_choice == "p" and computer_choice == "r":
            wins += 1
            print("You win!")
        elif user_choice == "s" and computer_choice == "p":
            wins += 1
            print("You win!")
        elif user_choice == "r" and computer_choice == "s":
            wins += 1
            print("You win!")
        else:
            print("----------------------------")
            print("No result.")
            print("Please check your input...")
            print("Only enter 'r', 'p', or 's'.")
            print("----------------------------")
            continue

        while True:
            play_again = input("Play again? yes(y) or no(n): ")

            if play_again == "y":
                is_playing = True
                break
            elif play_again == "n":
                is_playing = False
                break
            else:
                print("Check input...")

    stats = {
        "wins": wins,
        "loses": loses,
        "ties": ties
    }

    print(stats)


if __name__ == "__main__":
    play_game()

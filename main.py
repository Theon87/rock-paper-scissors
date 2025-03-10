# Rock-Paper-Scissors
import random

choices = ["r", "p", "s"]


def play_game():

    is_playing = True

    while is_playing:
        # get user choice
        user_choice = input(
            "Enter rock(r), paper(p), or scissors(s): ").lower()
        # randomly generate computer choice
        computer_choice = random.choice(choices)
        # compare user choice to computer choice
        print(f"Player: '{user_choice}'")
        print(f"Computer: '{computer_choice}'")
        # determine winner
        if user_choice == computer_choice:
            print("Tie")
        elif user_choice == "r" and computer_choice == "p":
            print("You lose.")
        elif user_choice == "p" and computer_choice == "s":
            print("You lose.")
        elif user_choice == "s" and computer_choice == "r":
            print("You lose.")
        else:
            print("You win!")
        # prompt user to play again

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
        # if user quits, show tally of wins and loses


if __name__ == "__main__":
    play_game()

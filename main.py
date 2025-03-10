# Rock-Paper-Scissors
import random


def play_game():
    choices = ["r", "p", "s"]
    # get user choice

    is_playing = True

    while is_playing:
        user_choice = input(
            "Enter rock(r), paper(p), or scissors(s): ").lower()
        # randomly generate computer choice
        computer_choice = random.choice(choices)
        # compare user choice to computer choice
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
        play_again = input("Play again? yes(y) or no(n): ")

        if play_again == "y":
            is_playing = True
        else:
            is_playing = False
        # if user quits, show tally of wins and loses


if __name__ == "__main__":
    play_game()

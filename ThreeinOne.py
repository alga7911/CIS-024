from games import rock_paper_scissors
from games import heads_or_tails
from games import rng_guessing_game
import random

#Creating the menu for each of the games
def main_menu():
    print("Welcome to Three Games in One! Pick a Game to Play!")
    print("1. Rock, Paper, Scissors?")
    print("2. Heads or Tails?")
    print("3. Guess the Number?")
    print("q. Quit.")

def main():
    while True:
        main_menu()
        #Asks the player what game they want to play
        choice = input("Enter the number for the game you want to play, or press 4 to quit.")

        if choice == "1":
            rock_paper_scissors.play_game()
        elif choice == "2":
            heads_or_tails.play_HT()
        elif choice == "3":
            rng_guessing_game.play_rng()
        elif choice == "q":
            print("Thanks for trying Three Games in One!")
            break 
        else:
            #In the case if someone picks an invalid option.
            print("The command you picked isn't valid. Try Again.")

        play_again = input("Do you wish to return to the main menu? (Y/N): ").lower()
        if play_again != "y":
            print("Thanks for trying Three Games in One!")
            break
if __name__ == "__main__":
    main()
            

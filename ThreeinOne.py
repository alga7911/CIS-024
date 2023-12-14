import random

#Creating the menu for each of the games
def main_menu():
    print("Welcome to Three Games in One! Pick a Game to Play!")
    print("1. Rock, Paper, Scissors?")
    print("2. Heads or Tails?")
    print("3. Guess the Number?")
    print("q. Quit.")

#Code for rock, paper, and scissors.

    #this gets the players choice
def get_rps_user_choice():
    rps_user_choice = input("Type your choice (rock, paper, or scissors)")
    if rps_user_choice.lower() in ["rock", "paper", "scissors"]:
        return rps_user_choice.lower()
    else:
        #Ask the user to input a valid choice
        print("Choice wasn't valid. Pick either rock, paper, or scissors.")
    
    #this is for the computers choice
def get_rps_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
    
    #shows the choices the player and computer made
def rps_winner(rps_user_choice, rps_computer_choice):
    if rps_computer_choice == rps_user_choice:
        return "It's a tie!"
    elif (
        (rps_user_choice == "rock" and rps_computer_choice == "scissors") or
        (rps_user_choice == "paper" and rps_computer_choice == "rock") or
        (rps_user_choice == "scissors" and rps_computer_choice ==" paper")
    ):
        return("You win!")
    else:
        return("You lose.")

def rock_paper_scissors():
    print("Welcome to Rock, Paper, and Scissors!")

    rps_user_choice = get_rps_user_choice()
    rps_computer_choice = get_rps_computer_choice()
    
    print(f"Player, you chose {rps_user_choice}")
    print(f"The computer chose {rps_computer_choice}")

    result = rps_winner(rps_user_choice, rps_computer_choice)
    print(result)

pass

#Code for Heads or Tails
def heads_or_tails():
    pass

#Code for Guessing the Number
def rng_guessing_game():
    pass

def main():
    while True:
        main_menu()
        #Asks the player what game they want to play
        choice = input("Enter the number for the game you want to play, or press 4 to quit.")

        if choice == "1":
            rock_paper_scissors()
        elif choice == "2":
            heads_or_tails()
        elif choice == "3":
            rng_guessing_game()
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
            

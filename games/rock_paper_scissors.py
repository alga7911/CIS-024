import random

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

#Displays the welcome message for Rock, Paper, Scissors.
def play_game():
    print("Welcome to Rock, Paper, and Scissors!")

    rps_user_choice = get_rps_user_choice()
    rps_computer_choice = get_rps_computer_choice()
    
    print(f"Player, you chose {rps_user_choice}")
    print(f"The computer chose {rps_computer_choice}")

    result = rps_winner(rps_user_choice, rps_computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()     
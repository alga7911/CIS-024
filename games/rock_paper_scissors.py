import random

# Code for rock, paper, and scissors.

def get_rps_user_choice():
    rps_user_choice = input("Type your choice (rock, paper, or scissors): ")
    if rps_user_choice.lower() in ["rock", "paper", "scissors"]:
        return rps_user_choice.lower()
    else:
        print("Choice wasn't valid. Pick either rock, paper, or scissors.")

def get_rps_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def rps_winner(rps_user_choice, rps_computer_choice):
    if rps_computer_choice == rps_user_choice:
        return "It's a tie!"
    elif (
        (rps_user_choice == "rock" and rps_computer_choice == "scissors") or
        (rps_user_choice == "paper" and rps_computer_choice == "rock") or
        (rps_user_choice == "scissors" and rps_computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose."

# Logic for the one game
def play_one_game():
    rps_user_choice = get_rps_user_choice()
    rps_computer_choice = get_rps_computer_choice()
 
    print(f"Player, you chose {rps_user_choice}")
    print(f"The computer chose {rps_computer_choice}")

    result = rps_winner(rps_user_choice, rps_computer_choice)
    print(result)

# Logic for best of three
def best_of_three():
    player_wins = 0
    computer_wins = 0
    rounds = 0

    # Checks to see what round you're in
    while rounds < 3:  # Changed ">" to "<" to ensure it runs for three rounds
        rps_user_choice = get_rps_user_choice()
        rps_computer_choice = get_rps_computer_choice()

        print(f"Player, you chose {rps_user_choice}")
        print(f"The computer chose {rps_computer_choice}")

        result = rps_winner(rps_user_choice, rps_computer_choice)
        print(result)

        if result == "You win!":
            player_wins += 1
        elif result == "You lose.":
            computer_wins += 1

        rounds += 1  # Increment the rounds counter
        
    # Displays if you win, lose, or tie
    if player_wins > computer_wins:
        print("You beat the computer in a game of three!")
    elif player_wins < computer_wins:
        print("You lost to the computer. Try again!")
    else:
        print("It's a tie! Try to win next time!")

# Displays the welcome message for Rock, Paper, Scissors.
def play_game():
    print("Welcome to Rock, Paper, and Scissors!")
    while True:
        # Allows the player to choose a game mode
        game_mode = input("Choose how you want to play! (1 for one game, 3 for best of 3): ")
        while game_mode not in ['1', '3']:
            # In the case of a wrong input
            game_mode = input("Invalid choice selected. Please input 1 or 3: ")

        if game_mode == '1':
            play_one_game()

        elif game_mode == '3':
            best_of_three()
        
        play_again = input("Do you wish to play again? (Y/N): ").lower()
        if play_again != "y":
            print("Thanks for playing Rock, Paper, Scissors!")
            break

if __name__ == "__main__":
    play_game()

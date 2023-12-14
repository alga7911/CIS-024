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

#Displays the welcome message for Rock, Paper, Scissors.
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
    #chooses either heads or tails
    def coin_flip():
        return random.choice(["heads", "tails"])
    
    #Gets the users guess
    def HT_user_input():
        user_input = input("Guess either heads or tails: ").lower()
        while user_input not in ["heads", "tails"]:
            #in the case they don't choose heads or tails
            print("Invalid guess. Please choose heads or tails.")
            user_input = input("Guess either heads or tails: ").lower()
        return user_input
    
    #Welcome message for heads or tails game
    def play_HT():
        print("Welcome to Heads or Tails!")

        user_input = HT_user_input()
        coin_result = coin_flip()

        print(f"The coin has landed on {coin_result}.")

        #determines if the guess is correct
        if user_input == coin_result:
            print(f"You guessed {user_input}, which is right!")
        else:
            print(f"Sorry, you guessed {user_input}, which was wrong.")
    play_HT()
    pass

#Code for Guessing the Number
def rng_guessing_game():
    #This gives the user the ability to make the game easier or harder.
    def get_upper_limit():
        while True:
            try:
                upper_limit = int(input("Enter the limit for the game. (Higher the harder!)"))
                if upper_limit > 0:
                    return upper_limit
                else:
                    print("Choose a number thats greater than 0.")
            except ValueError:
             print("Invalid input. Try again!")

    #This will get a random number between 1 and whatever the user picked
    def rng_generation(upper_limit):
        return random.randint(1, upper_limit)
    #This is the part where the user guesses the number the code picked.
    def get_user_number(upper_limit):
        while True:
            try:
                user_number = int(input(f"Guess a number between 1 and {upper_limit}: "))
                if 1 <= user_number <= upper_limit:
                    return user_number
                else:
                    print(f"Enter a number between 1 and {upper_limit}: ")
            except ValueError:
                print("Invalid input. Please enter a valid number!")
    #Displays the winning message or a hint for the player.
    def rng_winner(secret_number, user_number):
        if user_number == secret_number:
            return "WOW! You guess the correct number!"
        elif user_number < secret_number:
            return "Too low, Try again!"
        else:
            return "Too high, Try again!"
    
    #Messaage when choosing 3
    def play_rng():
        print("Welcome to Guess the Number!")

        upper_limit = get_upper_limit()
        secret_number = rng_generation(upper_limit)

        attempts = 0
        max_attempts = 5 #This number can change to make it harder or easier.

        #logic for calculate the amount of attempts a player has
        while attempts < max_attempts:
            user_number = get_user_number(upper_limit)
            rng_result = rng_winner(secret_number, user_number)
            print(rng_result)

            #tells the player they won or lost and the amount of attempts it took.
            if user_number == secret_number:
                print(f"YOU GUESSES CORRECT! It took you {attempts + 1} attempts to get it!")
                break

            attempts += 1

        if attempts == max_attempts:
            print(f"Sorry, you didn't guess within {max_attempts} attempts. The correct answer was {secret_number}.")

    play_rng()
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
            

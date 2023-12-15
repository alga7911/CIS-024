import random

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
    if __name__ == "__main__":
        play_rng()
    
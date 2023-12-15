import random

#lets the user pick how easy or hard the game is
def get_upper_limit():
    while True:
        try:
            upper_limit = int(input("Enter the limit for the game. (Higher the harder!): "))
            if upper_limit > 0:
                return upper_limit
            else:
                print("Choose a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number!")

#picks a random number within the upper limit and 1
def rng_generation(upper_limit):
    return random.randint(1, upper_limit)

#This gets the users guess
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

#this is how the code displays the message if you win or lose. It also give the player hints.
def rng_winner(secret_number, user_number):
    if user_number == secret_number:
        return "WOW! You guessed the correct number!"
    elif user_number < secret_number:
        return "Too low, Try again!"
    else:
        return "Too high, Try again!"

#this is how the game starts
def play_rng():
    print("Welcome to Guess the Number!")

    upper_limit = get_upper_limit()
    secret_number = rng_generation(upper_limit)

    attempts = 0
    max_attempts = 5  # This number can change to make it harder or easier.

    while attempts < max_attempts:
        user_number = get_user_number(upper_limit)
        rng_result = rng_winner(secret_number, user_number)
        print(rng_result)

        #when the user guesses the number, it displays you win with how many attempts it took.
        if user_number == secret_number:
            print(f"YOU GUESSED CORRECT! It took you {attempts + 1} attempts to get it!")
            break

        attempts += 1

    #Use all your attempts then you lose
    if attempts == max_attempts:
        print(f"Sorry, you didn't guess within {max_attempts} attempts. The correct answer was {secret_number}.")

if __name__ == "__main__":
    play_rng()

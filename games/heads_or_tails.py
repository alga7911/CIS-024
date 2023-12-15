import random

#Gives two option of heads or tails
def coin_flip():
    return random.choice(["heads", "tails"])

#gets the user input for what they pick
def HT_user_input():
    user_input = input("Guess either heads or tails!: ").lower()
    while user_input not in ["heads", "tails"]:
        print("Invalid guess. Please choose heads or tails.")
        user_input = input("Guess either heads or tails: ").lower()
    return user_input

#Displays the welcome message
def play_HT():
    print("Welcome to Heads or Tails!")
    user_input = HT_user_input()
    coin_result = coin_flip()

    #prints results
    print(f"The coin has landed on {coin_result}.")

    #tells the player if they won or lost
    if user_input == coin_result:
        print(f"You guessed {user_input}, which is right!")
    else:
        print(f"Sorry, you guessed {user_input}, which was wrong.")

if __name__ == "__main__":
    play_HT()

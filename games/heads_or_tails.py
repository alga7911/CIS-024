import random

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

    if __name__ == "__main__":
        play_HT() 
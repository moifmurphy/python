import random

def game():
    # Generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []
    
    while len(guesses) < 5:
        try:
            # Get a number guess fromm the player
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            # Compare guess to the secret number
            if guess == secret_num:
                print("Nice! My number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("It's higher than {}".format(guess))
            else:
                print("It's lower than {}".format(guess))
            guesses.append(guess)
    else:
        print("YOU LOSE! My number was {}".format(secret_num))
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Seeya, loser")

game()
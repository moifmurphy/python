import os
import random
import sys

# make a list of words
words = [
    'computer',
    'coffee',
    'watch',
    'cap',
    'sunglasses',
    'coins',
    'wallet',
    'pens',
    'phone',
    'multitool',
    'monitor'
]


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print('')
    print('Strikes: {}/7'.format(len(bad_guesses)))

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_', end='')

    print('')



def get_guess(bad_guesses, good_guesses):
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("One letter at a time!")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter, genius")
            continue
        elif not guess.isalpha():
            print("Letters, dickhead. Letters.")
            continue
        else:
            return guess


def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False
            if found:
                print("That wasn't so hard, eh?")
                print("The word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("Game over, loser")
                print("The word was {}".format(secret_word))
                done = True

        if done:
            play_again = input("Try again? Y/n ").lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()

def welcome():
    start = input('Press enter/return to being the awesome or Q to return to your boring life').lower()
    if start == 'q':
        print('Yeah, seeya loser')
        sys.exit()
    else:
        return True

print('Welcome to the most amazing word guess game in the known universe')

done = False

while True:
    clear()
    welcome()
    play(done)
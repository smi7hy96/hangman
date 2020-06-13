from hangman import start_game
import time


print("WELCOME TO HANGMAN!")
user_play = False
while not user_play:
    user_input = input("Do you want to play? (Y/N) \n").upper()
    if user_input == 'Y':
        print("OKAY!! Generating word.... good luck!")
        time.sleep(1.5)
        start_game()
    else:
        print("Okay... Maybe next time :(")
        user_play = True


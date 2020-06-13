from random_word_generator import *


def start_game():
    word = RandomWordGenerator().get_word().upper()
    char_list = []
    answer_list = []
    letter_used = []
    lives = 10
    for letter in word:
        char_list.append(letter)
        if letter != '-':
            answer_list.append('_')
        else:
            answer_list.append(letter)
    print(print_answer_list(answer_list))
    while answer_list != char_list:
        a_guess = guess_letter(char_list, answer_list, letter_used)
        if a_guess[0] != 'False' and a_guess != "True":
            letter_used.append(a_guess[1])
            answer_list = a_guess[0]
        elif a_guess[0] == 'False':
            letter_used.append(a_guess[1])
            lives -= 1
        if lives == 0:
            break
        print(f'Letters Used: {sorted(letter_used)} Lives left: {lives}')
        print(print_answer_list(answer_list))

    if lives > 0:
        print("YOU WON! CONGRATULATIONS")
    else:
        print("You lost... RIP")
        print(lose_game())
        print(f'The word was {word}')


def guess_letter(char_list, answer_list, letter_used):
    found = False
    guess = ''
    while True:
        guess = input("Enter a Letter:").upper()
        if check_letter(guess):
            break
        else:
            print("Not a letter")
    if guess not in letter_used:
        for x in range(len(char_list)):
            if char_list[x] != '-':
                if guess in char_list[x]:
                    answer_list[x] = guess
                    letter_found = guess
                    print(f'letter {letter_found} FOUND!')
                    found = True
        if not found:
            print("Letter NOT FOUND")
            return 'False', guess
    else:
        print("letter already used")
        return 'True'
    return answer_list, letter_found


def check_letter(guess):
    for letter in guess:
        if len(guess) == 1:
            if letter.isalpha():
                return True
    return False


def print_answer_list(answer_list):
    return '   '.join(answer_list)


def lose_game():
    return '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= '''
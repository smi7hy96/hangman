from tkinter import *
from random_word_generator import *
from hangman_interface.hangman_stages import *


def user_submit():
    user_answer = user_input.get().upper()
    user_input.delete(0, 'end')
    print(user_answer)
    if lives == 0:
        end_of_game_string.set("You lost... RIP")
        hangman_drawing.set(hangman_stages[-1])
        hidden_answer.set(f'The answer was... {random_w}')
        submit_button.configure(text="PLAY AGAIN?", command=new_game)
    elif answer_list != char_list:
        check_guess(user_answer)
        lives_string.set(lives)
        hangman_drawing.set(hangman_stages[fail_count])
        change_label(answer_list)
        letters_used_string.set(letter_used)
        if answer_list == char_list:
            end_of_game_string.set("YOU WON CONGRATULATIONS")
            submit_button.configure(text="PLAY AGAIN?", command=new_game)


def check_guess(user_answer):
    found = False
    if check_letter(user_answer):
        if user_answer not in letter_used:
            for x in range(len(char_list)):
                if char_list[x] != '-':
                    if user_answer in char_list[x]:
                        answer_list[x] = user_answer
                        letter_found = user_answer
                        response.set(f'Letter {letter_found} FOUND!')
                        found = True
            if not found:
                response.set("Letter NOT FOUND")
                global lives
                lives -= 1
                global fail_count
                fail_count +=1
            letter_used.append(user_answer)
        else:
            response.set("Letter ALREADY USED")
    else:
        response.set("Not a letter")


def new_game():
    global random_w
    random_w = RandomWordGenerator().get_word().upper()
    global char_list
    char_list = []
    global answer_list
    answer_list = []
    global letter_used
    letter_used = []
    global lives
    lives = 10
    global fail_count
    fail_count = 0
    lives_string.set(lives)
    my_string.set('')
    hidden_answer.set('')
    response.set('')
    letters_used_string.set(letter_used)
    end_of_game_string.set('')
    hangman_drawing.set(hangman_stages[fail_count])
    for a_letter in random_w:
        char_list.append(a_letter)
        if a_letter != '-' or a_letter != ' ':
            answer_list.append('_')
        else:
            answer_list.append(a_letter)

    change_label(answer_list)
    submit_button.configure(text="Submit", command=user_submit)


def draw_hangman():
    hangman_drawing.set('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= ''')


def change_label(text):
    my_string.set(text)


def check_letter(guess):
    for letter in guess:
        if len(guess) == 1:
            if letter.isalpha():
                return True
    return False


random_w = RandomWordGenerator().get_word().upper()
fail_count = 0
char_list = []
answer_list = []
letter_used = []
lives = 10
root = Tk()
root.configure(background="light blue")
root.geometry("500x400+0+0")
frame_main = Frame(root, bg="white")
root.title('Hangman')

label_top = Label(frame_main, text="WELCOME TO HANGMAN \n Start Guessing!")
label_top.grid()

lives_string = StringVar(value=f'Lives: {lives}')
label_lives = Label(frame_main, textvariable=lives_string)
label_lives.grid()

my_string = StringVar(value='')
label_hidden = Label(frame_main, textvariable=my_string)
label_hidden.grid()

hidden_answer = StringVar(value='')
label_answer = Label(frame_main, textvariable=hidden_answer)
label_answer.grid()

user_input = Entry(frame_main)
user_input.grid()
user_input.bind("<Return>", (lambda event: user_submit()))

submit_button = Button(frame_main, text='Submit', command=user_submit)
submit_button.grid()
submit_button.configure(bg="light blue")

response = StringVar(value='')
label_response = Label(frame_main, textvariable=response)
label_response.grid()

letters_used_string = StringVar(value=letter_used)
label_used_letters = Label(frame_main, textvariable=letters_used_string)
label_used_letters.grid()

end_of_game_string = StringVar(value='')
label_finish = Label(frame_main, textvariable=end_of_game_string)
label_finish.grid()

hangman_drawing = StringVar(value=hangman_stages[fail_count])
hangman_label = Label(frame_main, textvariable=hangman_drawing)
hangman_label.grid()

quit_button = Button(frame_main, text='Quit', command=root.destroy)
quit_button.grid()
quit_button.configure(bg="light blue")

frame_main.grid(row=0, column=0)
frame_main.grid_rowconfigure(0, weight=1)
frame_main.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


allWidgets = [label_top, label_hidden, label_lives, user_input, label_response, label_used_letters, label_finish, hangman_label, label_answer]
for wid in allWidgets:
    wid.configure(bg="white")


for letter in random_w:
    char_list.append(letter)
    if letter != '-' or letter != ' ':
        answer_list.append('_')
    else:
        answer_list.append(letter)

change_label(answer_list)


root.mainloop()
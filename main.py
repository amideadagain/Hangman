import random
from sys import exit
from string import ascii_uppercase


def choose_word_list(word_type):
    word_list = tuple()
    if word_type.upper() == 'COUNTRIES' or word_type == '2':
        word_list = tuple(open('countries.txt').read().split('\n'))
    elif word_type.upper() == 'EXIT' or word_type == '3':
        exit()
    else:
        print('No such option')
    return word_list


def choosing_word(words):
    while not words:
        words: tuple = choose_word_list(input('What type of word?\n  1) food\n  2) countries\n  3) exit\n'))
    selected_word = random.choice(words)
    return selected_word


def index_fix(letter, lower_list, showing_list):  # index() returns only first instance so I wrote this
    letter_index = [i for i, x in enumerate(lower_list) if x == letter]
    for correct_index in letter_index:
        showing_list[correct_index] = letter


allowed_mistakes = 6
alphabet = tuple(ascii_uppercase)


def game_start(words_list):
    our_word = choosing_word(words_list)
    letter_list = tuple(our_word)
    print(letter_list)
    lower_list = list(our_word.lower())
    showing_list = list('#' * len(letter_list))
    showing_alphabet = list(alphabet)
    empty_string = ' '
    if empty_string in lower_list:
        index_fix(empty_string, lower_list, showing_list)
    mistakes = 0
    while showing_list != lower_list and mistakes < allowed_mistakes:
        print('_______________________________________________________________')
        letter = input(f'{empty_string.join(showing_alphabet)}\n{empty_string.join(showing_list)}\n').lower()
        if letter in lower_list:
            index_fix(letter, lower_list, showing_list)
        else:
            mistakes += 1
            print('incorrect')
        try:
            showing_alphabet[showing_alphabet.index(letter.upper())] = '-'
        except ValueError:
            print("You've just wrote some nonsense, or already chosen it previously")
    print(our_word)
    if mistakes < allowed_mistakes:
        print('Congrats!')
    else:
        print("You've lost!")


your_words_list = choose_word_list(input('What type of word?\n  1) food\n  2) countries\n  3) exit\n'))
while True:
    game_start(your_words_list)
    to_exit = input('Wanna play again?\n  1) yes\n  2) no\n')
    if to_exit == '2' or to_exit.upper() == 'NO':
        break

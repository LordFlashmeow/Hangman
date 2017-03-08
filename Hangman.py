import random
import PyDictionary

dictionary = PyDictionary.PyDictionary()

word_list = []
right_guesses = []
wrong_guesses = []
selected_word = ""
cheats = False
letters_left = 1
tries_left = 1
again = True
win = False
lose = False


def import_dictionary():

    try:
        file = open("usa.txt").read()
        print("Loading wordlist...\n")
        for word in file.split():
            word_list.append(word)

    except FileNotFoundError:
        print("Error, file not found.")


def select_word():
    global selected_word, tries_left, letters_left, right_guesses, wrong_guesses

    right_guesses = []
    wrong_guesses = []

    random.seed()
    index = random.randint(0, len(word_list))
    selected_word = word_list[index]

    if cheats:
        print("The selected word is:", selected_word)

    tries_left = 7
    letters_left = len(selected_word)


def display_letters():
    global selected_word, tries_left, letters_left

    gallows(len(wrong_guesses))

    letters_left = len(selected_word)
    printed_output = []
    for letter in selected_word:
        if not letter.isalpha():        # Display any non-alphabetical characters
            printed_output.append(letter)

        if letter in right_guesses:
            printed_output.append(letter)
            letters_left -= 1

        else:                           # Display unguessed letters as underscores
            printed_output.append("_ ")

    print("".join(printed_output))

    print(" ".join(wrong_guesses))


def user_input():
    global selected_word, tries_left

    new_letter = input("Enter a letter: ")
    new_letter = new_letter.lower()

    if new_letter in right_guesses or new_letter in wrong_guesses:
        print("You have already guessed that letter. Try again.")
        user_input()

    if new_letter in selected_word:
        right_guesses.append(new_letter)

    elif new_letter not in selected_word:
        wrong_guesses.append(new_letter)
        tries_left -= 1


def victory():
    global letters_left, tries_left, win, lose, selected_word

    letters_left = len(selected_word)

    printed_output = []

    for letter in selected_word:

        if letter in right_guesses:
            printed_output.append(letter)
            letters_left -= 1

    if letters_left == 0:
        win = True
        return True

    if tries_left == 0:
        lose = True
        return True
    else:
        return False


def game():
    global again
    select_word()
    while not victory():
        display_letters()
        user_input()
        print("\n")

    if lose:
        gallows(7)
        print("You lose! The word was:")
        define(selected_word)

    if win:
        print("You win! The word was:")
        define(selected_word)
    again = input("Do you want to play again? (y/n) ")
    if again.lower() == "y":
        again = True

    elif again.lower() == "n":
        again = False
        print("Thank you for playing.")


def define(word):
    counter = 0
    definition = dictionary.meaning(word)
    if definition:
        print(word.capitalize())
        for group in definition:
            print(group)

            for sentence in definition[group]:
                words = sentence.split()
                print(' - ', end='')

                for word in words:
                    print(word, '', end='')
                    if (counter + len(word)) >= 80:
                        print('\n   ', end='')
                        counter = 0
                    else:
                        counter += len(word)

                counter = 0

                print('')
            print('')
    else:
        print("Error: couldn't find the word")


def gallows(wrong_answers):
    """

    "_____________    "
    "|           |    "
    "|           o    "
    "|          o o   "
    "|           o    "
    "|           |    "
    "|          /|\\  "
    "|         / | \\ "
    "|           |    "
    "|          / \\  "
    "|         /   \\ "
    "|                "
    """


    # Show the bar of the gallows first

    if wrong_answers > 0:
        print("_____________   ")

    if wrong_answers == 0:
        print("_____________   ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")


    if wrong_answers > 1:
        print("|           |   ")
        print("|           |   ")
    if wrong_answers == 1:
        print("|           |   ")
        print("|           |   ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")

    if wrong_answers > 2:
        print("|           o   ")
        print("|          o o  ")
        print("|           o   ")

    if wrong_answers == 2:
        print("|           o   ")
        print("|          o o  ")
        print("|           o   ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|               ")

    if wrong_answers == 3:
        print("|           |    ")
        print("|           |    ")
        print("|           |    ")
        print("|                ")
        print("|                ")
        print("|                ")
        print("|                ")

    if wrong_answers == 4:
        print("|           |    ")
        print("|          /|    ")
        print("|         / |    ")
        print("|                ")
        print("|                ")
        print("|                ")
        print("|                ")

    if wrong_answers > 5:      # Completed upper body
        print("|           |    ")
        print("|          /|\\  ")
        print("|         / | \\ ")

    if wrong_answers == 5:
        print("|           |    ")
        print("|          /|\\  ")
        print("|         / | \\ ")
        print("|                ")
        print("|                ")
        print("|                ")
        print("|                ")

    if wrong_answers == 6:
        print("|           |    ")
        print("|          /     ")
        print("|         /      ")
        print("|                ")

    if wrong_answers >= 7:
        print("|           |    ")
        print("|          / \\  ")
        print("|         /   \\ ")
        print("|                ")

    if wrong_answers > 8:
        print("\nYou should be dead!")

import_dictionary()

while again:
    game()

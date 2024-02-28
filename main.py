"""
Hangman game.
Input:
    - We prepare list of words in file.
    - user inputs the letter
    - repeating input until user guess the word or lose

Output:
    - message to user, if the guess was right or not
    - drawing changes, depending on output

"""

import random
import hang_man

guessed_letters = []
correct_letters = []


def get_word():
    """ Get random word from word_library.

    1. Read contents of the file.
    2. Split the text into individual words.
    3. Return random word from the list.

    :return: random word
    :rtype: str
    """
    with open('word_library.txt', 'r') as file:
        # Read the contents of the file
        word_library = file.read()
    # Split the text into individual words
    words_list = word_library.split()
    # return random word from the list
    return random.choice(words_list)


def validate_input(a: str):
    """ Validating input.
    1. Check if input length is equal 1
    2. Check if input is letter
    3. Check if input (letter) was not guessed before and add it to guessed_letters list
    4. check if letter is in the word and if not, add it to guessed_letters list
    5. check if letters in current word, if so, append them to correct letters list

    :return: letter in lowercase
    :rtype: str
    """
    your_guess = a.lower()
    if not len(your_guess) == 1:
        print("Wrong input length. Please enter just ONE letter.")
    elif not your_guess.isalpha():
        print("Not a letter. Input must contain only one LETTER from alphabet")
    elif your_guess in guessed_letters or your_guess in correct_letters:
        print(f"You already guessed letter {your_guess}. Try another one.")
        display_word()
    elif your_guess not in current_word:
        guessed_letters.append(your_guess)
        print(f"There is NO letter - {your_guess} - in this word")
        display_word()
    elif your_guess in current_word:
        correct_letters.append(your_guess)
        print(f"Correct! There IS letter - {your_guess} - in this word")
        display_word()
    return your_guess


def display_word():
    """ Print current status of the guessed word
    unknown letters are printed as underscore.
    print list of guessed letters
    1. Check for known letters and print letter or _
    2. Print guessed letters

    """
    print("Your word is:", end=" ")
    for letter in current_word:
        if letter in correct_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
    print(f"Current guessed letters are: ", end="")
    for letter in guessed_letters + correct_letters:
        print(letter, end=" ")
    print()


def winning_conditions():
    """Check winning conditions.
    1. Check, if all letters is finished.

    :return: True
    :rtype: bool
    """
    if len(set(correct_letters)) == len(set(current_word)):
        print()
        print(f"Congratulations! You have guessed all letters correctly! \n"
              f"The answer is {current_word}.")
        return True


def losing_conditions():
    """Check losing conditions.
    1. Check how many guesses.
        if >= 6, then player lost.

    :return: True
    :rtype: bool
    """
    if len(guessed_letters) == 6:
        print()
        print(f"Six incorrect guesses. You lost the game and got hanged. \n"
              f"Correct answer is {current_word}. See you next time!")
        return True


def draw_hanged_man():
    """ display hang_man drawing from hang_man file.

    1. Depending on wrong guesses print hang_man drawing


    :return: one of hang_man drawings from hang_man.py
    :rtype: callable
    """
    if len(guessed_letters) == 1:
        return hang_man.draw_hanged_man_1()
    elif len(guessed_letters) == 2:
        return hang_man.draw_hanged_man_2()
    elif len(guessed_letters) == 3:
        return hang_man.draw_hanged_man_3()
    elif len(guessed_letters) == 4:
        return hang_man.draw_hanged_man_4()
    elif len(guessed_letters) == 5:
        return hang_man.draw_hanged_man_5()
    elif len(guessed_letters) == 6:
        return hang_man.draw_hanged_man_6()
    else:
        return hang_man.draw_hanged_man_0()


if __name__ == "__main__":
    current_word = get_word()
    # print bellow line temporary, if you want to check the word
    print(f"Temporary displayed for testing reasons. Word is: {current_word}")
    hang_man.draw_hanged_man_0()
    while True:
        user_input = input(f"Guess a letter: ")
        validate_input(user_input)
        draw_hanged_man()
        if winning_conditions():
            break
        if losing_conditions():
            break

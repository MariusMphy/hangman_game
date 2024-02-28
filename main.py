"""
Hangman game.
Input:
    - We prepare list of words in file.
    - user inputs the letter
    - user must guess the word

Output:
    - message to user, if the guess was right or not
    - drawing changes, depending on output

Steps.
1. Create vocabulary in separate file.
2. Create a function. Game starts by picking a word from vocabulary. Let user pick goals to end the game.
- Winning and losing conditions.
- Lose: The player makes six incorrect guesses.
- Win: The player guesses the word correctly.
3. Create an input for user to guess the letter.
4. Function to validate input. Must be single, lowercase letter. Can't guess same twice.
5. Function to display length of words using underscore. Display correct guessed letters and wrong guessed letters.
- And count wrong guesses.
6. Create draw_hanged_man function, to draw hangman.
7. Function to check if endgame conditions are met. Encapsulate it.
- Winning and losing conditions.
- Lose: The player makes six incorrect guesses.
- Win: The player guesses the word correctly.


"""

import random

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


def validate_input(func: callable):
    """ Validating input.
    1. Check if input length is equal 1
    2. Check if input is letter
    3. Check if input (letter) was not guessed before and add it to guessed_letters list
    4. check if letter is in the word and if not, add it to guessed_letters list
    5. check if letters in current word, if so, append them to correct letters list

    :return: letter in lowercase
    :rtype: str
    """
    def wrapper():
        your_guess = func().lower()
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
    return wrapper


def display_word():
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
              f"The answer is {current_word}")
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


@validate_input
def user_input():
    """User input.
    1. Receives user input

    :return: user input
    :rtype: str
    """
    print()
    a = input(f"Guess a letter: ")
    return a

def draw_hanged_man():
    for _ in range(6):
        print "_"



if __name__ == "__main__":
    # print temporary
    current_word = (get_word())
    print(current_word)
    # b = input(f"Guess a letter: ")
    count = 0
    while True:
        user_input()
        if winning_conditions():
            break
        if losing_conditions():
            break

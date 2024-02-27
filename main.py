"""
Hangman game.
Input:
    - We prepare list of words in file.
    - user writes in the letter
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


# temporary
print(get_word())


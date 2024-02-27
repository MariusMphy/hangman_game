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

guessed_letters = []


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
    3. Check if input (letter) was not guessed before

    :return: letter in lowercase
    :rtype: str
    """
    def wrapper():
        result = func().lower()
        if not len(result) == 1:
            # in this case I just print a message.
            print("Wrong input length. Please enter just ONE letter.")
            # in that case I raise error.
        elif not result.isalpha():
            raise ValueError("Not a letter. Input must contain only one LETTER from alphabet")
        elif result in guessed_letters:
            print(f"You already guessed letter {result}. Try another one.")
        elif result not in get_word():
            guessed_letters.append(result)
        # else place letter instead of underscore. prepare empty underscore displayed.



        print("Please enter the letter")
        return result
    return wrapper


def check_word():
    pass


def winning_conditions():
    """Check winning conditions.
    1. Check, if all letters is finished.

    :return: True
    :rtype: bool
    """
    pass

def losing_conditions():
    """Check losing conditions.
    1. Check how many guesses.
        if >= 6, then player lost.
    2. Check, if man is hanged.

    :return: True
    :rtype: bool
    """
    pass

@validate_input
def user_input():
    """User input.
    1. Receives user input

    :return: user input
    :rtype: str
    """
    a = "B"
    # a = input(f"Enter a letter: ")
    return a

#create letter

if __name__ == "__main__":
    # print temporary
    print(get_word())
    # count temporary
    count = 0
    while True:
        print(user_input())
        # temporary printed
        print(guessed_letters)

        #temporary
        count += 1
        if count == 3:
            break

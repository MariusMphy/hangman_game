import random
import hang_man


class Main:
    def __init__(self):
        self.guessed_letters = []
        self.correct_letters = []
        self.current_word = self.get_word()

    @staticmethod
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

    def validate_input(self, a: str):
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
        elif your_guess in self.guessed_letters or your_guess in self.correct_letters:
            print(f"You already guessed letter {your_guess}. Try another one.")
            self.display_word()
        elif your_guess not in current_word:
            self.guessed_letters.append(your_guess)
            print(f"There is NO letter - {your_guess} - in this word")
            self.display_word()
        elif your_guess in current_word:
            self.correct_letters.append(your_guess)
            print(f"Correct! There IS letter - {your_guess} - in this word")
            self.display_word()
        return your_guess

    def display_word(self):
        """ Print current status of the guessed word
        unknown letters are printed as underscore.
        print list of guessed letters
        1. Check for known letters and print letter or _
        2. Print guessed letters

        """
        print("Your word is:", end=" ")
        for letter in current_word:
            if letter in self.correct_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()
        print(f"Current guessed letters are: ", end="")
        for letter in self.guessed_letters + self.correct_letters:
            print(letter, end=" ")
        print()

    def winning_conditions(self):
        """Check winning conditions.
        1. Check, if all letters is finished.

        :return: True
        :rtype: bool
        """
        if len(set(self.correct_letters)) == len(set(current_word)):
            print()
            print(f"Congratulations! You have guessed all letters correctly! \n"
                  f"The answer is {current_word}.")
            return True

    def losing_conditions(self):
        """Check losing conditions.
        1. Check how many guesses.
            if >= 6, then player lost.

        :return: True
        :rtype: bool
        """
        if len(self.guessed_letters) == 6:
            print()
            print(f"Six incorrect guesses. You lost the game and got hanged. \n"
                  f"Correct answer is {current_word}. See you next time!")
            return True

    def draw_hanged_man(self):
        """ display hang_man drawing from hang_man file.

        1. Depending on wrong guesses print hang_man drawing


        :return: one of hang_man drawings from hang_man.py
        :rtype: callable
        """
        drawing_list = ["  O   |", " ---  |", "/ | \\ |", "  |   |", " ---  |", "/   \\ |",
                        "|   | |"]
        print("  -----")
        print("  |   |")
        for index, line in enumerate(self.guessed_letters):
            print(drawing_list[index])
        for item in range(7-len(self.guessed_letters)):
            if len(self.guessed_letters) == 6:
                print(drawing_list[6])
            else:
                print("      |")
        print("      |")
        print("-------")
        print(f"{6-len(self.guessed_letters)} incorrect guesses left.")


if __name__ == "__main__":
    hang_it = Main()
    current_word = Main.get_word()
    # print bellow line temporary, if you want to check the word
    print(f"Temporary displayed for testing reasons. Word is: {current_word}")
    hang_man.draw_hanged_man_0()
    while True:
        user_input = input(f"Guess a letter: ")
        hang_it.validate_input(user_input)
        hang_it.draw_hanged_man()
        if hang_it.winning_conditions():
            break
        if hang_it.losing_conditions():
            break

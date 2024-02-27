# Mini project exercises

The following is a list of bigger exercises to practice your programming skills, with an explicit focus to practice all topics covered until now. Some of these exercises are 
- (D) Described in detail. This is to train you for when your nice developer colleagues at work spell out what needs to be done in detail and all that's left is for you to implement it.
- (V) Very vague.  It's up to you to make a decision and interpret the requirements. For example, when clients ask you to implement something using vague words and they don't really know what they want themselves. This is in general more difficult as it involves more planning on your part.

General tips:
- Before starting writing code we *highly* recommend to plan your program. Use pen and paper or write comments at the top of your python file. 
  - What is the desired use of your program? How will you or the user interact with it? What are the inputs, what are the outputs?
  - What functions should you create? Why? Write small documentation for functions before implementing them
  - What classes should you create? Why is it appropriate to use OOP here?
  - Should you use inheritance? Should you use encapsulation (data hiding)?
  - It's almost always a good idea to implement magic methods like `__str__`, `__repr__`. Think about whether you will compare objects, then implement `__eq__`, `__ne__`, `__le__`, `__ge__`, etc.
  - Think about whether it is appropriate to use `@dataclass`, `@staticmethod`, `@classmethod`, or custom decorators.
- As mentioned before, write documentation for functions and classes!
- Use type hinting in functions!
- Use PEP8 style to make your code readable. Press `CTRL + ALT + L` often!
- Use `print()` calls or `logging` library often for debugging! If you run into problems, use Pycharm IDE debugger
- If it makes sense, separate your functions and classes into distinct files.  
- Use `git` and `github` to keep track of your project and show it to others. Use informative commit messages and push small changes often!


## Tank exercise (D)

Your task is to develop in python a simple [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface) tank game. You will implement this exercise in stages, each stage is a bit more difficult and *builds upon* the previous stage. That is, please develop the same file iteratively or create a separate file each time where you copy from the previous stage, creating files `tank_stage1.py`, `tank_stage2.py`, etc.

Start with the given file `tank_game.py` because it has some starting code to make it easier for you.

```
# tank_game.py

class TankGame:
    def __init__(self, N: int = 7):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        """
        self.N = N
        # Hard-coded starting tank location is 2, 1
        self.tank_loc_x = 2
        self.tank_loc_y = 1
        # Starting direction: tank facing north/up
        self.direction = "up"

    def print_map(self):
        """Print the current map of the game.

        Example output for a 7x7 map:
           0  1  2  3  4  5  6
        0  .  .  .  .  .  .  .
        1  .  .  T  .  .  .  .
        2  .  .  .  .  .  .  .
        3  .  .  .  .  .  .  .
        4  .  .  .  .  .  .  .
        5  .  .  .  .  .  .  .
        6  .  .  .  .  .  .  .

        where T is the location of the tank,
        where . (the dot) is an empty space on the map,
        where the horizontal axis is the x location of the tank and,
        where the vertical axis is the y location of the tank.
        """
        # Print the numbers for the x axis
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            # Print the numbers for the y axis
            print(f"{i} ", end="")
            for j in range(self.N):
                if self.tank_loc_x == j and self.tank_loc_y == i:
                    print(" T ", end="")
                else:
                    print(" . ", end="")
            print()

    def steer_left(self):
        # TODO implement this
        pass

    # TODO: add more methods here


if __name__ == "__main__":
    # Initialize your game object
    tg = TankGame()
    # Start game loop
    while True:
        tg.print_map()

        command = input("Input a command: ")
        if command == "left":
            tg.steer_left()
        # TODO: add more command handling here...

```


### Stage 1

All tank and information management must be done on the console (actual graphical interface is not required). This will require you to create a menu and accept user instructions. Actions to be performed (methods called) until the user stops the program (for example, by selecting an actual menu item). You can use this management to test your TankGame class during your coding process.

Class: TankGame

Methods to implement: print_map (already implemented), forward, backward, steer_left, steer_right, shoot, info, ...

Store the following variables in the class:
- Tank coordinates.
- Direction of the tank.
- Number of shots in each direction.

The tank can move forward (to the North), to the right (to the East), back (to South), left (West) by one position. For example "the tank is moving left," meaning it turned 90 degrees and moved through one unit to the West.

A tank can only fire in the direction it is facing.

The `info()` method must display:
- Which direction the tank is currently facing.
- What are its coordinates.
- How many total shots did it make.
- How many shots were fired in each direction separately.

![picture](https://github.com/robotautas/kursas/raw/master/tanko%20iliustracija.png)

Text translation: this is only an illustration of the idea of the game, you don't need this kind of graphical interface, we work in the console only.

### Stage 2

Improve the program so that:
- A target is generated in the tank game grid. 
- The task of the tank is to be in the right position and in the right direction so that a hit is recorded after firing. 
- When a tank hits, we see the message "hit" on the console and a new target is generated immediately. 

### Stage 3

Improve the program further:
- Come up with a point system, e.g. start with 100 points, +50 points for hits, -10 points for each forward drive, sum up total hits. 
- Show the points next to the game grid. 
- When the points run out, the program shows how many targets have been shot down and ends. 
- Perhaps it is possible to store high scores - after the end, the name is entered and the player with the number of downed targets is recorded in the charts. 
- The charts can perhaps be viewed with the 'top' command. 

### Stage 4

Come up with some improvements of your own! Document the functions well and provide info for the player at the start of the game of your changes.

## Hangman (D)

How it looks like [here](https://i.vimeocdn.com/video/1727623664-abc3c668b087e48ec826f30ef75a285dada9f1fc4c3a45eba37c254f3a0406cd-d?mw=700&mh=393). 

### Step 1: Set Up the Hangman Project

Your hangman game will select a word, handle user input, and display all output using a text-based user interface. You need code to handle each of these tasks. However, you’ll do everything using built-in and standard-library tools. You don’t need to install anything else.

### Step 2: Select a Word to Guess

The first step in playing hangman is to select the target word. When a human player selects a word for hangman, they pick one word from their own vocabulary. For the computer to select a word, it needs to have a vocabulary from which to select. Of course, its vocabulary doesn’t need to be as large as a human’s.

### Step 3: Get and Validate the Player’s Input

Now, you need a way to get the player’s guesses at the command line. After all, a game isn’t much of a game if there isn’t some way for the player to influence the outcome.

In your hangman game, you have to get the player’s input and make sure that it’s valid. Remember when you created your list of words? All the words were in lowercase, so you should turn the player’s guesses into lowercase letters as well.

Additionally, the player shouldn’t be able to guess the same letter twice. It’d also be good to avoid numbers, special characters, and complete words as well.

### Step 4: Display the Guessed Letters and Word

Once you’ve selected the target word in a real-life game of hangman, you need to write an underscore, or blank, for each letter in the word. These blanks tell the players how many letters are in the target word. As players make guesses, you fill in the blanks with the correct letters. You should also keep track of incorrect letters, which you write to the side.

### Step 5: Draw the Hanged Man

Of course, there’s no hangman game without the actual hanged man, is there? You could simply print out the number of guesses the player has taken. But if you want to make the game look like hangman, then showing the hanged man is a good idea.
Implement a function `draw_hanged_man` that, depending on the integer passed, will show different ASCII pictures 

```
>>> draw_hanged_man(0)
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------

>>> draw_hanged_man(6)
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
```

### Step 6: Figure Out When the Game Is Over

Games normally end due to a condition set up by the player’s input. Perhaps the player has finally reached the goal, or they failed some task and lost the game.

Your hangman game ends when one of two events happens:

- The player makes six incorrect guesses.
- The player guesses the word correctly.

Both of these outcomes stem from the player’s input. So, it makes sense to check for them in the game loop, which is where you gather, validate, and process all player input. Encapsulating these checks into a function is a good idea as well.

### Step 7: Run the Game Loop

Up to this point, you’ve assembled the functions and code that cover most of the important parts of your hangman game. Those parts include the following:

1. Selecting a random word to guess
2. Gathering and processing the player’s input
3. Showing the word with unguessed letters hidden
4. Showing the hanged man drawing
5. Tracking the letters guessed and guesses taken
6. Checking if the game is over

## Task app (V)

Create a program where you can track a list of your tasks. With each task, you should be able to specify its name, priority, and deadline.
- You can keep track of your tasks inside a `tasks.txt` file which your program would constantly modify. You can use a simple text format but we recommend using JSON or CSV because it should be easier to work with it.
- You can implement your program that, once you run it, you can input your desired arguments using a CLI-like commands (similar to [Tank](#tank-exercise-d) exercise above)
- Alternatively, your application could benefit from [parsing arguments](https://docs.python.org/3/howto/argparse.html#argparse-tutorial). 
For example, you could run it as 
```bash
python todo.py --add "Do dishes" --priority 2 --deadline "2024-02-24 12:00"
```
where the words with `--` such as `--add` are called python program options and the words 
following those, such as `"Do dishes"` are the arguments. In this case, you would indicate 
that you like to _add_ the task "Do dishes" as a task.

For example, interaction with your application could look like this (this is using arguments, but similar idea would work for CLI applications):
```bash
>>> python todo.py --add "Do dishes" --priority 2 --deadline "2024-02-24 12:00"
Task added successfully! Here is the current list:
2. Do dishes. Due date: 2024-02-24 12:00
>>> python todo.py --add "Do laundry" --priority 1 --deadline "2024-02-24 11:00"
Task added successfully! Here is the current list:
1. Do laundry. Due date: 2024-02-24 11:00
2. Do dishes. Due date: 2024-02-24 12:00
>>> python todo.py --add "Call grandma" --priority 2 --deadline "2024-02-24 15:00"
Task added successfully! Here is the current list:
1. Do laundry. Due date: 2024-02-24 11:00
2. Do dishes. Due date: 2024-02-24 12:00
2. Call grandma. Due date: 2024-02-24 15:00
>>> python todo.py --del "Do laundry"
Task deleted successfully! Here is the current list:
2. Do dishes. Due date: 2024-02-24 12:00
2. Call grandma. Due date: 2024-02-24 15:00
>>> python todo.py --del
Latest task deleted successfully! Here is the current list:
2. Call grandma. Due date: 2024-02-24 15:00
>>> python todo.py --edit "Call ganma" --name "Call mom" --priority 3 --deadline "2024-02-25 17:00"  
Unfortunately, "Call ganma" task currently does not exist. Try again!
Here is the current list of tasks:
2. Call grandma. Due date: 2024-02-24 15:00
>>> python todo.py --edit "Call grandma" --name "Call mom" --priority 3 --deadline "2024-02-25 17:00"  
Task edited successfully! Here is the current list:
3. Call mom. Due date: 2024-02-25 17:00
```

## Wordle (V)

Create a [Wordle](https://en.wikipedia.org/wiki/Wordle) clone in python. You can use [colorama](https://pypi.org/project/colorama/) to set colors to printed outputs, check its documentation to understand how to use it.

## Rolling dice (V)

Demo of the app [here](https://files.realpython.com/media/python-dice-roll-demo.93e6fe0d714a.gif).

## Flashcard app (V)

Build a [flashcard](https://en.wikipedia.org/wiki/Flashcard) app. 

- Your flashcards can be stored in a TXT, JSON, CSV or other format in some file. 
- Implement some logic which retrieves the cards using [spaced repetition](https://www.khanacademy.org/science/learn-to-learn/x141050afa14cfed3:learn-to-learn/x141050afa14cfed3:spaced-repetition/a/l2l-spaced-repetition).
- Example usage could look similar to [this](https://github.com/bttger/markdown-flashcards) but feel free to create your own!

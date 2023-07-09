 # ahorcadoPython

#### This repository is the first project for ADA course using Python.

This is a hangman game implemented in Python. The program selects a random word from a predefined list, and the user tries to guess the word by entering individual letters. The user has a limited number of attempts to guess the word correctly.

## Libraries
The following library is used in this program:
- `random`: Used to select a random word from the word list.

## Variables
The program uses the following variables:
- `words`: A list of words that the user can guess.
- `life_count`: The number of attempts/lives the user has.
- `wrong_letters`: A list to store the wrong letters guessed by the user.
- `right_letters`: A list to store the correct letters guessed by the user.

## Functions
The program includes the following functions:
- `selectWord(words_list)`: Selects a random word from the given word list and returns it as well as a string of underscores representing the unknown letters.
- `identifyLettersInWord(word)`: Returns the distinct letters present in the given word.
- `checkIfLetterInWord(letter, word)`: Checks if the given letter is present in the word and updates the `right_letters` and `wrong_letters` lists accordingly. Returns a boolean indicating if the letter is in the word.
- `losingLife(life_count, notLessLife)`: Checks if the user selected a correct letter and updates the life count accordingly. Returns the updated life count.
- `replaceUnderscoresWithLetter(letter, word, unknown_word)`: Replaces the underscores in the `unknown_word` with the correctly guessed `letter` at the corresponding positions in the `word`. Returns the updated `unknown_word`.
- `checkIfUnderscoresRemaining(unknown_word)`: Checks if there are any underscores remaining in the `unknown_word`. Returns a boolean indicating if there are underscores remaining.

## Execute Game
The main game execution is performed in this section. It starts by selecting a random word and displaying the number of letters as underscores. Then, it enters a loop where the user is prompted to enter a letter. The input is validated, and if it is a single letter, it checks if it is present in the word. The `right_letters`, `wrong_letters`, and `life_count` are updated accordingly. The game continues until the user correctly guesses the word or runs out of lives.

## How to Run
To run the hangman game, execute the Python script. The program will guide you through the game, prompting you to enter letters to guess the word.





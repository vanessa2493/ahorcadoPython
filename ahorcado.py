 ## Libraries##
import random


 ## Variables ##
# List of words the user can access to play
words = ["aeropuerto", "hospital", "programadora", "saturno", "escaleras"]

# The number of attemps the user has
life_count = 5

# The list in which the wrong letters per attempt would be added and shown to the user
wrong_letters = []

# The list in which the right letters per attemp would be added and showed to the user
right_letters = []


## Functions ##

# This function selects a random word and transforms it into underscores
def selectWord (words_list:list) -> tuple:
    random_word = random.choice(words_list)
    unknoun_word= "_"*len(random_word)
    return random_word , unknoun_word

# This function gives the distinct letters of a word
def identifyLettersInWord (word:str) -> str:
    setLetters = set(word)
    return setLetters

# This function checks if a letter is present in a word
def checkIfLetterInWord (letter:str, word:str) -> bool:
    if letter in word:
        return True
    else:
        return False
    
# This function checks if the user selects a correct letter and if not the user losses a life
def losingLife (life_count:int, notLessLife:bool) -> int:
    if notLessLife:
        life_count 
    else:
        life_count = life_count - 1
    return life_count

# This function returns the unknown word with a string of underscores with the replacements of each underscore with the correct letter inputted by an user
def replaceUnderscoresWithLetter (letter:str, word:str, unknoun_word:str) -> str :
    positions = []
    counter = 0
    word_list = [*word]
    unknoun_word_list = [*unknoun_word]

    for l in word_list:
        if l == letter:
            positions.append(counter)
        counter += 1
    print(positions) 

    for p in positions:
        unknoun_word_list[p] = letter
    print(unknoun_word_list)
    word_string = ''.join(unknoun_word_list)
    print(word_string)

    return word_string

# This function tells if there are underscores remaining
def checkIfUnderscoresRemaining (unknoun_word:str):
    unknoun_word_list = [*unknoun_word]
    
    return "_" in unknoun_word_list
    









random_word, unknoun_word = selectWord(words)
print(random_word)
letters = identifyLettersInWord(random_word)
print(letters)
check = checkIfLetterInWord("e", random_word)
print(check)
life_count = losingLife(life_count,check)
print(life_count)
unknoun_word = replaceUnderscoresWithLetter("e",random_word,unknoun_word)
check2= checkIfUnderscoresRemaining(unknoun_word)
print(check2)

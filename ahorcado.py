 ## Trabajo Práctico presentado por Vanessa
 ## 9 Julio 2023


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

# 
def selectWord(words_list:list) -> tuple:
    """This function selects a random word and transforms it into underscores

    Args:
        words_list (list)

    Returns:
        tuple
    """
    random_word = random.choice(words_list)
    unknoun_word= "_"*len(random_word)
    return random_word , unknoun_word

# 
def identifyLettersInWord(word:str) -> str:
    """This function gives the distinct letters of a word

    Args:
        word (str)

    Returns:
        str
    """
    setLetters = set(word)
    return setLetters

# 
def checkIfLetterInWord(letter:str, word:str) -> bool:
    """This function checks if a letter is present in a word

    Args:
        letter (str)
        word (str)

    Returns:
        bool
    """
    if letter in word:
        right_letters.append(letter)
        print("Letras incorrectas: ", wrong_letters)
        print("Letras correctas: ", right_letters)
        return True
    else:
        wrong_letters.append(letter)
        print("Letras incorrectas: ", wrong_letters)
        print("Letras correctas: ", right_letters)
        return False
    
# 
def losingLife(life_count:int, notLessLife:bool) -> int:
    """This function checks if the user selects a correct 
    letter and if not the user losses a life

    Args:
        life_count (int)
        notLessLife (bool)

    Returns:
        int
    """
    if notLessLife:
        life_count 
    else:
        life_count = life_count - 1
    return life_count

# 
def replaceUnderscoresWithLetter(letter:str, word:str, unknoun_word:str) -> str :
    """This function returns the unknown word with a string of underscores with 
    the replacements of each underscore with the correct letter inputted by an user

    Args:
        letter (str)
        word (str)
        unknoun_word (str)

    Returns:
        str
    """
    positions = []
    counter = 0
    word_list = [*word]
    unknoun_word_list = [*unknoun_word]

    for l in word_list:
        if l == letter:
            positions.append(counter)
        counter += 1

    for p in positions:
        unknoun_word_list[p] = letter
        
    word_string = ''.join(unknoun_word_list)

    return word_string

# 
def checkIfUnderscoresRemaining(unknoun_word:str) -> bool:
    """This function tells if there are underscores remaining

    Args:
        unknoun_word (str)

    Returns:
        bool
    """
    unknoun_word_list = [*unknoun_word]
    return "_" in unknoun_word_list
    
 

## Execute Game ##

random_word, unknoun_word = selectWord(words)

print("Bienvenidx al juego AHORCADO") 
print(f"La palabra que va a divinar tiene {len(unknoun_word)} letras")

while (checkIfUnderscoresRemaining(unknoun_word) and life_count >= 0):

    if life_count == 0:
        print("Ya no tiene vidas, Perdió :( ")
        break

    print(' '.join(list(unknoun_word)))

    letter_input = input("Ingrese una letra: ")

    if len(letter_input) == 1 and letter_input.isalpha():

        letters_set = identifyLettersInWord(random_word)
        
        check = checkIfLetterInWord(letter_input, random_word)

        life_count = losingLife(life_count,check)

        unknoun_word = replaceUnderscoresWithLetter(letter_input,random_word,unknoun_word)

        if checkIfUnderscoresRemaining(unknoun_word) == False:
            print(f"Ha adivinado la palabra que es: '{unknoun_word}', \nGanó :) ")
        else:
            print(f"Le quedan {life_count} vidas")
    
    else:
        print("Debe ingresar una letra")



## END




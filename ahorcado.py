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


# Functions

def selectWord (words_list):
    random_word = random.choice(words_list)
    unknoun_word= "_"*len(random_word)
    return random_word , unknoun_word

import random

words = ["keyboard", "python", "owen", "blue", "tyrannosaurus"]
random_word = random.choice(words)
blanks = []
letter = input("Guess a letter: ")

def rand_word(self): # Funcion to count the number of letters in random word
    count = 0

    for i in random_word:
        count += 1
    print(count)
    return count
    

def word_blanks(self): # Function to print out blanks for the random word.
    
    for i in random_word:
        blanks.append("_")
    
    word_blanks = " ".join(blanks)

    print(word_blanks)

    return word_blanks

def validate_input(letter): # Check to see if the user input is a letter
    while True:
        if letter.isalpha():
            return True
        else:
            input("Please enter a letter: ")
            return False

def letter_in_word(letter, random_word): # Function to check is Users letter is in word
    word = []
    
    for l in random_word:
        word.append(l)
    
    if letter in random_word:
        print("You guessed right")
    else:
        print("Guess again")


rand_word(rand_word)
word_blanks(word_blanks)
validate_input(letter)
letter_in_word(letter, random_word)



print(random_word)
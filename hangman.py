import random

words = ["keyboard", "python", "owen", "blue", "tyrannosaurus"]
random_word = random.choice(words)
blanks = []

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


rand_word(rand_word)
word_blanks(word_blanks)



print(random_word)
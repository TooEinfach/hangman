import random

words = ["keyboard", "python", "owen", "blue", "tyrannosaurus"]
random_word = random.choice(words)
blanks = []
guess_count = 1

print("Welcome to Hangman")

def menu():
    print("-" * 30 + "Menu" + "-"* 30)
    print("1 - Guess letter ")
    print("2 - Guess Word")
    print("3 - Quit")

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
            break
        else:
            letter = input("Please enter a letter: ")
            

def letter_in_word(letter, random_word, guess_count): # Function to check is Users letter is in word
    word = []

    for l in random_word:
        word.append(l)
    
    while guess_count <= 15:
        if letter in word:
            print("There is a/an " + letter)
            print(guess_count)
            letter = input("Guess another letter: ")
        else:
            letter = input("Guess again: ")
            print(guess_count)
        guess_count += 1
    
    if guess_count >= 15:
        print("Sorry you lose please play again the word was " + random_word)

def main():
    while True:
        menu()
        choice = input("? ")

        if choice.isdigit():
            if 1 == choice <= 3:
                print("You picked " + choice)
                break
            else:
                choice = input("Please enter a number between 1 and 3: ")
        else:
            choice = input("Please enter a number between 1 and 3: ")

if __name__ == "__main__":
    main()
# menu()
# rand_word(rand_word)
# word_blanks(word_blanks)
# validate_input(letter)
# letter_in_word(letter, random_word, guess_count)



print(random_word)
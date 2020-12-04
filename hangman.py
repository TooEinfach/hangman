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
    

def word_blanks(rand_word): # Function to print out blanks for the random word.
    
    for i in random_word:
        blanks.append("_")
    
    word_blanks = " ".join(blanks)

    return word_blanks

def validate_input(letter): # Check to see if the user input is a letter
    while True:
        if letter.isalpha():
            return letter
        else:
            letter = input("Please enter a letter: ")
            return letter
            

def letter_in_word(letter, random_word, guess_count): # Function to check is Users letter is in word
    word = []
    print(letter)

    for l in random_word:
        word.append(l)
    
    while guess_count <= 15:
        letter = validate_input(letter) # had to do this so that when number put in the vaildate letter when returned set for the rest of the function.
        
        if letter in word:
            print("There is a/an " + letter)
            return letter
            
        else:
            print("There is no " + letter)
            return             

            # print(guess_count)
        guess_count += 1
    
    if guess_count >= 15:
        print("Sorry you lose please play again the word was " + random_word)

def main():
    while True:
        menu()
        print("Your word is " + word_blanks(random_word))
        choice = int(input("Select Your option:  "))

        if 1 == choice <= 3:
            if choice == 1:
                letter = input("Please guess a letter: ")
                letter_in_word(letter, random_word, guess_count)
            elif choice == 2:
                pass
            elif choice == 3:
                print("Please come back and play again")
                break
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
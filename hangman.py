import random

words = ["keyboard", "python", "owen", "blue", "tyrannosaurus", "triceratops", "deinonychus", "compsognathus", "black", "nephi"]
random_word = ""
blanks = []
word = []
guess_count = 1

print("Welcome to Hangman")

def menu():
    print("-" * 30 + "Menu" + "-"* 30)
    print("1 - Guess letter ")
    print("2 - Guess Word")
    print("3 - Quit")
    print()

def rand_word(self): # Funcion to count the number of letters in random word
    count = 0

    for i in random_word:
        count += 1
    return count
    

def word_blanks(random_word): # Function to print out blanks for the random word.
    
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
            
def guess_word(random_word, guess_count, round_word):
    user_guess = input("Guess your word: ")

    # while True:
    if user_guess == random_word:
        print("YOU GOT IT YOU WIN!!")
        print()
        return            
    else:
        print("Sorry that guess was wrong")
        print()
        # guess_count += 1
        # print(guess_count)
        # return guess_count
        playgame(random_word, round_word, guess_count)

def word_by_letters(rand_word, word):

    for l in random_word:
        word.append(l)
    return word
    
def fill_in_the_blank(letter, blanks, word):
    indices = [i for i, x in enumerate(word) if x == letter]
    
    for i in indices:
        blanks[i] = letter
    return blanks

def letter_in_word(letter, random_word, guess_count,round_word, word, blanks): # Function to check is Users letter is in word


    

    if letter in word:
        print("There is a/an " + letter)
        fill_in_the_blank(letter,blanks, word)
        round_word = " ".join(blanks)

        if blanks == word:
            print("YOU GOT IT YOU WIN!! Your word was: " + random_word)
            return
        
        playgame(rand_word, round_word, guess_count)
        
    else:
        print("There is no " + letter)
        playgame(rand_word, round_word, guess_count)   

    

                  

def playgame(rand_word, round_word, guess_count):
    guess_count += 1
    while guess_count <= 15:
        menu()
        print("Your word is: " + round_word)
        print()
        try:
            choice = int(input("Select Your option:  "))
        except ValueError:
            print("Please select an number between 1 and 3")
            print()
            continue
        
        if 1 <= choice <= 3:
            if choice == 1:
                letter = input("Please guess a letter: ")
                letter_in_word(letter, random_word, guess_count, round_word, word, blanks)
            elif choice == 2:
                guess_word(random_word, guess_count, round_word)
            elif choice == 3:
                print("Please come back and play again")
                break
        else:
            choice = input("Please enter a number between 1 and 3: ")
        return
    return guess_count

def main():
    global random_word, blanks, guess_count, word
    random_word = random.choice(words)
    round_word = word_blanks(random_word)
    word_by_letters(random_word, word)
    while True:
        playgame(random_word, round_word, guess_count)

        if guess_count <= 15:
            print("Please come back and play again.")

        play_again = input("Would you like to play again Y/N: ").lower()
        if play_again == "y":
            blanks = []
            word = []
            random_word = random.choice(words)
            main()
            
        elif play_again == "n":
            print("Come back and play again")
            break
        
        
    


if __name__ == "__main__":
    main()
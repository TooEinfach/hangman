import random

words = ["keyboard", "python", "owen", "blue", "tyrannosaurus"]
# count = 0
random_word = random.choice(words)

def rand_word(rand_word):
    count = 0

    for i in random_word:
        count += 1
    print(count)
    return count
    


# print("Random word test: " + random_word)
rand_word(rand_word)
# print(count)
print(random_word)
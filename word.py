# 21MCA0066 ankit singh rajwar
# Coditation Assignment

import random


def games_func(words, guess):
    outputs = ['-', '-', '-', '-', '-']
    for i in range(0, 5):
        found = words.find(guess[i])
        if(found != -1):
            if(word[i] == guess[i]):
                outputs[i] = '*'
            else:
                outputs[i] = '+'
    print(outputs)


def presence_of_mind(guess, data_into_list):
    if(len(guess) != 5):
        print("Length of word should be exactly 5")
        return True
    if guess in data_into_list:
        return False  # Word Found and time to end the  loop
    print("Word not found in the list please try again")
    return True  # Here True means continuing the loop or the word is not present in the list

    # Reading file elements to the list
    # Please Change the path before running the program.
my_file = open(r"words.txt")
data = my_file.read()
data_into_list = data.split("\n")
my_file.close()
word = random.choice(data_into_list)

#Rules and Regulations
print("Welcome to wordle game")
print("1. '-' Sign means the word is not present in the list")
print("2. '+' Sign means word is present but incorrectly placed")
print("3. '*' Sign means word is present and correctly placed")
print("4. If word correctly guessed you will win the game")
print("5. You only have 6 guesses to win this game")

# For global declaration
guess = "temporarystring"
counting = 0
won = 0
for i in range(0, 6):
    guess = input()
    present = presence_of_mind(guess, data_into_list)
    while(present):
        guess = input()
        present = presence_of_mind(guess, data_into_list)
    counting = counting+1
    if(word == guess):
        print("Hurray, You won in ", counting, " tries")
        won = 1
        break
    else:
        games_func(word, guess)
if(won == 0):
    print("OOps You Lost Please try again") 
    print(word)
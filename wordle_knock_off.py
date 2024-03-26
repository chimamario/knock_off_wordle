# Recreating my version of wordle
# User will get the option of a 5 or 6 letter word
# user will have to input words to figure out which letter are in the word and what placement it will have
import random
import string
from word_data import five_dict, six_dict

# correct_letters = []
# incorrect_letters = [] 
# correct_position = []


def wordle():
    welcome()
    
#test

def string_to_list(word): #this makes a list of the word's letters
    list_of_letters = []
    # list_of_letters[:0] = word
    for letter in word:
        list_of_letters.append(letter)
    
    return list_of_letters

def no_duplicates(list): #this looks for duplicates within the 'string_to_list' list and removes them
    seen = []
    for letter in list:
        if letter in seen:
            continue
        else:
            seen.append(letter)
    return seen

def welcome(): #lets user pick how long they want the word
    print("\nWelcome to my knock-off version of wordle")
    print("____________________")
    correct_ans = False
    while correct_ans == False:
        five_or_six = int(input("\nPlease select a 5 or 6 lettered word: "))\

        if five_or_six == 5:
            correct_ans = True
            start_game(five_dict)
            
        elif five_or_six == 6:
            correct_ans = True 
            start_game(six_dict)      
            
        else:
            print("Invalid option, Please Try again")

def start_game(word_list): # This small method acknowledges the length of word selected and pick a random word
    print("____________________")
    print("\nYou have selected a {}-worded wordle round.".format(str(len(word_list[0]))))
    real_word = str(random.choice(word_list))
    # print(real_word)
    guessing_game(real_word, None, None, [], [], [], [], [])

def guessing_game(correct_word, guess, num_of_attempts_left, correct_letters, incorrect_letters, correct_position,correct_letter_wrong_position, guess_list = []):
   

    if num_of_attempts_left == 0: #when user runs out of attempts the game will show correct word and end the game
        print("____________________")
        for wrong_guess in guess_list:
            print(wrong_guess)
        print("\nRan out of attempts. The word was {}".format(correct_word))
        print("GAME OVER")
        exit()
    
    
    if guess != None: #works
        print("____________________")
        print("\nNumber of attempts left: {}".format(num_of_attempts_left))
        print("\nYou had guessed the word: {}".format(guess))
        print("____________________")
        print("\n")

        if guess != None: #letters in the correct position will be capitalized to show that the word is in the correct position
            for wrong_guess in guess_list:
                correct_position_index = len(correct_position) - 1
                while correct_position_index != -1:
                    letter_index = len(wrong_guess) - 1
                    while letter_index != -1:
                        if wrong_guess[letter_index] == correct_position[correct_position_index]:
                            wrong_guess = wrong_guess[:letter_index] + wrong_guess[letter_index].upper() + wrong_guess[letter_index + 1:]
                        letter_index -= 1
                    correct_position_index -= 1     
                print(wrong_guess)
        print("NOTE: if letter is in the correct position, letter will be CAPITALIZED")
        # print("\nCorrectly Positioned Letters: {}".format(correct_position))
        # print("Correct Letters in Guess (Might not be correct position): {}".format(correct_letters))
        print("Correct letters, Wrong Position: {}".format(correct_letter_wrong_position))
        print("Incorrect Letters in Guess: {}".format(incorrect_letters))

   
    correct_letters = [] #these list reset every attempt. 
    # incorrect_letters = [] 
    correct_position = []
    correct_letter_wrong_position = []

    if num_of_attempts_left == None: #works
        num_of_attempts_left = 6    

    proper_guess = False
    while proper_guess == False:
        print("____________________")
        print("\nInput should have no captial letters\nNOTE: letter can only be used once")
        guess = input("\nGuess a {}-lettered word\nInput: ".format(str(len(correct_word))))
        

        list = string_to_list(guess)
        list_of_letters = no_duplicates(list)
        correct__hidden = string_to_list(correct_word)
        correct_letters_hidden = no_duplicates(correct__hidden)

        # if len(guess) == len(correct_word): #we want to end loop after this guess #dont know if it works
        #     proper_guess = True 
        #     continue

        if len(guess) != len(correct_word): #WORKS
            print("____________________")
            print("\nInvalid guess. Please Try again")

            proper_guess = False
        
        elif guess == correct_word: #WORKS
            print("CONGRATULATIONS!! You have guessed the correct word: {}".format(correct_word))
            exit()
        
        elif guess in guess_list:
            print("____________________")
            print("\nGuess has already been attempted. Please Try again")
            proper_guess = False

        elif guess != correct_word:
            proper_guess = True
            guess_index = len(correct_word) - 1
            while guess_index != -1:
                word_index = len(correct_word) - 1
                while word_index != -1: #we need to for list of letter first and them make our lists

                    if guess[guess_index] == correct_word[word_index]: #guess_index is stagnant in this while loop. it will be seeing a lot of different 'word_index'
                        if guess_index == word_index: #this is to see if the matching letting have the same positioning
                            if guess[guess_index] not in correct_position: #removes potential duplicates
                                correct_position.append(guess[guess_index]) 
                            if guess[guess_index] not in correct_letters: #removes duplicates
                                correct_letters.append(guess[guess_index])
                        if guess_index != word_index: #the letter matches but isnt in the same position
                            if guess[guess_index] not in correct_letters:
                                correct_letters.append(guess[guess_index])
                
                    if guess[guess_index] != correct_word[word_index]: # at this point, the correct letters and correct positions lists have been filled.
                        if guess[guess_index] not in correct_letters_hidden:
                            if guess[guess_index] not in incorrect_letters:
                                incorrect_letters.append(guess[guess_index])
                        
                    word_index -= 1
                guess_index -= 1
            
    correct_letter_wrong_position = []
    for letter in correct_letters:
        if letter not in correct_position:
            correct_letter_wrong_position.append(letter)
    num_of_attempts_left -= 1
    guess_list.append(guess) 
    guessing_game(correct_word, guess, num_of_attempts_left, correct_letters, incorrect_letters, correct_position, correct_letter_wrong_position, guess_list,)
    

# make it possible to use letter mulitple times in guess
#correctly positioned letters in prior guesses should not also change into captial letter once letter is guess correctly in current guess
# make incorrect letter list in order


wordle()


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
#test 2

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

def duplicates(word): #creates dictionary with keys that are the words letters and the values are the indexs of the letter (helpful if the word has mulitiple occurances)
    position_of_letter = string_to_list(word)
    list_dict = {}

    list_dict = {letter: [] for letter in set(position_of_letter)}
    for index, letter in enumerate(position_of_letter):
        list_dict[letter].append(index)
    
    return list_dict



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
    guessing_game(real_word, None, None, [], [], {}, {}, {} ,[])

def guessing_game(correct_word, guess, num_of_attempts_left, correct_letters, incorrect_letters, correct_position_dict, incorrect_position_dict, incorrect_letter_dict,guess_list = []):
   

    if num_of_attempts_left == 0: #when user runs out of attempts the game will show correct word and end the game
        print("____________________")
        for wrong_guess in guess_list:
            print(wrong_guess)
        print("\nRan out of attempts. The word was {}".format(correct_word))
        print("GAME OVER")
        exit()
    
    
    if guess != None: #works
        # print("____________________")
        # print("\nNumber of attempts left: {}".format(num_of_attempts_left))
        # print("\nYou had guessed the word: {}".format(guess))
        # print("____________________")
        # print("\n")

        if guess != None: #letters in the correct position will be capitalized to show that the word is in the correct position
            merge_letter_dict = {letter: correct_position_dict.get(letter, []) 
                     + incorrect_position_dict.get(letter, []) + 
                     incorrect_letter_dict.get(letter, []) 
                     for letter in set(correct_position_dict) | set(incorrect_letter_dict) | set(incorrect_letter_dict) }

            max_index = len(guess)

            wrong_guess = [''] * (max_index + 1)

            for letter, list in merge_letter_dict.items():
                for index in list:
                    wrong_guess[index] = letter.upper() if letter in correct_position_dict and index in correct_position_dict[letter] else letter.lower()

            result = ''.join(wrong_guess)
        print('\n \n \n \n \n \n\n \n \n')
        print("____________________")
        print("\nNumber of attempts left: {}".format(num_of_attempts_left))
        print("NOTE: if letter is in the correct position, letter will be CAPITALIZED\n")
    
        incorrect_position_list = []
        for letter, list in incorrect_position_dict.items():
            if list == []:
                continue
            else:
                incorrect_position_list.append(letter)

        guess_list.append(result)
        for guess in guess_list:
            print(guess)
        print('\n')
        print("Correct letters, Wrong Position: {}".format(incorrect_position_list))
        print("Incorrect Letters in Guess: {}".format(incorrect_letters))

   
    correct_letters = [] #these list reset every attempt. 
    incorrect_letters = []
    correct_position_dict = {}
    incorrect_position_dict = {}
    incorrect_letter_dict = {}

    if num_of_attempts_left == None: #works
        num_of_attempts_left = 6    

    proper_guess = False
    while proper_guess == False:
        print("____________________")
        print("\nInput should have no captial letters")
        guess = input("\nGuess a {}-lettered word\nInput: ".format(str(len(correct_word))))
        

        guess_dict = duplicates(guess)
        correct_dict = duplicates(correct_word)

        # list = string_to_list(guess)
        # list_of_letters = no_duplicates(list)
        # correct__hidden = string_to_list(correct_word)
        # correct_letters_hidden = no_duplicates(correct__hidden)

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

            for letter, index_list in correct_dict.items():
                correct_position_dict[letter] = []

            for letter, index_list in guess_dict.items():
                incorrect_position_dict[letter] = []
                incorrect_letter_dict[letter] = []

            for letter, index_list in guess_dict.items():
                

                if letter not in correct_dict.keys():
                    incorrect_letters.append(letter)
                    for index in index_list:
                        incorrect_letter_dict[letter].append(index)
                

                if letter in correct_dict.keys():
                    correct_letters.append(letter)
                    for index in index_list:
                        if index in correct_dict[letter]:
                            correct_position_dict[letter].append(index)
                        if index not in correct_dict[letter]:
                            incorrect_position_dict[letter].append(index)

    num_of_attempts_left -= 1
    

    guessing_game(correct_word, guess, num_of_attempts_left, correct_letters, incorrect_letters, correct_position_dict, incorrect_position_dict,incorrect_letter_dict ,guess_list,)
    

# make it possible to use letter mulitple times in guess
#correctly positioned letters in prior guesses should not also change into captial letter once letter is guess correctly in current guess
# make incorrect letter list in order

#few ideas to improve code
#changing from a list that seperates works to a dictionary that has the keys as letters and the values should be a list that has the index of that letter (this is to make it possible for letters to be used multiple times)
#for the idea above - the dictorary only has to apply to the correct word (current list process can still be kept for the guessing word)   
#steps 
#

wordle()


# Recreating my version of wordle
# User will get the option of a 5 or 6 letter word
# user will have to input words to figure out which letter are in the word and what placement it will have
import random
import string
from word_data import five_dict, six_dict


def wordle():
    welcome()
    

def string_to_list(word): #this makes a list of the word's letters
    list_of_letters = []
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
            start_game(five_dict,five_or_six)
            
        elif five_or_six == 6:
            correct_ans = True 
            start_game(six_dict,five_or_six)      
            
        else:
            print("Invalid option, Please Try again")

def start_game(word_list, five_or_six): # This small method acknowledges the length of word selected and pick a random word
    print("____________________")
    print(f"\nYou have selected a {five_or_six}-worded wordle round.")
    real_word = str(random.choice(word_list))
    guessing_game(real_word, None, None, [], [], {}, {}, {} ,[])

def guessing_game(correct_word, guess, num_of_attempts_left, correct_letters, incorrect_letters, correct_position_dict, incorrect_position_dict, incorrect_letter_dict, correct_dict,guess_list = []):
   

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
            merge_letter_dict = {letter: correct_position_dict.get(letter, [])  #note that every all the index values should come from these dictionaries combined
                     + incorrect_position_dict.get(letter, []) + 
                     incorrect_letter_dict.get(letter, []) 
                     for letter in set(correct_position_dict) | set(incorrect_letter_dict) | set(incorrect_letter_dict) }

            max_index = len(guess)

            wrong_guess = [''] * (max_index + 1)

            for letter, list in merge_letter_dict.items(): #for loop that capitalizes the correct letters in the right position
                for index in list:
                    wrong_guess[index] = letter.upper() if letter in correct_position_dict and index in correct_position_dict[letter] else letter.lower()

            result = ''.join(wrong_guess)
        print('\n \n \n \n \n \n\n \n \n')
        print("____________________")
        print("\nNumber of attempts left: {}".format(num_of_attempts_left))
        print("NOTE: if letter is in the correct position, letter will be CAPITALIZED\n")
    
        incorrect_position_list = []
        for letter, list in incorrect_position_dict.items():
            if list == []: #this means the letter was either not in the guess or the letter is in the correct position
                continue
            else:
                incorrect_position_list.append(letter)
            
            if len(correct_position_dict[letter]) == len(correct_dict[letter]): #if there is an additional usage of letter in the guess, it may incorrectly add it to 'Correct letters, Wrong Position' 
                index = incorrect_position_list.index(letter)                   # which is incorrect so we must remove it
                incorrect_position_list.pop(index)                              # getting the index of misplaced letter to remove it from 'correct letter, wrong position list'
            

        guess_list.append(result) #printing all the guesses that the user has inputted
        for guess in guess_list:
            print(guess)
        print('\n')
        print("Correct letters, Wrong Position: {}".format(incorrect_position_list))
        print("Incorrect Letters in Guesses: {}".format(incorrect_letters))

   
    correct_letters = [] #these list reset every attempt. 
    # incorrect_letters = []
    correct_position_dict = {}
    incorrect_position_dict = {}
    incorrect_letter_dict = {}

    if num_of_attempts_left == None: #works
        num_of_attempts_left = 6    

    proper_guess = False
    while proper_guess == False:
        print("____________________")
        guess = input("\nGuess a {}-lettered word. (Note: Input should have no captial letters) \nInput: ".format(str(len(correct_word))))
        

        guess_dict = duplicates(guess) #these functions creates a dictionary where the letter of the word is the key and the index where the letter is placed is the values
        correct_dict = duplicates(correct_word)



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
        
        # 

        elif guess != correct_word:


            proper_guess = True

            for letter, index_list in correct_dict.items(): #setting up a dictionary (letter: ['index_1', 'index_2',....]). guesses with the correct index values will be added to its letters dict list
                correct_position_dict[letter] = []

            for letter, index_list in guess_dict.items(): #setting up a dictionary (letter: ['index_1', 'index_2',....]). If letter doesn't align with the same letters in the correct dictionary, it goes into this dictionary 
                incorrect_position_dict[letter] = [] #for correct letters but they are in the wrong position
                incorrect_letter_dict[letter] = [] #for incorrect letters (they do not show up in the guess)

            for letter, index_list in guess_dict.items():
                
                if letter not in correct_dict.keys():
                    incorrect_letters.append(letter) #adding incorrect letter to list
                    for index in index_list:
                        incorrect_letter_dict[letter].append(index) #adding incorrect letter and it's index value to dictionary 
                

                if letter in correct_dict.keys(): #confirms that letter in guess is also in correct word
                    correct_letters.append(letter) #add letter to list
                    for index in index_list: #iterating through all index values connected to a specific letter
                        if index in correct_dict[letter]: #checking if the guess' index value is also in the correct word index value list
                            correct_position_dict[letter].append(index)
                        if index not in correct_dict[letter]:
                            incorrect_position_dict[letter].append(index)

    num_of_attempts_left -= 1
    

    guessing_game(correct_word, guess, num_of_attempts_left, correct_letters, incorrect_letters, correct_position_dict, incorrect_position_dict,incorrect_letter_dict, correct_dict,guess_list,)
    


wordle()

#new ideas
#notice that if a letter is in the correct position but is also used again in the wrong posistion, then the second attempt of letter should be added to the incorrect letter (IF THERE IS NO MORE POSITIONS WHERE IT WOULD BE CORRECT)
#
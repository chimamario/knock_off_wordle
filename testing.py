
word = 'pooping'

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

def duplicates(word):
    position_of_letter = string_to_list(word)
    seen = no_duplicates(position_of_letter)
    list_dict = {}

    list_dict = {letter: [] for letter in set(position_of_letter)}
    for index, letter in enumerate(position_of_letter):
        list_dict[letter].append(index)



    # for letter in seen:
    #     list_dict[letter] = []
    
    # for letter in word:
    #     index = position_of_letter.index(letter)
    #     print(index)
    #     if letter in list_dict.keys():
    #         list_dict[letter].append(index)
    
    # print(position_of_letter)

    return list_dict

correct_letters = [] #these list reset every attempt.    
incorrect_letters = []
correct_position_dict = {} #use
incorrect_position_dict = {} #use 
incorrect_letter_dict = {}

correct_word = 'pooping'
guess = 'tropign'
proper_guess = False

guess_dict = duplicates(guess)
correct_dict = duplicates(correct_word)

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
        

#note that correct_position_dict, incorrect_position_dict, and incorrect_letter_dict should all have all the index values to create the guess again   
        

print(correct_letters) 
print(incorrect_letters)  
print(correct_position_dict)
print(incorrect_position_dict)
print(incorrect_letter_dict)



#after going through function the first time

merge_letter_dict = {letter: correct_position_dict.get(letter, []) 
                     + incorrect_position_dict.get(letter, []) + 
                     incorrect_letter_dict.get(letter, []) 
                     for letter in set(correct_position_dict) | set(incorrect_letter_dict) | set(incorrect_letter_dict) }

max_index = len(guess)

wrong_guess = [''] * (max_index + 1)

for letter, list in merge_letter_dict.items():
    for index in list:
        wrong_guess[index] = letter.upper() if letter in correct_position_dict and index in correct_position_dict[letter] else letter

result = ''.join(wrong_guess)





incorrect_position_list = []
for letter, list in incorrect_position_dict.items():
    if list == []:
        continue
    else:
        incorrect_position_list.append(letter)

print(f"Correct letters, Wrong Position: {incorrect_position_list}")
print(f"Incorrect Letters in Guess: {incorrect_letters}")
print(result)








# while proper_guess == False:
#     print("____________________")
    
    

    













#     if guess != correct_word:
#         proper_guess = True
#         guess_index = len(correct_word) - 1
#         while guess_index != -1:
#             word_index = len(correct_word) - 1
#             while word_index != -1: #we need to for list of letter first and them make our lists

#                 if guess[guess_index] == correct_word[word_index]: #guess_index is stagnant in this while loop. it will be seeing a lot of different 'word_index'
#                     if guess_index == word_index: #this is to see if the matching letting have the same positioning
#                         if guess[guess_index] not in correct_position: #removes potential duplicates
#                             correct_position.append(guess[guess_index]) 
#                         if guess[guess_index] not in correct_letters: #removes duplicates
#                             correct_letters.append(guess[guess_index])
#                     if guess_index != word_index: #the letter matches but isnt in the same position
#                         if guess[guess_index] not in correct_letters:
#                             correct_letters.append(guess[guess_index])
            
#                 if guess[guess_index] != correct_word[word_index]: # at this point, the correct letters and correct positions lists have been filled.
#                     if guess[guess_index] not in correct_letters_hidden:
#                         if guess[guess_index] not in incorrect_letters:
#                             incorrect_letters.append(guess[guess_index])
                    
#                 word_index -= 1
#             guess_index -= 1



# print(duplicates(word))
#results {'i': [4], 'g': [6], 'p': [0, 3], 'n': [5], 'o': [1, 2]}

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

print(duplicates(word))
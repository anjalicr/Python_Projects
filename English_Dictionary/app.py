import json
import difflib
from difflib import get_close_matches

# Loading json file in python object
data = json.load(open("data.json"))

def word_mean(word):

    small_case_keyword = word.lower() # converting case of input word from user to small case
    # creating list of words that match with the input word from data (here we aare taking only 3 words from data object i.e., default value in get_close_matches)
    matching_wordlist = get_close_matches(small_case_keyword , data.keys())

    if small_case_keyword in data.keys():
        return data[small_case_keyword]

    elif word.title() in data.keys():
        return data[word.title()]

    elif word.upper() in data.keys():
        return data[word.upper()]

    elif len(matching_wordlist) > 0:
        yn = input("Do you mean {} ? If Yes, enter y and if No , enter n: ".format(matching_wordlist[0]))

        if yn == 'y':
            return data[matching_wordlist[0]]
        elif yn == 'n':
            return "The word is not in dictionary, please try with correct word."
        else:
            return "We don't understand your query."

    else:
        return "The word is not in dictionary, please try with correct word."

word = input("Enter a word: ")

output = word_mean(word)

#checking if the output for user input word is a list and then interating to print every meaning on new line.
if type(output) == list:
    for item in output:
        print (item)
else:
    print (output)

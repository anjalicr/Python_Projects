import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))


def word_mean(word):

    small_case_keyword = word.lower()
    matching_wordlist = get_close_matches(small_case_keyword , data.keys())

    if small_case_keyword in data.keys():
        return data[small_case_keyword]
    elif len(matching_wordlist) > 0:
        yn = input("Do you mean {} ? If Yes, enter y and if No , enter n: ".format(matching_wordlist[0]))
        if yn == 'y':
            return data[matching_wordlist[0]]
        elif yn == 'n':
            return "The word is not in dictionary, please try with correct word."
        else:
            return "We don't understnad your query."
    else:
        return "The word is not in dictionary, please try with correct word."

word = input("Enter a word: ")

output = word_mean(word)

if type(output) == list:
    for item in output:
        print (item)
else:
    print (output)

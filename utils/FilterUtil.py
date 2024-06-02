import re

# Initializes the ignore list with hardcoded words
# Input: None
# Output: ignoreList, the list of ignored words
# TODO: Create UI to allow entry of ignored words in the terminal
# TODO: Store ignored words in a txt file
def initializeIgnoreList():
    ignoreList = []
    ignoreList.append("") # Regex for hello, hi, morning, night, bye, thanks, goodbye, !, ?, ., ,, :, ;, 

    return ignoreList

# Filter function to remove ignored words in description
# Input: ignoreList, a list of ignored words, input, the description in the json
# Output: description in the json removing ignored words
# TODO: Upgrade into the Rabin-Karp algorithm for faster processing
# TODO: Discuss how to implement phrases
# TODO: Discuss how to sort phrases by importance
def filterIgnoreList(ignoreList: list, input: list):
    for ignore in ignoreList:

        # change this to assume that ignore is a regex
        if ignore in input:
            list.remove(ignore)
    return input

# Filter function that removes words in order of ignored words, then greetings/farewells
# Input: ignoreList, a list of ignored words, input, the description in the json
# Output: description in the json removing ignored words and greetings/farewells
def filterDescription(input: str):
    splitString = str.split()
    filterIgnoreList(initializeIgnoreList(), splitString)
    return input
    
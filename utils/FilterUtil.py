import string

class FilterUtil():
    # Initializes the ignore list with hardcoded words
    # Input: None
    # Output: ignoreList, the list of ignored words
    # TODO: Create UI to allow entry of ignored words in the terminal
    # TODO: Store ignored words in a txt file
    def initializeIgnoreList(self) -> list:
        ignoreList = ["hello", "hi", "morning", "night", "bye", "thanks", "goodbye", "please"]
        return ignoreList


    # Cleans the ticket by changing the words to lower case, and splitting the words into a list, and removing punctuation
    # Input: input, the description to clean
    # Output: the cleaned description, which is a list of strings
    def cleanDescription(self, input: str) -> list:
        output = input.lower().translate(str.maketrans('', '', string.punctuation)).split()
        return output


    # Filter function to remove ignored words in description
    # Input: ignoreList, a list of ignored words, input, the description in the json
    # Output: description in the json removing ignored words
    # TODO: Upgrade into the Rabin-Karp algorithm for faster processing
    # TODO: Discuss how to implement phrases
    # TODO: Discuss how to sort phrases by importance (Pagerank?)
    def filterIgnoreList(self, ignoreList: list, input: list) -> list:
        if len(ignoreList) == 0:
            return input
        
        if len(input) == 0:
            return input

        for string in input[:]:
            if string in ignoreList:
                input.remove(string)

        return input

    # Filter function that removes words in order of ignored words, then greetings/farewells
    # Input: ignoreList, a list of ignored words, input, the description in the json
    # Output: description in the json removing ignored words and greetings/farewells
    def filterDescription(self, input: str) -> str:
        if len(input) == 0:
            return ""

        cleanedDescription = FilterUtil.cleanDescription(self, input)
        cleanedDescription = FilterUtil.filterIgnoreList(self, FilterUtil.initializeIgnoreList(self), cleanedDescription)
        output = " "
        return output.join(cleanedDescription)
        
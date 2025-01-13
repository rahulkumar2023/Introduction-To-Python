from functions3 import *

def main():

    word1 = ""
    word2 = ""
    correct = False

    # This while loop ensures that the user ends up entering an upper-case word for word 1.
    while not correct:
       correct = True
       word1 = input("Please enter an upper-case word: ")
       word1 = word1.strip(' ')

       if len(word1) == 0 or word1 != word1.upper() or not word1.isalpha():
            print("Invalid input.")
            correct = False

    correct = False

    # This while loop ensures that the user ends up entering an upper-case word for word 2.
    while not correct:
        correct = True
        word2 = input("Please enter another upper-case word: ")
        word2 = word2.strip(' ')

        if len(word2) == 0 or word2 != word2.upper() or not word2.isalpha():
            print("Invalid input.")
            correct = False

    # The below code calls the function is_anagram, to check whether the two strings are anagrams or not.
    anagram_or_not = is_anagram(word1, word2)

    if anagram_or_not == True:
        print("The two words that have been entered are anagrams of each other.")

    else:
        print("The two words that have been entered are not anagrams of each other.")
        
main()


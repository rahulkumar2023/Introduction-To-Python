from functions3 import *

def main():
    word1 = ""
    word2 = ""
    prime_list1 = []
    prime_list2 = []
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

    # This function applies the radix sort on the list of primes that was created from the user input of the first word.
    for i in range(len(word1)):
        prime_list1.append(char_prime(word1[i]))

    max_digits = len(str(max(prime_list1)))
    sorted_prime_list1 = radix_sort_recursive(prime_list1, max_digits)
    print("The unsorted list of primes for the first word is: " + str(prime_list1) + ".")
    print("The sorted list of primes for the first word, in ascending order, is: " + str(sorted_prime_list1) + ".")

    # This function applies the radix sort on the list of primes that was created from the user input of the second word.
    for i in range(len(word2)):
        prime_list2.append(char_prime(word2[i]))

    max_digits = len(str(max(prime_list2)))

    sorted_prime_list2 = radix_sort_recursive(prime_list2, max_digits)

    print("The unsorted list of primes for the second word is: " + str(prime_list2) + ".")
    print("The sorted list of primes for the second word, in ascending order, is: " + str(sorted_prime_list2) + ".")

main()

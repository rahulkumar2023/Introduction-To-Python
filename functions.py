"""
   CISC-121 2023F

   Name:   Rahul Kumar
   Student Number: 20349877
   Email:  21rk74@queensu.ca
   Date: 2023-08-03

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""

def char_prime(my_char):
    """
    -------------------------------------------------------
    Converts an uppercase letter to a unique prime number
    Based on the conversion given in the footnote
    -------------------------------------------------------
    Parameters:
    my_char - a char in ABCDEFGHIJKLMNOPQRSTUVWXYZ (char)
    Returns:
    prime_int = a prime number unique to the letter
    -------------------------------------------------------
    """

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    p_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

    # This function creates a dictionary and zips the letters and prime numbers together.
    dictionary = dict(zip(letters, p_numbers))

    prime_int = dictionary.get(my_char)
    return (prime_int)

def Primeify(my_string):
    """
    -------------------------------------------------------
    RECURSIVELY gives the product of primes corresponding to the letters
    in the string
    -------------------------------------------------------
    Parameters:
    my_string - any string (str)
    Returns:
    prime_product = the product of all primes for each letter
    -------------------------------------------------------
    """

    n = len(my_string)
    prime_product = 1

    # If the length of the string is 1, the prime number associated with the letter within the word must be used.
    if n == 1:
        prime_product = char_prime(my_string)

    # If the length of the string is greater than 1, the function is recursively called so as to continue to multiply all of the prime numbers within the characters of the string.
    else:
        prime_product = prime_product * Primeify(my_string[0]) * Primeify(my_string[1: n + 1])

    return prime_product

def is_anagram(string1, string2):
    """
    -------------------------------------------------------
    Determines if two strings are anagrams of each other
    -------------------------------------------------------
    Parameters:
    string1, string2 - any two strings (str)
    Returns:
    is_anagram = whether or not they are anagrams (Boolean)
    ------------------------------------------------------
    """

    is_anagram = False

    # If the product of primes is equal for both strings, then, they are both anagrams.
    if Primeify(string1) == Primeify(string2):
        is_anagram = True

    return is_anagram

def radix_sort_recursive(arr, max_digits):

    """
    -------------------------------------------------------
    Creates a radix sort for the product of primes that have been created from the inputs of the words entered by the user.
    -------------------------------------------------------
    Parameters:
    arr - list of unsorted prime numbers
    max_digits - number of digits within the list
    Returns:
    sorted_arr = sorted list of prime numbers
    ------------------------------------------------------
    """

    # Determine the maximum number of digits in the array
    if (len(arr) == 0 or max_digits <= 0):
        return arr

    buckets = [[] for _ in range(10)]

    # Distribute the elements of the array into the buckets based on the current digit value
    for num in arr:
        digit = (num // 10 ** (max_digits - 1)) % 10
        buckets[digit].append(num)

    # Recursively sort the elements in each bucket
    sorted_buckets = [radix_sort_recursive(bucket, max_digits - 1) for bucket in buckets]

    # Concatenate the sorted buckets back into a single array
    sorted_arr = []

    for bucket in sorted_buckets:
        sorted_arr += bucket

    return sorted_arr
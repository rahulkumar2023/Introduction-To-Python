"""
   CISC-121 2022F

   Name:   Rahul Kumar
   Student Number: 20349877
   Email:  21rk74@queensu.ca
   Date: 2023-17-01

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""
import random
import math


def valid_or_invalid_numbers(num1, num2):
    """
    -------------------------------------------------------
    This function checks if the two random integers outputted are valid or not, based upon the difference of the two numbers.
    Use: valid_or_invalid_numbers(num1, num2)
    -------------------------------------------------------
    Parameters:
        num1 - represents the first random integer that has been outputted.
        num2 - represents the second random integer that has been outputted.
    Returns:
        None
    -------------------------------------------------------
    """

    # Check if numbers are already valid
    diff = max(num1, num2) - min(num1, num2)

    #  Double the larger integer if diff is less than 10 or take one third of the larger number is diff is greater than 50
    if diff < 10 or diff > 50:

        while (diff < 10 or diff > 50):
            print("This pair of integers is invalid.")

            if diff < 10:
                print("Since the difference of the two numbers is less than 10, the larger integer has been multiplied by 2.")

                if num1 > num2:
                    num1 = 2 * num1

                else:
                    num2 = 2 * num2

            else:
                print("Since the difference of the two numbers is greater than 50, the larger integer has been multiplied by 1/3.")

                if num1 > num2:
                    num1 = math.ceil(1 / 3 * num1)

                else:
                    num2 = math.ceil(1 / 3 * num2)

            diff = max(num1, num2) - min(num1, num2)

            print("Two randomly generated integer numbers are", num1, "and", num2)

    print("This pair of integers is valid")

    # Once the numbers are valid call the function to apply fruit or object(s) based on conditions
    fruit_or_object(num1, num2)

def fruit_or_object(num1, num2):
    """
    -------------------------------------------------------
    This function prints out all of the numbers between the first number and the second number, and prints out object(s) or a number depending upon a couple of conditions.
    Use: fruit_or_number(num1, num2)
    -------------------------------------------------------
    Parameters:
        num1 - represents the smallest valid number between the two randomly generated numbers
        num2 - represents the largest valid number between the two randomly generated numbers
    Returns:
        min_num - the lower number between num1 and num2
    -------------------------------------------------------
    """
    print("Output of the valid numbers ", min(num1, num2), ",", max(num1, num2), ":", sep="")

    min_num = min(num1, num2)
    max_num = max(num1, num2)

    # Run the loop from min to max
    while min_num <= max_num:

        # If a number is a factor of 5 or 7 or contains 3, then print an object(s)
        if (min_num % 5 == 0) or (min_num % 7 == 0) or (min_num // 10 == 3) or (min_num % 10 == 3):

            if (min_num % 5 == 0):
                print("apple", end=" ")

            if (min_num % 7 == 0):
                print("pen", end=" ")

            if min_num // 10 == 3 or min_num % 10 == 3:
                print("pineapple", end="")

            print("")

        # Else, print a number
        else:
            print(min_num)

        min_num = min_num + 1


def main():

    # Generates 2 random numbers
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print("Two randomly generated integer numbers are", num1, "and", num2)

    # Calls the function
    valid_or_invalid_numbers(num1, num2)

main()
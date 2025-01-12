from functions import all_odd_or_even

"""
-------------------------------------------------------
This function takes any number of integers and returns whether the integers are either all even, all odd, or neither all even nor all odd.
Use: all_odd_or_even(*integers)
-------------------------------------------------------
Parameters:
    *integers - represents any number of arguments that can be entered by the user, so long as they are all integers
Returns:
    returnvalue - boolean value that if true, represents that all integers are either all odd oe all even, but if false, represents that all integers are neither all even nor all odd
-------------------------------------------------------
"""

def main():

    choice = "Yes"
    integers = []
    flag = True

    print("This program will allow you to check whether the integers you've entered are either all even or all odd.")

    choice = input("Would you like to participate in this activity? Please enter Yes or yes to continue: ")

    # if the user wants to play, then, allow them to enter integers
    if (choice == "Yes" or choice == "yes"):

        while (choice == "Yes" or choice == "yes"):

            try:
                number = int(input("Please enter an integer: "))
                number = integers.append(number)

            except:
                # if an integer is not entered, exit the program
                flag = False
                print("An integer was not entered.")
                print("Exiting....")
                break

            choice = input("Would you like to add another integer? Please enter Yes or yes to continue: ")

        # check whether the integers provided are all odd or all even

        if all_odd_or_even(integers):
            print("All of the numbers that have been entered are either all odd or all even.")

        else:
            print("All of the numbers that have been entered are neither all odd nor all even.")

    # if the user doesn't want to participate in the activity, exit the program
    else:
        print("Exiting...")

main()



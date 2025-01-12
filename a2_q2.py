"""
   CISC-121 2022F

   Name:   Rahul Kumar
   Student Number: 20349877
   Email:  21rk74@queensu.ca
   Date: 2023-31-01

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""

from functions import friends_to_dictionary
from functions import friendship_degree
from functions import all_my_friends

"""
-------------------------------------------------------
This function converts the file friendship.txt into a dictionary, and returns said dictionary.
Use: friends_to_dictionary()
-------------------------------------------------------
Parameters:
    None
Returns:
    friendshipdict - converts the file friendship.txt into a dictionary
-------------------------------------------------------
"""

"""
-------------------------------------------------------
This function takes a person from the list and returns all the people who are friends with the given name.
Use: all_my_friends(friendshipdict, friend)
-------------------------------------------------------
Parameters:
    friendshipdict - Dictionary that stores the information about a person and their friends
    friend - An individual friend of a particular person
Returns:
    friendlist - Represents all of the friends of an individual person in a list
-------------------------------------------------------
"""

"""
-------------------------------------------------------
This function prints out the friends of each person in the dictionary.
Use: friendship_degree(dictionary)
-------------------------------------------------------
Parameters:
    dictionary - Represents the dictionary that has the information of a person and that person's friends
Returns:
    None
-------------------------------------------------------
"""

def main():

    # call function to read the friendship file and return the dictionary
    fdict = friends_to_dictionary()

    # call the function to print the friendship list for a person inputted by the user
    name = input('What is the name of the person whose friends you would like to know?: ')

    flist = all_my_friends(fdict, name)

    print(name + " has the following friends: " +str(flist))

    friendship_degree(fdict)

main()




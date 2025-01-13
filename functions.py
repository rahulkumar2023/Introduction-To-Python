def all_odd_or_even(*integers):

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

    returnvalue = False

    # checks if a list is sent, and if so, then retrieves the list
    if type(*integers) == list:
        integerslist = integers[0]

    if len(integerslist) > 0:
        odd_integers = []
        even_integers = []

        for number in integerslist:

            if (number % 2 == 0):
                even_integers.append(number)

            else:
                odd_integers.append(number)

        if len(integerslist) == len(even_integers) or len(integerslist) == len(odd_integers):
            returnvalue = True

    return returnvalue

def friends_to_dictionary():

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

    friendshipdict = {}

    # reads the file
    filename = 'friendship.txt'

    with open(filename, 'r') as datafile:

        for line in datafile:

            if (line.strip() != ""):
                record = line.split()
                key = record[0]

                # if the person doesn't exist in the dictionary create a value list
                if key not in friendshipdict.keys():
                    friendshipdict[key] = []

                # add friend to the list
                friendshipdict[key].append(record[1])

    datafile.close()

    return friendshipdict

def all_my_friends(friendshipdict, friend):

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

    friendlist = friendshipdict[friend]

    # find all people who are friends with this person
    for key in friendshipdict.keys():

        # if the person is in the other list and not already added to this list, then, add the other person to this list
        if ((friend in friendshipdict[key]) and (key not in friendlist)):
            friendlist.append(key)

    return friendlist

def friendship_degree(dictionary):

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

    for key in dictionary.keys():
        # this will call all of the friends for each individual person
        flist = all_my_friends(dictionary, key)

        print(key + " has " + str(len(flist)) + " friends: (%s)" % str(flist).strip('[]'))

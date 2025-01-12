import random

def writeTofile(name, age, color):
    """
    -------------------------------------------------------
    This function appends my name, my age, and my favourite colour to a separate file named myspace_profiles.txt.
    Use: writeTofileForme(name, age, color)
    -------------------------------------------------------
    Parameters:
        name - my name
        age - my age
        color - my favourite colour
    Returns:
        f - the file that has been appended with all of this function's information, whose name is myspace_profiles.txt.
    -------------------------------------------------------
    """
    #  Opens file in append mode
    f = open ("myspace_profiles.txt", "a")

    # Add name, age, color on separate line. Add '-' as record seperator
    f.write(name + "\n")
    f.write(str (age) + "\n")
    f.write(color + "\n")
    f.write("-" + "\n")

def main():

    # Creates a record for myself
    name = "Rahul Kumar"
    age = 18
    color = "blue"

    #Writes to file
    writeTofile(name,age,color)

    #Creates a record by asking user
    name = input("What is your name? ")

    age = random.randint(18,22)

    colors = ["green", "red", "yellow", "pink", "blue", "orange"]
    # Generates random number to get random color
    wordPosition = random.randint(0, len(colors) - 1)
    color = colors[wordPosition]

    writeTofile(name,age,color)

main()

# Import all functions from functions2 file.
from functions2 import *

# Create a list of dictionaries by reading electionData from file and provide a menu to the user for different reports.
def main():
    listdistricts = []
    stop = False

    # Create a list of dictionaries from the file.
    with open('electionsData.txt') as reader:
        lines = reader.readlines()
        reader.close()

    keys = lines[0].strip().split('\t')

    for i in range(1, len(lines)):
        lineparts = lines[i].strip().split('\t')
        d = dict(zip(keys, lineparts))
        listdistricts.append(d)

    # Create a menu and provide the user with options to access different functionalities. Stop flag will help the user to exit from the menu.
    while (stop == False):

        print("++++++++++++++Main Menu++++++++++++")
        print("1. Display information for an electoral district")
        print("2. Show unique districts by the given province")
        print("3. Find the district with the maximum value for any of the column headers")
        print("4. Find the district with the maximum value for any of the column headers")
        print("5. Find the total number of votes in each province")
        print("6. Sort the list based on any column header")
        print("7. Find the percentage of voter turnout for a district based on the electoral district number")
        print("8. Exit")

        option = int(input('Enter your choice: '))

        # Option 1 will display information about an electoral district.
        if (option == 1):

                distname = input("Enter an electoral district number: ")
                displayInfo(distname, listdistricts)

        # Option 2 will display all electoral districts within a province.
        elif (option == 2):
            province = input('Enter the name of a province: ')
            uniqueDistricts(province, listdistricts)

        # Option 3 will display the maximum value for a user supplied column.
        elif (option == 3):
            colname = ""

            # Check if valid column is provided
            while (colname != 'Electors' and colname != 'Population' and colname != 'Polling Stations' and colname != 'Valid Ballots' and colname != 'Rejected Ballots' and colname != 'Total Ballots'):
                colname = input('Enter the name of a column header: ')
            findMax(colname, listdistricts)

        # Option 4 will display the minimum value for a user supplied column
        elif (option == 4):
            colname = ""

            # Check if valid column is provided
            while (colname != 'Electors' and colname != 'Population' and colname != 'Polling Stations' and colname != 'Valid Ballots' and colname != 'Rejected Ballots' and colname != 'Total Ballots'):
                colname = input('Enter the name of a column header: ')

            findMin(colname, listdistricts)

        # Option 5 will display the total number of votes per province.
        elif (option == 5):
            totalVotes(listdistricts)

        # Option 6 will sort the list based on a user provided column.
        elif (option == 6):
            colname = ""

            # Checks if the provided Column is a valid column.
            while (colname not in keys):
                colname = input('Enter the name of the column by which you would like to sort the list: ')
            listdistricts = selectionSort(listdistricts, colname)
            print("Sorted by '" + colname + "'")

        # Option 7 gives the % of voters that turned up for a given electoral district.
        elif (option == 7):
            distno = int(input('Enter a district number: '))
            binarySearch(distno, listdistricts)

        # Option 8 allows the user to exit from the menu.
        elif (option == 8):
            print("Exiting.....")
            stop = True

        # Any other input given by the user will result in an invalid input.
        else:
            print("Invalid input.")

main()

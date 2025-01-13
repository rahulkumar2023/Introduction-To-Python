def displayInfo(districtname, listdistricts):

    """
    -------------------------------------------------------
    This function displays the information of a particular electoral district.
    Use: displayInfo(districtname, listdistricts)
    -------------------------------------------------------
    Parameters:
        districtname - represents the name of an electoral district
        listdistricts - represents the list of dictionaries created with all of the column headers and their values.
    Returns:
        None
    -------------------------------------------------------
    """

    #  Iterates through the list to display the information for a given district.
    for dictd in listdistricts:

        if (dictd['Electoral District Number'] == districtname):

            print('Polling Stations: {0}, Valid Ballots: {1}, Total Ballots Cast: {2}, Voter Turnout: {3}%'.format(dictd['Polling Stations'], dictd['Valid Ballots'], dictd['Total Ballots Cast'],dictd['Percentage of Voter Turnout']))

def uniqueDistricts(provincename, listdistricts):

    """
    -------------------------------------------------------
    This function displays all of the electoral districts for a partciular province.
    Use: uniqueDistricts(provincename, listdistricts)
    -------------------------------------------------------
    Parameters:
        provincename - represents the name of a province
        listdistricts - represents the list of dictionaries created with all of the column headers and their values.
    Returns:
        None
    -------------------------------------------------------
    """

    districts = []

    #  Iterates through the list to display information and appends the district to a list.
    for dictd in listdistricts:

        if (provincename == (dictd['Province'].split('/'))[0]):
            districts.append(dictd['Electoral District Name'])

    if (len(districts) == 0):
        print("No Data Found")

    else:
        print(districts)

def findMax(keyvalue, listdistricts):

    """
    -------------------------------------------------------
        This function displays the maximum value for a particular header column.
        Use: findMax(keyvalue, listdistricts)
    -------------------------------------------------------
    Parameters:
        keyvalue - represents a column header
        listdistricts - represents the list of dictionaries created with all of the column headers and their values.
    Returns:
        None
    -------------------------------------------------------
    """

    # Set max to a negative number originally.
    max = -999
    # Iterate through list and if the current number is greater than max, then, update max.
    for key in listdistricts:

        if int(key[keyvalue]) > max:
            max = int(key[keyvalue])
            districtname = key['Electoral District Name']

    print('Max {0}: {1} {2}'.format(keyvalue, districtname, max))

def findMin(keyvalue, listdistricts):

    """
    -------------------------------------------------------
    This function displays the minimum value for a particular header column.
    Use: findMin(keyvalue, listdistricts)
    -------------------------------------------------------
    Parameters:
        keyvalue - represents a column header
        listdistricts - represents the list of dictionaries created with all of the column headers and their values.
    Returns:
        None
    -------------------------------------------------------
    """

    # Set min to a very high number
    min = 10000000000

    # Iterate through list and if current number is smaller than min, then, update min.
    for key in listdistricts:

        if int(key[keyvalue]) < min:
            min = int(key[keyvalue])
            districtname = key['Electoral District Name']

    print('Min {0}: {1} {2}'.format(keyvalue, districtname, min))

def totalVotes(listdist):

    """
    -------------------------------------------------------
    This function displays the total number of votes in all provinces.
    Use: totalVotes(listdist)
    -------------------------------------------------------
    Parameters:
        listdist - represents a list of all electoral districts
    Returns:
        None
    -------------------------------------------------------
    """

    resultlist = []
    result = {}

    # Iterate through list and check if the 'Provice' already exists. If so, then, add total Ballots Cast to the total number of ballots within the province.
    for d in listdist:

        if d['Province'] not in (totalv['Province'] for totalv in resultlist):
            result = {'Province': d['Province'], 'Total Ballots Cast': int(d['Total Ballots Cast'])}
            resultlist.append(result)

        else:

            for i in range(0, len(resultlist) - 1):

                if (resultlist[i]['Province'] in d['Province']):
                    resultlist[i]['Total Ballots Cast'] += d['Total Ballots Cast']

    # Sort the list albhabetically based on the province column.
    resultlist = selectionSort(resultlist, 'Province')

    # Remove the French name from the provinces.
    print("Total Votes:")

    for keys in resultlist:
        print('{0}: {1}'.format((keys['Province'].split('/'))[0], keys['Total Ballots Cast']))

def selectionSort(listdistricts, keyvalue):

    """
    -------------------------------------------------------
    This function sorts any particular user inputted column header.
    Use: selectionSort(listdistricts, keyvalue)
    -------------------------------------------------------
    Parameters:
        listdistricts - represents the list of dictionaries created with all of the column headers and their values.
        keyvalue - represents a particular column header
    Returns:
        listdisricts - the sorted list of dictionaries for a particular column header
    -------------------------------------------------------
    """

    # Sort the list based on a column provided. Start with the 2nd element as the 1st element is already sorted.
    for i in range(1, len(listdistricts)):
        key_item = listdistricts[i]
        j = i - 1

        # Keep swapping the elements until the beginning or until the right place has been found for the element.
        while j >= 0 and listdistricts[j][keyvalue] > key_item[keyvalue]:
            listdistricts[j + 1] = listdistricts[j]
            j -= 1

        # Copy the data to the correct location.
        listdistricts[j + 1] = key_item

    return listdistricts

    for key in listdistricts:
        print(key['Electoral District Name'] + ":" +key[keyvalue])

def binarySearch(districtnumber, listdistricts):
    """
    -------------------------------------------------------
    This function does a binary search based on the sorted electoral district number and gives out the percentage of people that voted for a particular electoral number.
    Use: binarySearch(districtnumber, listdistricts)
    -------------------------------------------------------
    Parameters:
        districtnumber - represents a particular electoral number
        listdistricts - represents the list of dictionaries created with all of the column headers and their values.
    Returns:
        None
        -------------------------------------------------------
        """

    # To run a binary search, the list need to be sorted. Sort the list based on the disctrict number.
    listdistricts = selectionSort(listdistricts, 'Electoral District Number')

    # Start the search from the full list
    low = 0
    high = len(listdistricts) - 1
    mid = 0
    found = False

    # Keep on searching until found is true or low become higher than high.
    while ((low <= high) and (found == False)):

        # Divide the list in half and based on the search value, decide which half will have the element within itself.
        mid = (high + low) // 2

        if int(listdistricts[mid]['Electoral District Number']) < districtnumber:
            low = mid + 1

        elif int(listdistricts[mid]['Electoral District Number']) > districtnumber:
            high = mid - 1

        else:
            found = True

    if found == True:
        print('Found: {0}'.format(listdistricts[mid]['Percentage of Voter Turnout'] + "%"))

    else:
        print('Item Was Not Found')

     

                        
                

from hotel_classes import *

# Create hotel rooms
suites =[Suite(i, date.today()) for i in range(1, 20)]

standard_rooms =[StandardRoom(i, date.today()) for i in range(20, 109)]
taylor_suites =[TaylorSuite(i, date.today()) for i in range(109, 123)]

# Create a guest and check them in
guestname = str(input('Enter the name of the guest: '))

nodays = int(input("Enter the number of days that the guest will stay for: "))

guest = Guest(guestname, date.today() + timedelta(days=nodays))
invalid = False
found = False

while not invalid and not found:
    print("+++++++++++++++++++++++++++++++")

    # Select Room Type
    print("---Room Type Menu---")
    print("1. Suite")
    print("2. Standard Room")
    print("3. Taylor Suite")

    typeroom = int(input('Enter your room type: '))

    if (typeroom == 1):
        i = 1

        while (i < 20 and not found):

            if (suites[i].available):
                suites[i].guest_check_in(guest)
                found = True
            i = i + 1

    elif (typeroom == 2):
        i = 1

        while (i < 90 and not found):

            if (standard_rooms[i].available):
                standard_rooms[i].guest_check_in(guest)
                found = True
        i = i + 1

    elif (typeroom == 3):
        i = 1

        while (i < 14 and not found):

            if (taylor_suites[i].available):
                taylor_suites[i].guest_check_in(guest)
                found = True
        i = i + 1

    else:
        print('Invalid room type.')

if (found == False):
    print("No room is available for the type of room that's been inputted.")
    exit

invalid = False

while not invalid:
    # Select service type
    print("++++++++++++++++++++++++++++++")
    print("---Service Type---")
    print("1. Room Service")
    print("2. Movie Rental")
    print("3. Both")
    services = int(input('Enter the service type you would like: '))

    if (services == 1):
        guest.add_service('Room Service', 200)
        invalid = True

    elif (services == 2):
        guest.add_service('Movie Rental', 20)
        invalid = True

    elif (services == 3):
        guest.add_service('Room Service', 200)
        guest.add_service('Movie Rental', 20)
        invalid = True

    else:
        print('Invalid service type inputted.')

print(guest.name + " will check out on " + str(guest.check_out_date) + ".")

# Send the guest's bill
guest.send_bill()

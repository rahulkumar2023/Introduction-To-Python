from datetime import *

class HotelRoom:
    def __init__(self, room_number, available_date):

        # Initialize the HotelRoom object with a room number and an available date
        self.room_number = room_number
        self.available_date = available_date
        self.available = True

    def guest_check_in(self, some_guest):
        """ -------------------------------------------------------
        Checks a guest into a room and updates availability
        -------------------------------------------------------
        Parameters:
            Some_guest – the guest checking in (guest object)
        Returns:
            None
        -------------------------------------------------------
        """

        # Set the availability of the room to False
        self.available = False

        # If the room is a Taylor suite, set the available date to the check-out date of the guest plus 2 days.
        if isinstance(self, TaylorSuite):
            self.available_date = some_guest.check_out_date + timedelta(days=2)

        # If the room is a Suite, set the available date to the check-out date of the guest plus 1 day.
        elif isinstance(self, Suite):
            self.available_date = some_guest.check_out_date + timedelta(days=1)

        # Otherwise, set the available date to the check-out date of the guest.
        else:
            self.available_date = some_guest.check_out_date

class Suite(HotelRoom):
    def __init__(self, room_number, available_date):

        # Initialize a suite object by inheriting from HotelRoom and passing a room number and available date
        super().__init__(room_number, available_date)

class StandardRoom(HotelRoom):
    def __init__(self, room_number, available_date):

        # Initialize a StandardRoom object by inheriting from HotelRoom and passing a room number and available date
        super().__init__(room_number, available_date)

class TaylorSuite(HotelRoom):
    def __init__(self, room_number, available_date):

        # Initialize a Taylor suite object by inheriting from HotelRoom and passing a room number and available date
        super().__init__(room_number, available_date)

class Guest:
    def __init__(self, name, check_out_date):

        # Initialize a guest object with a name and check-out date
        self.name = name
        self.check_out_date = check_out_date

        # List of services for the guest
        self.services = []

        # Total bill for the guest
        self.total_bill = 0

    def add_service(self, service_name, service_cost):
        """ -------------------------------------------------------
        Adds a service to the bill of a guest
        -------------------------------------------------------
        Parameters:
            Service name – name of service (str)
            Service_cost - cost of the service (int)
        Returns:    None
        -------------------------------------------------------
        """

        # Add a service to the guest's bill by appending a service to the services list and incrementing the total bill
        self.services.append(Service(service_name, service_cost))
        self.total_bill += service_cost

    def send_bill(self):
        """ -------------------------------------------------------
        Based on the total services and bill total provides a Printed statement of all services with the total cost
        -------------------------------------------------------
        Parameters:    None
        Returns:       None
        ---------------------------------------------------
        """

        # Print out the bill for the guest with a statement for each service and the total cost
        print("The bill for " + self.name + " is:")

        for service in self.services:
            print("- " + service.service_name + ": $" + str(service.service_cost))

        print("Total: $" + str(self.total_bill))


class Service:
    def __init__(self, service_name, service_cost):

        # Initialize a service object with a service name and cost
        self.service_name = service_name
        self.service_cost = service_cost


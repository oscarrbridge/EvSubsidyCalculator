"""This program calculates the subsidy for someone to receive when ordering electric cars."""
EV_OPTIONS = {"REG": ["Audi e-tron", "Volkswagen ID 4", "Kia Nitro EV",
                      "BMW i3", "Polstar 2", "Tesla Model Y"],
              "TOP": ["Jaguar I-PACE", "Tesla Model 3", "Ford Mustang Mach-E",
                      "Volkswagen e_Golf", "Renault Zoe",
                      "Nissan Leaf"]}


def get_total_subsidy(car, event):
    """
    Calculate the total subsidy for the customer and return.

    :param car:
    :param event:
    :return:
    """
    return car + event


def total_car_subsidy(cars_on_order):
    """
    Work out the total subsidy of the cars together.

    :param cars_on_order:
    :return:
    """
    subsidy_received = 0

    for i in range(len(cars_on_order)):
        if cars_on_order[i] in EV_OPTIONS["REG"]:
            subsidy_received += 2000

        elif cars_on_order[i] in EV_OPTIONS["TOP"]:
            subsidy_received += 5000

    return subsidy_received


"""
    for cars_on_order in EV_OPTIONS["REG"]:
        print(cars_on_order)
        subsidy_received += 2000

    for cars_on_order in EV_OPTIONS["TOP"]:
        print(cars_on_order)
        subsidy_received += 5000
"""


# REG_EV_OPTIONS = $2000, TOP_EV_OPTIONS = $5000


def event_charge(order_type):
    """
    Calculate the subsidy received for the type of event.

    :param order_type:
    :return:
    """
    if order_type == "Promo event":
        return 400

    else:
        return 0
    # promo event adds $400


def add_car_to_order(car_to_add, cars_on_order):
    """
    Add each car the customer wants to a list.

    :param car_to_add:
    :param cars_on_order:
    :return:
    """
    add_cars = int(input("How many of these cars would you like to add? "))

    for i in range(1, add_cars + 1):
        cars_on_order.append(car_to_add)

    return cars_on_order


def get_order(cars_on_order):
    """
    Ask the customer what cars they want.

    Displays a list of all the cars
    Customer selects which car they would like and how many
    Customer must have a quantity greater than MIN_CARS
    :param cars_on_order:
    :return:
    """
    car_choice = 0
    min_cars = 5

    for i in range(0, len(EV_OPTIONS["REG"])):
        print("{}: {}".format(i + 1, EV_OPTIONS["REG"][i]))

    for i in range(0, len(EV_OPTIONS["TOP"])):
        print("{}: {}".format((i + 1) + len(EV_OPTIONS["TOP"]),
                              EV_OPTIONS["TOP"][i]))

    while car_choice not in range(1, (len(EV_OPTIONS["REG"] + EV_OPTIONS["TOP"]) - 1)) and len(
            cars_on_order) < min_cars:

        car_choice = 0
        try:
            car_option = int(input("What EV option would you like to add?: "))

            if car_option > ((len(EV_OPTIONS["REG"]) + len(EV_OPTIONS["TOP"]))):
                print("Please enter a valid option")

            elif car_option > len(EV_OPTIONS["REG"]) and car_option < (len(EV_OPTIONS["REG"]) + len(EV_OPTIONS["TOP"])):
                car_option = EV_OPTIONS["TOP"][(car_option - len(EV_OPTIONS["REG"])) - 1]
                order_list = add_car_to_order(car_option, cars_on_order)

            elif car_option < len(EV_OPTIONS["REG"]) and car_option > 0:
                car_option = EV_OPTIONS["REG"][car_option - 1]
                order_list = add_car_to_order(car_option, cars_on_order)

            else:
                car_option = 0

        except: #needs to change to exceptvalue error. 
            print("Please select a valid option")

    return order_list


def get_address():
    """
    Get the customers address.

    :return:
    """
    address = input("What is the customer's address?: ")

    return address


def get_phone_number():
    """
    Get the customers phone number.

    :return:
    """
    phone_number = input("What is the customer's phone number?: ")

    return phone_number


def get_order_type():
    """
    Return back what type of order the customer asks for.

    :return:
    """
    order_type = 0

    while order_type not in ["1", "2"]:
        order_type = input("1: Promo event \n2: Phone call ")
    if order_type == "1":
        return "Promo event"

    elif order_type == "2":
        return "Phone call"


def get_name():
    """
    Get the name of the customer.

    :return:
    """
    name = input("What is the customer's name?: ")

    return name


"""
def final_screen(orders):
    print(orders)

    return 3
    # Format all information in dictionary and print each using for loop
"""


def add_info():
    """
    Collect all information for the dictionary.

    :return:
    """
    car_order_list = []
    order_info = {}

    order_type = get_order_type()
    customer_name = get_name()
    phone_number = get_phone_number()
    address = get_address()
    cars_on_order = get_order(car_order_list)
    subsidy_of_cars = total_car_subsidy(cars_on_order)
    order_subsidy = event_charge(order_type)
    total_subsidy = get_total_subsidy(subsidy_of_cars, order_subsidy)

    order_info["Name"] = customer_name
    order_info["Phone number"] = phone_number
    order_info["Address"] = address
    order_info["Order type"] = order_type
    order_info["Cars on order"] = cars_on_order
    order_info["Subsidy of cars"] = subsidy_of_cars
    order_info["Order subsidy"] = order_subsidy
    order_info["Total Subsidy"] = total_subsidy

    # order_dict[(len(order_dict)+1)] = order_info

    return order_info


def join_info(current_order, order_info):
    """
    Join all received information into one dictionary.

    :param current_order:
    :param order_info:
    :return:
    """
    current_order[(len(current_order) + 1)] = order_info

    return current_order


def final(order_dict):
    """
    Display all the collected information from the day.

    :param order_dict:
    :return:
    """
    gap = ("=" * 50)
    overall_potential_cost = 0
    print("Thank you for using this program")
    print(gap)
    print("Registrations of Interest in EV Subsidy Received:")
    print(gap)
    """
    for orders in order_dict:
        print("Order: {}".format(orders))
        overall_potential_cost += order_dict[orders]["Total Subsidy"]
        for items in order_dict[orders]:
            if items == "Cars on order":
                occ_of_car = {}
                for car in order_dict[orders]["Cars on order"]:
                    occ_of_car = order_dict[orders]["Cars on order"].count(car)
                    print("{} x {} @ ${}".format(occ_of_car, car, 200))
            else:
                print("{}: {}".format(items, order_dict[orders][items]))
    """
    for orders in order_dict:
        if order_dict[orders] != "canceled":
            print("Order: {}".format(orders))
            overall_potential_cost += order_dict[orders]["Total Subsidy"]
            for items in order_dict[orders]:
                if items == "Cars on order":
                    cars_dict = {}
                    for car in order_dict[orders]["Cars on order"]:
                        if car in cars_dict.keys():
                            cars_dict[car] += 1
                        else:
                            cars_dict[car] = 1

                    for car_name in cars_dict.keys():
                        print("{} x {}".format(car_name, cars_dict[car_name]))

                else:
                    print("{}: {}".format(items, order_dict[orders][items]))
        
        else:
            print("Order {} was canceled".format(orders))
        print(gap)

    print("Total orders: {}".format(len(order_dict)))
    print("Overall potential cost of these orders = {}".format(overall_potential_cost))
    print(gap)
    return


def cancel_order(order_dict):

    operator_option = 0

    for key in order_dict.keys():
        print("Order : {}".format(key))

    while operator_option not in order_dict.keys():
        try:    
            operator_option = int(input("Which order would you like to cancel? "))
            if operator_option > len(order_dict):
                print("Please choose a valid option")

        except ValueError:
            print("Please choose a valid option")

    order_dict[operator_option] = "canceled"
    return order_dict


"""
    if operator_option in range(0, len(order_dict)):
        order_dict[operator_option] = "Canceled..."
        print("thing", order_dict[operator_option - 1])
        return order_dict

    else:
        order_dict[operator_option] = "Canceled"
        return order_dict
"""


"""
for i in range(0, len(order_dict) + 1):
    print("Order: {}".format(order_dict[(i + 1)]))
"""


"""
    order_dict[len(order_dict+1)] = customer_name
    order_dict[len(order_dict+1)] = phone_number
    order_dict[len(order_dict+1)] = address
    order_dict[len(order_dict+1)] = cars_on_order
    order_dict[len(order_dict+1)] = total_subsidy
    print(order_dict)
"""


# Get all information and add it all into a dictionary using the format below


def start():
    """
    Control the program, ask user which option they would like to use.

    :return:
    """
    orders = {}
    operator_option = "0"

    while operator_option not in ["1", "2", "3"]:
        try:
            operator_option = input("1: Add new order \n2: Show final orders \n3: Cancel order ")
            if operator_option == "1":
                operator_option = "0"
                order_info = add_info()
                all_orders = join_info(orders, order_info)

            elif operator_option == "2" and len(orders) >= 1:
                final(all_orders)
                return

            elif operator_option == "3" and len(orders) >= 1:
                all_orders = cancel_order(all_orders)
                operator_option = "0"

            elif len(orders) < 1:
                operator_option = "0"

        except TypeError:
            print("Please enter a valid option")
            operator_option = "0"


if __name__ == '__main__':
    start()

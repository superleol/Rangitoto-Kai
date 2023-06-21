"""This is an ordering system called rangitoto kai."""
# This is the constants section.
COST_OF_BUDGET_MENU_OPTIONS = 6
COST_OF_PREMIUM_MENU_OPTIONS = 9
DELIVERY_COST = 5

BUDGET_MENU_OPTIONS = [
  "Kawakawa spritzer", "Pork and Puha slider", "Pork and Watercress pie",
  "Paua and Prawn dumplings", "Kumara and Fennel salad", "Kina canapes", "k", "c"
]

PREMIUM_MENU_OPTIONS = [
  "Horopito Fish Collars", "Kawakawa Mussels", "Paua Porridge", "a"
]

TOTAl_ITEMS_THAT_CAN_BE_ORDERED = 3


# Constants section ends.


def main():
    """This function is for my main loop of my programme"""
    print("Welcome to Rangitoto Kai.")

    finished_day = 'n'

    while finished_day == 'n' or finished_day == 'no':
        create_order()
        finished_day = ''
        while finished_day != 'y' and finished_day != "yes" and finished_day != 'n' and finished_day != 'no':
            finished_day = input("Has your work day finished. Please enter 'yes' or 'no' you can also enter 'y' or 'n': ")

    # end of day, print summary
    print_end_of_day_summary()


def create_order():
    """This is the create order function"""
    # creates an empty dictionary for ordered items
    ordered_items = {}
    # creates an empty dictionary for customer info
    customer_info = {}
    # creates an empty dictionary for gst
    gst = {}

    # asks the user to input their name
    name = ''
    while not name.strip():
        name = input("\n\nPlease enter your name: ")

    customer_info.update({"User name: ": name})

    # prints hello, then users name
    print("Hello", name.strip())

    choose_food(ordered_items, gst, customer_info)

    # check if user wants to cancel the order
    cancel_option = ''
    while cancel_option != "n" and cancel_option != "no" and cancel_option != "yes" and cancel_option != "y":
        cancel_option = input("Do you want to cancel this order. Please enter 'yes' or 'no' you can also enter 'y' or 'n': ")

    if cancel_option == "yes" or cancel_option == "y":
        print("Ok, sure, the current order will be removed.")
    else:
        print_receipt(customer_info, ordered_items, gst)
        all_orders.append(ordered_items)
        all_customers.append(customer_info)
        all_gst.append(gst)


def print_end_of_day_summary():
    """This is the function at the end of the programme that prints out all the information for the day."""
    print("\n\nThank you for your hardwork today and thank you for using this program.")
    print("_________________________________________")
    print("Below is the food orders today: ")
    print("_________________________________________")

    index = 0
    total_incl_gst = 0
    total_excl_gst = 0
    while index < len(all_customers):
        print("\nOrder ", index+1, ":")
        print_receipt(all_customers[index], all_orders[index], all_gst[index])
        total_incl_gst = total_incl_gst + all_gst[index].get("Total incl GST")
        total_excl_gst = total_excl_gst + all_gst[index].get("Total excl GST")
        index += 1

    print("Total orders:", index)
    print("Day total incl GST: $", total_incl_gst)
    print("Day total excl GST: $", total_excl_gst)
    print("_________________________________________")


def print_receipt(cur_customer_info, cur_ordered_items, cur_gst):
    """This is the print receipt function."""
    print("Name: ", cur_customer_info.get("User name: "))
    print("Order type: ", cur_customer_info.get("Delivery type: "))
    if cur_customer_info.get("Delivery type: ") == "Delivery":
        print("Phone number: ", cur_customer_info.get("Phone number: "))
        print("Post code: ", cur_customer_info.get("Post code: "))
        print("Adress: ", cur_customer_info.get("Adress: "))

    print("Item ordered: ")
    for key, value in cur_ordered_items.items():
        if key in BUDGET_MENU_OPTIONS:
            print(value, " x ", key, " @ $", COST_OF_BUDGET_MENU_OPTIONS, " = $", int(value) * COST_OF_BUDGET_MENU_OPTIONS)
        elif key in PREMIUM_MENU_OPTIONS:
            print(value, " x ", key, " @ $", COST_OF_PREMIUM_MENU_OPTIONS, " = $", int(value) * COST_OF_PREMIUM_MENU_OPTIONS)

    print("Your total for incl GST is $", cur_gst.get("Total incl GST"))
    print("Your total for excl GST is $", cur_gst.get("Total excl GST"))
    print("\n")


def rangitoto_uber(customer_info):
    """This is the function for the delivery option."""
    post_code = input("Please enter your post code. The post codes that we can deliver too are 0620, 0630, and 0632: ")
    # checks if post code entered is 0632, 0620 or 0630
    while post_code != "0632" and post_code != "0620" and post_code != "0630":
        post_code = input("Please enter your post code. The post codes that we can deliver too are 0620, 0630, and 0632: ")
    adress = input("Please enter your adress: ")

    phone_number = input("Please enter your phone number: ")
    while not phone_number.isdigit():
        phone_number = input("Please enter your phone number: ")
    if phone_number.isdigit():
        while len(phone_number) < 9 or len(phone_number) > 11:
            print("This phone number is invalid.")
            phone_number = input("Please enter your phone number: ")

    customer_info.update({
        "Phone number: ": phone_number,
        "Post code: ": post_code,
        "Adress: ": adress
      })


def delivery_option():
    """This function asks the user wheather they want to have their item delivered or pickup their item."""
    uber_input = ''
    while uber_input != "pickup" and uber_input != "delivery":
        uber_input = input("Is this order for pickup or rangitoto uber delivery. Please enter 'pickup' for pickup and 'delivery' for our rangitoto uber delivery: ")

    return uber_input


def choose_food(ordered_items, gst, customer_info):
    """This is the choose food function."""
    cost_of_items = []
    # creates an empty dictionary for total cost of items
    total_cost = {}

    print("We have a budget menu and a premium menu.")
    print("In the budget menu we have", BUDGET_MENU_OPTIONS)
    print("In the premium budget menu we have", PREMIUM_MENU_OPTIONS)

    # take orders
    while len(ordered_items) < TOTAl_ITEMS_THAT_CAN_BE_ORDERED:
        input_item = input("Please choose the item that you would like to order: ")
        while (input_item not in BUDGET_MENU_OPTIONS) and (input_item not in PREMIUM_MENU_OPTIONS):
            print("Sorry, that item is not avaliable.")
            input_item = input("Please choose the item that you would like to order: ")

        quantity = input("Please input the quantity that you would like: ")
        while not quantity.isdigit():
            print("Please enter a number")
            quantity = input("Please input the quantity that you would like: ")

        # updates the dictionary
        ordered_items.update({
           input_item: quantity
         })

        # print order and calculate price
        print("You ordered", input_item, "and your quantity that you ordered is", quantity)

        if input_item in BUDGET_MENU_OPTIONS:
            total_cost.update(
            {"Total cost of item: ": int(quantity) * COST_OF_BUDGET_MENU_OPTIONS})
        cost_of_items.append(int(quantity) * COST_OF_BUDGET_MENU_OPTIONS)

        if input_item in PREMIUM_MENU_OPTIONS:
            total_cost.update(
            {"Total cost of item: ": int(quantity) * COST_OF_PREMIUM_MENU_OPTIONS})
        cost_of_items.append(int(quantity) * COST_OF_PREMIUM_MENU_OPTIONS)

        print("The total cost of your ordered item is $", total_cost["Total cost of item: "])
        gst.update({
           "Total incl GST": round(sum(cost_of_items), 2),
           "Total excl GST": round((sum(cost_of_items) / 1.15), 2)
         })
        print("Your total for incl GST is $", gst.get("Total incl GST"))
        print("Your total for excl GST is $", gst.get("Total excl GST"))

        order_another_item = ''
        while order_another_item != "yes" and order_another_item != "y" and order_another_item != "no" and order_another_item != "n":
            order_another_item = input("Do you want to order another item. Please enter 'yes' or 'no' you can also enter 'y' or 'n': ")

        if order_another_item == "no" or order_another_item == "n":
            break
        elif len(ordered_items) == 3:
            print("Sorry you cannot order more than 3 items.")

    delivery = delivery_option()
    if delivery == "delivery":
        rangitoto_uber(customer_info)
        customer_info.update({"Delivery type: ": "Delivery"})
        gst.update({"Total incl GST": float(gst.get("Total incl GST")) + 5})
        gst.update({"Total excl GST": float(gst.get("Total excl GST")) + 4.35})
    else:
        customer_info.update({"Delivery type: ": "Pick up"})


# creates a list for all of the orders
all_orders = []
# creates a list for order today
all_customers = []
# creates an empty list for all gst
all_gst = []

main()

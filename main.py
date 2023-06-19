"""This is an ordering system called rangitoto kai."""
# This is the constants section.
COST_OF_BUDGET_MENU_OPTIONS = 6
COST_OF_PREMIUM_MENU_OPTIONS = 9

BUDGET_MENU_OPTIONS = ["kawakawa spritzer", "Pork and Puha slider", "Pork and Watercress pie", "Paua and Prawn dumplings", "Kumara and Fennel salad", "Kina canapes"]

PREMIUM_MENU_OPTIONS = ["Horopito Fish Collars", "Kawakawa Mussels", "Paua Porridge"]

TOTAl_ITEMS_THAT_CAN_BE_ORDERED = 3

# Constants section ends.


def main():
    """This function is for my main loop of my programme"""
    reset_programme()
    print("Welcome to Rangitoto Kai.")
    # asks the user to input their name
    name = input("Please enter your name: ")
    while not name.strip():
        name = input("Please enter your name: ")

    # prints hello, then users name
    print("Hello", name.strip())

    choose_food()


def reset_programme():
    """This function resets the programme."""
    # clears the customer info dictionary
    customer_info.clear()
    # clears the ordered items dictionary
    ordered_items.clear()
    # clears the total cost dictionary
    total_cost.clear()
    gst.clear()


def thank_you_msg():
    """This is the function at the end of the programme that prints out all the 
    information for the day."""
    print("Thank you for your hardwork today and thank you for using this program.")
    print("_______________________________________")
    print("Below is the food orders today: ")
    print("_________________________________________")
    print("Name: ", customer_info.get("User name: "),"\n",
          "Phone number: ", customer_info.get("Phone number: "),"\n",
          "Post code: ", customer_info.get("Post code: "),"\n",
          "Adress: ",customer_info.get("Adress: "))
    print("The item that you ordered is: ", ordered_items.get("Item you ordered: "), "\n",
          "Quantity: ", ordered_items.get("Quantity: "))
    print("Your total for incl GST is $", gst.get("Total incl GST"),"\n",
          "Your total for excl GST is $",gst.get("Total excl GST"))
  
    main()


def clear_data():
    """This is the clear data function."""
    # clears the customer info dictionary
    customer_info.clear()
    # clears the ordered items dictionary
    ordered_items.clear()
    # clears the total cost dictionary
    total_cost.clear()
    thank_you_msg()
    main()


def print_receipt():
    """This is the print receipt function."""
    print("Name: ", customer_info.get("User name: "),"\n",
          "Phone number: ", customer_info.get("Phone number: "),"\n",
          "Post code: ", customer_info.get("Post code: "),"\n",
          "Adress: ",customer_info.get("Adress: "))
    print("The item that you ordered is: ", ordered_items.get("Item you ordered: "), "\n",
          "Quantity: ", ordered_items.get("Quantity: "))
    print("Your total for incl GST is $", gst.get("Total incl GST"),"\n",
          "Your total for excl GST is $",gst.get("Total excl GST"))

    cancel_option = input("Do you want to cancel this order. Please enter 'yes' or 'no' you can also enter 'y' or 'n': ")
    if cancel_option == "yes" or cancel_option == "y":
        print("Ok, sure")
        main()
    elif cancel_option == "no" or cancel_option == "n":
        print("OK")
        finished_day = input("Has your work day finished. Please enter 'yes' or 'no' you can also enter 'y' or 'n': ")
        if finished_day == 'n' or finished_day == 'no':
            main()
        elif finished_day == 'y' or finished_day == 'yes':
            thank_you_msg()
    else:
        print_receipt()


def order_pickup():
    """This is the pickup item function."""
    order_finished = input("Is this order finished. Please enter 'yes' or 'no' you can also enter 'y' or 'n': ")
    if order_finished == "yes" or order_finished == "y":
        print_receipt()
    elif order_finished == "no" or "n":
        choose_food()
    else:
        order_pickup()


def rangitoto_uber():
    """This is the function for the delivery option."""
    post_code = input("Please enter your post code. The post codes that we can deliver too are 0620, 0630, and 0632: ")
    # checks if post code entered is 0632, 0620 or 0630
    while post_code != "0632" and post_code != "0620" and  post_code != "0630":
      post_code = input("Please enter your post code. The post codes that we can deliver too are 0620, 0630, and 0632: ")
    adress = input("Please enter your adress: ")

    user_name = input("Please enter your name: ")
    phone_number = input("Please enter your phone number: ")
    while not phone_number.isdigit():
        phone_number = input("Please enter your phone number: ")
        if phone_number.isdigit():
            while len(phone_number) < 9 or len(phone_number) > 11:
                print("This phone number is invalid.")
                phone_number = input("Please enter your phone number: ")

    customer_info.update({
    "User name: ": user_name,
    "Phone number: ": phone_number,
    "Post code: ": post_code,
    "Adress: ": adress
    })

    finished =  input("Is this order finished. Please enter 'yes' or 'no' you can also enter 'y' or 'n': ")
    while finished != "y" and  finished != "yes":
      if finished == "n" or finished == "no":
        add_item = input("Would you like to add more items. Please enter 'yes' or 'no' you can also enter 'y' or 'n': ")
        if add_item == "y" or add_item == "yes":
            choose_food()
        else:
            rangitoto_uber()
      finished =  input("Is this order finished. Please enter 'yes' or 'no' you can also enter 'y' or 'n': ")
    print("Ok")
    print_receipt()
    




    return customer_info


def delivery_option():
    """This function asks the user wheather they want to have their item delivered 
    or pickup their item."""
    uber_input = input("Is this order for pickup or rangitoto uber delivery. Please enter 'pickup' for pickup and 'delivery' for our rangitoto uber delivery: ")
    if uber_input == "pickup":
        order_pickup()
    elif uber_input == "delivery":
        print("Ok")
        rangitoto_uber()
    else:
        delivery_option()


def choose_food():
    """This is the choose food function."""
    print("We have a budget menu and a premium menu.")
    print("In the budget menu we have", BUDGET_MENU_OPTIONS)
    print("In the premium budget menu we have", PREMIUM_MENU_OPTIONS)

    input_item = input("Please choose the item that you would like to order: ")
    quantity = input("Please input the quantity that you would like: ")
    while not quantity.isdigit():
        quantity = input("Please input the quantity that you would like: ")

    

    # updates the dictionary
    ordered_items.update({
    "Item you ordered: ": input_item,
    "Quantity: ": quantity
    })

    x = len(ordered_items)
    print(x)

    print("You ordered", input_item, "and your quantity that you ordered is",quantity)

    

  
    if input_item in BUDGET_MENU_OPTIONS:
        total_cost.update({
        "Total cost of item: ": int(quantity) * COST_OF_PREMIUM_MENU_OPTIONS
        })
        print("The total cost of your ordered item is $", total_cost["Total cost of item: "])
        order_another_item = input("Do you want to order another item. Please enter 'yes' or 'no' you can also enter 'y' or 'n': ")
        if order_another_item == "yes" or order_another_item == "y":
            # checks if items in the dictionary is greater than 3
            if x < TOTAl_ITEMS_THAT_CAN_BE_ORDERED:
                choose_food()
            # if the items in the dictionary is greater than 3 then the user cannot order anything more
            elif x > TOTAl_ITEMS_THAT_CAN_BE_ORDERED or x == TOTAl_ITEMS_THAT_CAN_BE_ORDERED:
              gst.update({
              "Total incl GST": sum(total_cost.values()),
              "Total excl GST": int(sum(total_cost.values())/1.15
                                   )})
        elif order_another_item == "no" or order_another_item == "n":
              gst.update({
              "Total incl GST": sum(total_cost.values()),
              "Total excl GST": int(sum(total_cost.values())/1.15
                                   )})
        # checks if items in dictionary is greater than 3
        if x < TOTAl_ITEMS_THAT_CAN_BE_ORDERED:
             a = total_cost.get(input_item)
             print("Total incl GST $", gst.get("Total incl GST"),"\n",
                   "Total excl GST ", gst.get("Total excl GST"))
             delivery_option()
             # if the items in the dictionsty is greater than 3 then the user cannot order anything more
        elif x > TOTAl_ITEMS_THAT_CAN_BE_ORDERED or x == TOTAl_ITEMS_THAT_CAN_BE_ORDERED:
             print("Sorry you cannot order more than 3 items.")
             gst.update({
             "Total incl GST": sum(total_cost.values()),
             "Total excl GST": int(sum(total_cost.values())/1.15
                                   )})
             delivery_option()
    elif input_item in PREMIUM_MENU_OPTIONS:
        total_cost.update({
        "Total cost of item: ": int(quantity) * COST_OF_PREMIUM_MENU_OPTIONS
        })
        print("The total cost of your ordered item is $", total_cost["Total cost of item: "])
        order_another_item = input("Do you want to order another item. Please enter 'yes' or 'no' you can also enter 'y' or 'n': ")
        if order_another_item == "yes" or order_another_item == "y":
            # checks if items in dictionary is greater than 3
            if x < TOTAl_ITEMS_THAT_CAN_BE_ORDERED:
                choose_food()
                # if the items in the dictionary is greater than 3 then the user cannot order anything more
            elif x > TOTAl_ITEMS_THAT_CAN_BE_ORDERED or x == TOTAl_ITEMS_THAT_CAN_BE_ORDERED:
                print("Sorry you cannot order more than 3 items.")
                gst.update({
                "Total incl GST": sum(total_cost.values()),
                "Total excl GST": int(sum(total_cost.values())/1.15
                                   )})
                delivery_option()
        elif order_another_item == "n" or order_another_item == "no":
            print("ok")
            gst.update({
            "Total incl GST": sum(total_cost.values()),
            "Total excl GST": int(sum(total_cost.values())/1.15
                                   )})
            delivery_option()
    else:
        ordered_items.pop(input_item, quantity)
        print("Sorry, that item is not avaliable.")
        choose_food()


# creates an empty dictionary for ordered items
ordered_items = {}
# creates an empty dictionary for customer info
customer_info = {}
# creates an empty dictionary for total cost of items
total_cost = {}
# creates an empty dictionary for gst
gst = {}



main()

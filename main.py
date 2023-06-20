"""This is an ordering system called rangitoto kai."""
# This is the constants section.
COST_OF_BUDGET_MENU_OPTIONS = 6
COST_OF_PREMIUM_MENU_OPTIONS = 9

BUDGET_MENU_OPTIONS = [
  "Kawakawa spritzer", "Pork and Puha slider", "Pork and Watercress pie",
  "Paua and Prawn dumplings", "Kumara and Fennel salad", "Kina canapes"
]

PREMIUM_MENU_OPTIONS = [
  "Horopito Fish Collars", "Kawakawa Mussels", "Paua Porridge"
]

TOTAl_ITEMS_THAT_CAN_BE_ORDERED = 3

delivery_charge = 5

# Constants section ends.


def main():
  """This function is for my main loop of my programme"""
  reset_programme()
  print("Welcome to Rangitoto Kai.")

  create_order()

  finished_day = ''
  while finished_day != 'y' and finished_day != "yes" and finished_day != 'n' and finished_day != 'no':
    finished_day = input(
      "Has your work day finished. Please enter 'yes' or 'no' you can also enter 'y' or 'n': "
    )

  while finished_day == 'n' or finished_day == 'no':
    all_orders.append([ordered_items, customer_info, total_cost, gst])
    create_order()

  # end of day, print summary
  thank_you_msg()


def create_order():
  # asks the user to input their name
  name = input("Please enter your name: ")
  while not name.strip():
    name = input("Please enter your name: ")

  # prints hello, then users name
  print("Hello", name.strip())

  choose_food()
  delivery = delivery_option()
  if delivery == "delivery":
    rangitoto_uber()

  # check if user wants to cancel the order
  cancel_option = ''
  while cancel_option != "n" and cancel_option != "no" and cancel_option != "yes" and cancel_option != "y":
    cancel_option = input(
      "Do you want to cancel this order. Please enter 'yes' or 'no' you can also enter 'y' or 'n': "
    )

  if cancel_option == "yes" or cancel_option == "y":
    print("Ok, sure")
    reset_programme()  ########todo
  else:
    print_receipt()


def reset_programme():
  """This function resets the programme."""
  # clears the customer info dictionary
  customer_info.clear()
  # clears the ordered items dictionary
  ordered_items.clear()
  # clears the total cost dictionary
  total_cost.clear()
  # clears the gst dictionary
  gst.clear()
  # clears the cost of items list
  cost_of_items.clear()
  all_orders.clear()


def thank_you_msg():
  """This is the function at the end of the programme that prints out all the 
    information for the day."""
  print(
    "Thank you for your hardwork today and thank you for using this program.")
  print("_______________________________________")
  print("Below is the food orders today: ")
  print("_________________________________________")
  all_orders.append([ordered_items, customer_info, total_cost, gst])
  orders_today.append([all_orders])
  print(orders_today)

  main()


def print_receipt():
  """This is the print receipt function."""
  print("Name: ", customer_info.get("User name: "), "\n", "Phone number: ",
        customer_info.get("Phone number: "), "\n", "Post code: ",
        customer_info.get("Post code: "), "\n", "Adress: ",
        customer_info.get("Adress: "))

  print("Item ordered: ")
  for key in ordered_items
    print()
  """
  print("The item that you ordered is: ",
        ordered_items.get("Item you ordered: "), "\n", "Quantity: ",
        ordered_items.get("Quantity: "))
  print("Your total for incl GST is $", gst.get("Total incl GST"), "\n",
        "Your total for excl GST is $", gst.get("Total excl GST"))
"""

def rangitoto_uber():
  """This is the function for the delivery option."""
  post_code = input(
    "Please enter your post code. The post codes that we can deliver too are 0620, 0630, and 0632: "
  )
  # checks if post code entered is 0632, 0620 or 0630
  while post_code != "0632" and post_code != "0620" and post_code != "0630":
    post_code = input(
      "Please enter your post code. The post codes that we can deliver too are 0620, 0630, and 0632: "
    )
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


def delivery_option():
  """This function asks the user wheather they want to have their item delivered 
    or pickup their item."""
  uber_input = ''
  while uber_input != "pickup" and uber_input != "delivery":
      uber_input = input(
      "Is this order for pickup or rangitoto uber delivery. Please enter 'pickup' for pickup and 'delivery' for our rangitoto uber delivery: ")

  return uber_input


def choose_food():
  """This is the choose food function."""
  print("We have a budget menu and a premium menu.")
  print("In the budget menu we have", BUDGET_MENU_OPTIONS)
  print("In the premium budget menu we have", PREMIUM_MENU_OPTIONS)
  input_item = input("Please choose the item that you would like to order: ")
  while (input_item not in BUDGET_MENU_OPTIONS) and (input_item not in PREMIUM_MENU_OPTIONS) :
    print("Sorry, that item is not avaliable.")
    input_item = input("Please choose the item that you would like to order: ")
    
  quantity = input("Please input the quantity that you would like: ")
  while not quantity.isdigit():
    print("Please enter a number")
    quantity = input("Please input the quantity that you would like: ")

  
  # updates the dictionary
  ordered_items.update({
    input_item : quantity
  })

  x = len(ordered_items)

  print("You ordered", input_item, "and your quantity that you ordered is",
        quantity)

  if input_item in BUDGET_MENU_OPTIONS:
    total_cost.update(
      {"Total cost of item: ": int(quantity) * COST_OF_BUDGET_MENU_OPTIONS})
    cost_of_items.append(int(quantity) * COST_OF_BUDGET_MENU_OPTIONS)
    print("The total cost of your ordered item is $",
          total_cost["Total cost of item: "])
    order_another_item = input(
      "Do you want to order another item. Please enter 'yes' or 'no' you can also enter 'y' or 'n': "
    )
    while order_another_item != "yes" and order_another_item != "y":
      if order_another_item == "no" or order_another_item == "n":
        gst.update({
          "Total incl GST": sum(cost_of_items),
          "Total excl GST": int(sum(cost_of_items) / 1.15)
        })
        return
      order_another_item = input(
        "Do you want to order another item. Please enter 'yes' or 'no' you can also enter 'y' or 'n': "
      )

    # checks if items in the dictionary is greater than 3
    if x < TOTAl_ITEMS_THAT_CAN_BE_ORDERED:
      choose_food()
      # if the items in the dictionary is greater than 3 then the user cannot order anything more
    elif x >= TOTAl_ITEMS_THAT_CAN_BE_ORDERED:
      gst.update({
        "Total incl GST": sum(cost_of_items),
        "Total excl GST": int(sum(cost_of_items) / 1.15)
      })
      return
  elif input_item in PREMIUM_MENU_OPTIONS:
    total_cost.update(
      {"Total cost of item: ": int(quantity) * COST_OF_PREMIUM_MENU_OPTIONS})
    cost_of_items.append(int(quantity) * COST_OF_PREMIUM_MENU_OPTIONS)

    print("The total cost of your ordered item is $",
          total_cost["Total cost of item: "])
    order_another_item = input(
      "Do you want to order another item. Please enter 'yes' or 'no' you can also enter 'y' or 'n': "
    )
    while order_another_item != "yes" and order_another_item != "y":
      if order_another_item == "n" or order_another_item == "no":
        print("ok")
        gst.update({
          "Total incl GST": sum(cost_of_items),
          "Total excl GST": int(sum(cost_of_items) / 1.15)
        })
        return
      order_another_item = input(
        "Do you want to order another item. Please enter 'yes' or 'no' you can also enter 'y' or 'n': "
      )

    if x < TOTAl_ITEMS_THAT_CAN_BE_ORDERED:
      choose_food()
      # if the items in the dictionary is greater than 3 then the user cannot order anything more
    elif x > TOTAl_ITEMS_THAT_CAN_BE_ORDERED or x == TOTAl_ITEMS_THAT_CAN_BE_ORDERED:
      print("Sorry you cannot order more than 3 items.")
      gst.update({
        "Total incl GST": sum(cost_of_items),
        "Total excl GST": int(sum(cost_of_items) / 1.15)
      })
      return



# creates an empty dictionary for ordered items
ordered_items = {}
# creates an empty dictionary for customer info
customer_info = {}
# creates an empty dictionary for total cost of items
total_cost = {}
# creates an empty dictionary for gst
gst = {}
# creates a list for cost of items
cost_of_items = []
# creates a list for all of the orders
all_orders = []
# creates a list for order today
orders_today = []

main()

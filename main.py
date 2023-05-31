import os
cost_of_budget_menu_options = 6
cost_of_premium_menu_options = 9

def main():
  reset_programme()
  print("Welcome to Rangitoto Kai.")
  #asks the user to input their name
  name = input("Please enter your name: ")
  while not name.strip():
    name = input("Please enter your name: ")

  #prints hello, then users name
  print("Hello",name.strip())



  choose_food()

def reset_programme():
  os.remove("customer_info.txt")
  os.remove("ordered_items.txt")
  f = open("customer_info.txt","w")
  f2 = open("ordered_items.txt","w")

def thank_you_msg():
  print("Thank you")

def clear_data():
  open('customer_info.txt', 'w').close()
  open('ordered_items.txt', 'w').close()
  thank_you_msg()
  main()

def print_receipt():
  #opens a file called customer_info.txt
  f = open("customer_info.txt")
  #reads content inside the file
  content = f.read()
  #prints out the content inside the file
  print(content)
  #closes the file
  f.close()

  #opens a file called ordered_items.txt
  f2 = open("ordered_items.txt")
  #reads content inside the file
  content2 = f2.read()
  #prints out the content inside the file
  print(content2)
  #closes the file
  f.close()

  cancel_option = input("Do you want to cancel this order: ")
  if cancel_option == "yes" or cancel_option == "y":
    print("Ok, sure")
    main()
  elif cancel_option == "no" or cancel_option == "n":
    print("OK")
    clear_data()
  else:
    print_receipt()


def order_pickup():
  order_finished = input("Is this order finished: ")
  if order_finished == "yes" or order_finished == "y":
    print_receipt()
  elif order_finished == "no" or "n":
    choose_food()
  else:
    order_pickup()

def delete_info():
  with open(r"ordered_items.txt")as fp:
   #checks how much line are in the text file
   x = len(fp.readlines())

   with open('ordered_items.txt','r') as fr:
    # reads the file line by line
    lines = fr.readlines()
    #pointer for position
    ptr = 1
    #opening file in writing mode
    with open('ordered_items.txt','w') as fw:
     for line in lines:
       #removes the 3rd line
       if ptr != x:
         fw.write(line)
       ptr +=1
    print("Sorry, we cannot deliver to that postcode.")
    rangitoto_uber()



def rangitoto_uber():
  post_code = input("Please enter your post code: ")
  #checks if post code entered is 0632, 0620 or 0630
  if post_code == "0632" or post_code == "0620" or post_code == "0630":
    adress = input("Please enter your adress: ")
    
    user_name = input("Please enter your name: ")
    phone_number = input("Please enter your phone number: ")
    while not phone_number.isdigit():
      phone_number = input("Please enter your phone number: ")
    if phone_number.isdigit():
        while len(phone_number) < 9 or len(phone_number) > 11:
          print("This phone number is invalid.")
          phone_number = input("Please enter your phone number: ")
        
    
          
      
      
      
    #opens a file called customer_info.txt and appens to this file
    info = open("customer_info.txt","a")
    #writes users name in this file
    info.write(user_name)
    info.write("\n")
    #writes users phone number in this file
    info.write(phone_number)
    info.write("\n")
    #writes users post code in this file
    info.write(post_code)
    info.write("\n")
    #writes users adress in this file
    info.write(adress)
    info.write("\n")
    #closes this file
    info.close()
    finished =  input("Is this order finished: ")
    if finished == "y" or finished == "yes":
      print("Ok")
      print_receipt()
    elif finished == "n" or finished == "no":
      add_item = input("Would you like to add more items: ")
      if add_item == "y" or add_item == "yes":
        choose_food()
      else:
        rangitoto_uber()
    
  else:
    delete_info()
  



def delivery_option():
  uber_input = input("Is this order for pickup or rangitoto uber delivery: ")
  if uber_input == "pickup":
    order_pickup()
  elif uber_input == "rangitoto uber delivery":
    print("Ok")
    rangitoto_uber()
  else:
    delivery_option()
    
def delete_item():
  with open(r"ordered_items.txt")as fp:
    #checks how much line are in the text file
    x = len(fp.readlines())
  with open('ordered_items.txt','r') as fr:
   #reads file line by line
   lines = fr.readlines()
   #pointer for position
   ptr = 1
   #opens file in writing mode
   with open('ordered_items.txt','w') as fw:
     for line in lines:
       #removes the third line from file
       if ptr != x:
         fw.write(line)
       ptr +=1
  
  print("Sorry, we don't have that type of item.")
  choose_food()
  


def choose_food():
  print("We have a budget menu and a premium menu.")
  print("In the budget menu we have", budget_menu_options)
  print("In the premium budget menu we have", premium_menu_options)

  input_item = input("Please choose the item that you would like to order: ")
  #opens a file called ordered_items.txt and appends to it
  text_file = open("ordered_items.txt", "a")
  #adds to the file
  text_file.write(input_item)
  text_file.write("\n")
  #closes the file
  text_file.close()
  with open(r"ordered_items.txt")as fp:
    #checks how much line are in the text file
    x = len(fp.readlines())
    print('Total lines:', x)
  
  


  if input_item in budget_menu_options:
    print("Ok")
    order_another_item = input("Do you want to order another item: ")
    if order_another_item == "yes" or "y":
      #checks if items in file is greater than 3
      if x < 3:
        choose_food()
      #if the items in the file is greater than 3 then the user cannot order anything more
      elif x > 3 or x == 3:
        print("Sorry you cannot order more than 3 items.")
        delivery_option()
    elif order_another_item == "no" or "n":
      delivery_option()
    else:
      choose_food()
      #checks if items in file is greater than 3
      if x < 3:
        delivery_option()
      #if the items in the file is greater than 3 then the user cannot order anything more
      elif x > 3 or x == 3:
        print("Sorry you cannot order more than 3 items.")
        delivery_option()
  elif input_item in premium_menu_options:
    print("Ok")
    order_another_item = input("Do you want to order another item: ")
    if order_another_item == "yes" or order_another_item == "y":
      #checks if items in file is greater than 3
      if x < 3: 
       choose_food()
      #if the items in the file is greater than 3 then the user cannot order anything more
      elif x > 3 or x == 3:
        print("Sorry you cannot order more than 3 items.")
        delivery_option()
    elif order_another_item == "n" or order_another_item == "no":
      print("ok")
      delivery_option()
  else:
    delete_item()



        


budget_menu_options = ["kawakawa spritzer", "Pork and Puha slider", "Pork and Watercress pie", "Paua and Prawn dumplings", "Kumara and Fennel salad", "Kina canapes"]

premium_menu_options = ["Horopito Fish Collars", "Kawakawa Mussels","Paua Porridge"]

main()
#Separate dictionary for category. Format: (item, price, quantity)
foods = {
    'A1': ("Chips", 3, 10),
    'A2': ("Biscuit", 2, 10),
    'A3': ("Chocolate", 3, 10),
    'A4': ("Sandwich", 5.50, 10)
}

drinks = {
    'B1': ("Water", 1.50, 10),
    'B2': ("Juice", 3.50, 10),
    'B3': ("Coffee", 5, 10), 
    'B4': ("Soda", 3, 10),
}

# Displays menu and takes user input
def display():
    print("\nWelcome to the Machine!") # Greetings
    print("Please select a category.") # Asks user for category (Foods or Drinks)
    print("\nCategory:")

    selected_item = None # Store the selected item

    while True: #Loop to ensure user enters correct
        category = input("Foods or Drinks: ").capitalize() # User input

        # If user choose Foods category
        if category == "Foods":
            print("\nMenu for Foods:") # Display items for foods
            for code, (item, price, quantity) in foods.items():
                # Iterating through the foods dictionary and displaying each item
                print(f"{code}: {item} - {price:.2f} AED. (Available: {quantity})")

            print("\nChoose your order in the given menu.") # Asks user for order
            while True: # Loop to ensure user enters correct item code
                code = input("\nEnter the item code: ").upper() # User enter code of item
                if code in foods: # If entered code is in foods dictionary
                    selected_item = foods[code] # Retrieve item details
                    break
                else:
                    print("\nInvalid code, please try again.")  # If invalid item code is entered, user will try again
            break

        # If user choose Drinks category             
        elif category == "Drinks":
            print("\nMenu for Drinks:")
            for code, (item, price, quantity) in drinks.items():
                # Iterating through the foods dictionary and displaying each item
                print(f"{code}: {item} - {price:.2f} AED (Available: {quantity})")

            print("\nChoose your order in the given menu.")
            while True: # Loop to ensure user enters correct item code
                code = input("\nEnter the item code: ").upper() # User enter code of item
                if code in drinks: # If entered code is in drinks dictionary
                    selected_item = drinks[code] # Retrieve item details
                    break
                else:
                    print("\nInvalid code, please try again.")  # If invalid item code is entered, user will try again
            break

        else: 
            print("\nInvalid category. Please start again.")  # If the category is invalid

    return selected_item # Return the selected item

#Payment from the user. Ensure the user pays enough and return change
def payment(price, quantity):
    total_paid = 0 # Track the amount inserted
    total_price = price * quantity # Total price is the item price multiplied by the quantity ordered

    while True:
        try: # Ask for payment
            amount_entered = float(input(f"Please instert {total_price - total_paid:.2f} AED for the item: "))
            total_paid += amount_entered  # Add the entered amount to the total paid

            # If the total payment is enough
            if total_paid >= total_price:
                change = total_paid - total_price
                if change > 0:
                    print(f"Change returned: {change:.2f}AED")
                elif change == 0:
                    print("No change, exact amount recieved.")
                return change # Return change

            # If the user hasn't paid enough, shows how much more is needed
            else:
                short = total_price - total_paid
                print(f"Insufficient amount. Please instert {short:.2f} AED more.")

        except ValueError:
            print("Invalid amount, please insert the specific amount.")

# Dispense product after payment
def dispense(item):
    print(f"\nDispensing {item[0]}...") # Dispensing the item
    print(f"Enjoy your {item[0]}!\n")

# Main
def machine():
    item = display() # Display the menu and get selected item

    if item: # If a valid item was selected
        code, price, quantity = item # Unpack the selected item
        print(f"\nYou selected: {code} price: {price:.2f} AED. (Availability: {quantity})")

        quantity_ordered = int(input(f"How many {item[0]} would you like to purchase? (Available: {quantity}): "))
        
        if quantity_ordered > 0 and quantity_ordered <= quantity:
            change = payment(price, quantity_ordered) # Process payment and get change

            dispense(item) # Dispense the item
            print(f"Thank you for your purchase!")

            more = input("\nWould you like to buy something else? (Yes or No): ").capitalize()
            if more == "Yes":
                machine()  # Restart the process
            
            else:
                print("Thank you for using the Vending Machine. Goodbye!")  # End message
        elif quantity_ordered < quantity:
            print("Out of stock, would you like to buy another item?")
            another_item = input("Yes or No: ")

            if another_item == "Yes":
                display()
            elif another_item == "No":
                print("We apologize for not having stocks of you wanted item.")

        else:
            print("Invalid quantity, Please try again.")
            

# Run the machine function
machine()
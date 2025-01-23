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
    print("\n\033[1m\033[4mWelcome to the Machine!\033[0m") # Greetings
    print("\n******************** \nPlease select a category.") # Asks user for category (Foods or Drinks)
    print("\n\033[1m\033[4mCategory:\033[0m")

    selected_item = None # Store the selected item

    while True: #Loop to ensure user enters correct
        category = input("Foods or Drinks: ").capitalize() # User input

        # If user choose Foods category
        if category == "Foods":
            print("\n********************\nMenu for Foods:") # Display items for foods
            for code, (item, price, quantity) in foods.items():
                # Iterating through the foods dictionary and displaying each item
                print(f"\033[96m{code}:\033[0m {item} - {price:.2f} AED. \033[94m(Available: \033[1m{quantity})\033[0m")

            print("\nChoose your order in the given menu.") # Asks user for order
            while True: # Loop to ensure user enters correct item code
                code = input("\nEnter the item code: ").upper() # User enter code of item
                if code in foods: # If entered code is in foods dictionary
                    if foods[code][2] > 0:  # Check if the item is in stock
                        selected_item = (code, *foods[code]) # Retrieve item details
                        break
                    else:
                        print("\nSorry, the item is not available/out of stock.")
                else:
                    print("\nInvalid code, please try again.")  # If invalid item code is entered, user will try again
            break

        # If user choose Drinks category             
        elif category == "Drinks":
            print("\nMenu for Drinks:")
            for code, (item, price, quantity) in drinks.items():
                # Iterating through the foods dictionary and displaying each item
                print(f"{code}: {item} - {price:.2f} AED. \033[96m(Available: {quantity}\033[0m)")

            print("\nChoose your order in the given menu.")
            while True: # Loop to ensure user enters correct item code
                code = input("\nEnter the item code: ").upper() # User enter code of item
                if code in drinks: # If entered code is in drinks dictionary
                    if drinks[code][2] > 0:  # Check if the item is in stock
                        selected_item = (code, *drinks[code]) # Retrieve item details
                        break
                    else:
                        print("\nSorry, the item is not available/out of stock.")
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
            amount_entered = float(input(f"********************\nPlease instert\033[91m {total_price - total_paid:.2f} AED\033[0m for the item: "))
            total_paid += amount_entered  # Add the entered amount to the total paid

            # If the total payment is enough
            if total_paid >= total_price:
                change = total_paid - total_price
                if change > 0:
                    print(f"Change returned: \033[36m{change:.2f}AED\033[0m")
                elif change == 0:
                    print("\033[36mNo change, exact amount recieved. \033[0m")
                return change # Return change

            # Shows how much more is needed
            else:
                short = total_price - total_paid
                print(f"Insufficient amount. Please instert \033[91m {short:.2f} \033[0m AED more.")

        except ValueError:
            print("\033[91m Invalid amount, please insert the specific amount. \033[0m")

# Dispense product after payment
def dispense(item):
    print(f"\n******************** \nDispensing \033[92m {item[1]}...\033[0m") # Dispensing the item
    print(f"Enjoy your \033[92m {item[1]}!\033[0m\n********************")

#Stocks update
def update_stock(category, code, quantity_ordered):
    if category == "Foods":
        item, price, quantity = foods[code]
        foods[code] = (item, price, quantity - quantity_ordered)
    elif category == "Drinks":
        item, price, quantity = drinks[code]
        drinks[code] = (item, price, quantity - quantity_ordered)

# Main
def machine():
    while True:
        item = display()  # Display the menu and get selected item

        if item:  # If a valid item was selected
            code, name, price, quantity = item  # Unpack the selected item
            print(f"\n******************** \nYou selected: \033[92m{name}\033[0m | price: {price:.2f} AED. \033[94m(Available: {quantity})\033[0m")

            while True:
                try:
                    quantity_ordered = int(input(f"How many {name} would you like to purchase? Enter amount: "))
                    if 0 < quantity_ordered <= quantity:
                        payment(price, quantity_ordered)  # Process payment
                        update_stock("Foods" if code in foods else "Drinks", code, quantity_ordered)  # Update stock
                        dispense(item)  # Dispense the item
                        break
                    else:
                        print("Invalid quantity, please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            more = input("\nWould you like to buy something else? (Yes or No): ").capitalize()
            if more != "Yes":
                print("Thank you for using the Vending Machine. Goodbye!")
                break
            
# Run the machine function
machine()
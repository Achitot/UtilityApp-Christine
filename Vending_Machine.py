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
                item, price, quantity = foods[code] # Retrieve item details
                print(f"\nYou have chosen {code}: {item} - {price:.2f} AED.") # Confirms user input
                break # Exit the loop
            else:
                print("\nInvalid code, please try again.")  # If invalid item code is entered, user will try again
           
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
                item, price, quantity = drinks[code] # Retrieve item details
                print(f"\nYou have chosen {code}: {item} - {price:.2f} AED.") # Confirms user input
                break # Exit the loop
            else:
                print("\nInvalid code, please try again.")  # If invalid item code is entered, user will try again

    else: 
        print("\nInvalid category. Please start again.")  # If the category is invalid

display()

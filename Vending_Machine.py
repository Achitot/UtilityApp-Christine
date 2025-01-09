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

def main_display():
    print("\nWelcome to the Machine!")
    print("Please select a category.")
    print("\nCategory:")
    category = input("Foods or Drinks: ").capitalize()
    if category == "Foods":
        print("\nMenu for Foods:")
        for code, (item, price, quantity) in foods.items():
            print(f"{code}: {item} - {price:.2f} AED. (Available: {quantity})")

        print("\nChoose your order in the given menu.")
        while True:
            code = input("Enter the item code: ").upper()
            if code in foods:
                item, price, quantity = foods[code]
                print(f"You have chosen {code}: {item} - {price:.2f} AED.")
                break
            else:
                print("\nInvalid code, please try again.")
           
                    
    elif category == "Drinks":
        print("\nMenu for Drinks:")
        for code, (item, price, quantity) in drinks.items():
            print(f"{code}: {item} - {price:.2f} AED (Available: {quantity})")

        print("\nChoose your order in the given menu.")
        while True:
            code = input("Enter the item code: ").upper()
            if code in drinks:
                item, price, quantity = drinks[code]
                print(f"You have chosen {code}: {item} - {price:.2f} AED.")
                break
            else:
                print("\nInvalid code, please try again.")
            
main_display()

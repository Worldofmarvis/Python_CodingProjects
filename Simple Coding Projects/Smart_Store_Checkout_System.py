def calculate_subtotal(price, quantity):
    total_price = price * quantity
    return total_price

def apply_discount(subtotal, is_member):
    if(is_member):
        total_amount = subtotal * 0.10
    elif(subtotal>100):
        total_amount = subtotal * 0.5
    else:
        total_amount = subtotal
    return total_amount

def generate_receipt(item_name, final_price):
    # TODO: Write your code here
    pass

# --- Main Progra
while(True):
    print("=== Welcome to the Smart Store ===")
    item_name = input("Enter item name: ")
    item_price = float(input("Enter price per item: "))

    is_member = input("Are you a store member? (yes/no): ").lower()
    if(is_member == "y"):
        apply_discount()
    else:
        generate_receipt()

    proceed_transaction = input("Would you like to process another transaction? (y/n): ").lower()
    if(proceed_transaction == "n"):
        False


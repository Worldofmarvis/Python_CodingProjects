def calculate_subtotal(price, quantity):
    total_price = price * quantity
    return total_price

def apply_discount(subtotal, is_member):
    discount_multiplier = 0.0
    
    if is_member:
        discount_multiplier += 0.10  
        
    if subtotal > 100.00:
        discount_multiplier += 0.05 
        
   
    final_price = subtotal * (1 - discount_multiplier)
    return final_price

def generate_receipt(item_name, final_price):
    print("--- RECEIPT ---")
    print(f"Item: {item_name}")
    print(f"Total Due: ${final_price:.2f}")
    print("-" * 15)


while True:
    print("=== Welcome to the Smart Store ===")
    item_name = input("Enter item name: ")
    item_price = float(input("Enter price per item: "))
    item_quantity = int(input("Enter quantity: "))

    
    subtotal = calculate_subtotal(item_price, item_quantity)

    
    membership_input = input("Are you a store member? (yes/no): ").lower()
    is_member = True if membership_input == "yes" else False
    print()

    
    final_price = apply_discount(subtotal, is_member)

  
    generate_receipt(item_name, final_price)
    print()

    proceed_transaction = input("Would you like to process another transaction? (y/n): ").lower()
    print()
    if proceed_transaction == "n":
        print("Thank you for shopping with us! Goodbye.")
        break

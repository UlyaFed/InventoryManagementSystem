import json

# Load inventory from the JSON file
def load_inventory():
    try:
        with open("inventory.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Inventory file not found, initializing new inventory.")
        return {}  # Return an empty dictionary if the file doesn't exist

# Save inventory to the JSON file
def save_inventory(inventory):
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

    
# Display inventory formatted   
def display_inventory():
    inventory = load_inventory()
    if not inventory:
        print("No products in inventory.")
        return
    
    print(f"{'Product Name':<20} {'Price per Unit':<15} {'Quantity':<10} {'Total Price':<15}") # :<20 tab steps/ colum width
    print("="*60)
    
    for product_name, product_details in inventory.items():
        total_price = round(product_details['total_price'], 2)  # round the total price to 2 decimal places
        print(f"{product_name:<20} {product_details['price_per_unit']:<15} "
              f"{product_details['quantity']:<10} {total_price:<15}")  
    print("="*60)   

# Initial inventory setup - if the file doesn't exist yet, one will be created
inventory = load_inventory()
if not inventory:
   inventory = {"laptop": {"item_name": "Laptop", "price_per_unit": 1000, "quantity": 1, "total_price": 1000}}
   save_inventory(inventory)  # Save initial inventory to JSON
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

def display_inventory():
    inventory = load_inventory()
    print(f"Updated version of inventory:\n {inventory}")

# Initial inventory setup - if the file doesn't exist yet, one will be created
inventory = load_inventory()
if not inventory:
   inventory = {"Laptop": {"item_name": "Laptop", "unit_price": 1000, "product_qty": 1,"total_price": 1000}}
   save_inventory(inventory)  # Save initial inventory to JSON
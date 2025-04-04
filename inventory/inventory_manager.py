from product import Product
from inventory_dict import load_inventory, save_inventory, display_inventory #Britta

class InventoryManager():
    """ InventoryManager class shows a program for the manager to maintain
    the inventory. 
    The inventory file is saved for every change in our permanent json file.
    Returns:
        _type_: method 'product_in_inventory' returns a product, after name is given
        _type_: method 'add_products' adds new products or changes quantity and price
        _type_: method 'remove_products' removes complete items and list them temporarily
        _type_: method 'update_inventory_quantity' increase or decrease a product's quantity
        _type_: method 'get_total_inventory_value' shows the total value of all items in stock
        _type_: method 'get_inventory_info' shows selcted key values and the inventory
    """
    removed_products = []  # Empty list to track removed products from inventory
    
    def __init__(self, ):
        #self.inventory = {} 
        self.deleted_items = 0 # created for counting deleted items
    
    
    def product_in_inventory(self, item_name):
        inventory = load_inventory()
        
        if item_name in inventory:# Check if the product exists in the inventory
            product = inventory[item_name]
            print(f"\nProduct details for {item_name}:")
            print(f"---------------------------------------")
            print(f"Name: {product['item_name']}")
            print(f"Price per unit: {product['price_per_unit']}")
            print(f"Quantity: {product['quantity']}")
            print(f"Total price: {product['total_price']}")
            print(f"---------------------------------------\n")
        else:
            print(f"Product '{item_name}' not found in the inventory\n.")
    
    
    def add_products(self, product): # get product info from product class
        inventory = load_inventory()

        if product["item_name"] in inventory: 
            print(f"Product {product["item_name"]} already exists in the inventory. Updating quantity.")
            new_quantity = inventory[product["item_name"]]["quantity"] + product["quantity"]
            for key, value in inventory.items():
                if key == product["item_name"]:
                    value["quantity"] = new_quantity
                    value["total_price"] = new_quantity * product["price_per_unit"]
            save_inventory(inventory)
        else:             
            inventory[product["item_name"]] = product # bring new product to self.inventory # Britta change
            save_inventory(inventory)

              
    def remove_products(self, item_name):
        inventory = load_inventory()
        if item_name in inventory:
            removed_item = inventory.pop(item_name)
            save_inventory(inventory)
            self.__class__.removed_products.append(removed_item)  # fill a list "removed products" with removed products
            self.deleted_items += 1
            return self.deleted_items
        else:
            print(f"Product {item_name} not found in the inventory.")
        

        
    def update_inventory_quantity(self,item_name, qty_to_change): 
        inventory = load_inventory()
        if item_name in inventory:
            new_quantity = inventory[item_name]["quantity"] + qty_to_change
            for key, value in inventory.items():
                if key == item_name:
                    value["quantity"] = new_quantity
                    value["total_price"] = new_quantity * value["price_per_unit"]
            save_inventory(inventory)    
            
        
    
    def get_total_inventory_value(self):
        inventory = load_inventory()
        total_value = sum(product["total_price"] for product in inventory.values())
        print(f"\nThe total inventory value is {total_value:,.2f} EUR\n")  
        return total_value # returning the total value
    
    
    def get_inventory_info(self):
        inventory = load_inventory()
        
        # get amount of products in inventory
        total_len = len(inventory)
        # Find the most expensive product by price per unit
        most_expensive_by_unit = max(inventory.items(), key=lambda x: x[1]["price_per_unit"])
        me_product = most_expensive_by_unit[0]
        # Find the most expensive product by total price
        most_expensive_by_total_price = max(inventory.items(), key=lambda x: x[1]["total_price"])
        highest_value_product = most_expensive_by_total_price[0]       
        
        print(f"\nActually, we have ** {total_len} ** different products in stock. ")
        print( )
        print(f"Most expensive item is: {me_product}")
        print( )
        print(f"Highest value per item in stock: {highest_value_product}\n\n")
        print()
        print(f"List of removed items:\n{self.deleted_items}\n\n")
        
        
        
        # Displaying the inventory in a readable and more beautiful format
        print("Overview inventory:\n")
        print( )
        display_inventory() # run Display inventory  from inventory.dict  
        print( )
        print( )
        
        
       

        

           

    

    
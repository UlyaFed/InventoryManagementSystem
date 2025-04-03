from product import Product

class InventoryManager():
    
    def __init__(self, ):
        self.inventory = {}
        self.deleted_items = 0 # created for counting deleted items
    
    def add_products(self, product):
        
        if product.item_name in self.inventory:
            print(f"Product {product.item_name} already exists in the inventory. Updating quantity.")
            self.inventory[product.item_name].update_quantity(product.quantity) # is it adding the new quantity
        else:
            self.inventory[product.item_name] = product
            print(f"Product {product.item_name} added to the inventory.")
            #print(self.inventory)
              
    def remove_products(self, item_name):
        if item_name in self.inventory:
            self.inventory.pop(item_name)
            self.deleted_items += 1 # incrementing the deleted items
            print(f"Product {item_name} removed from the inventory.")
        else:
            print(f"Product {item_name} not found in the inventory.")
        
    def update_inventory_quantity(self,item_name, qty_to_change): 
        if item_name in self.inventory:
            product = self.inventory[item_name]
            product.update_quantity(qty_to_change)
            print(f"Quantity of {item_name} updated to {product.quantity}.")
        else:
            print(f"Product {item_name} not found in the inventory.")
        
    
    def get_total_inventory_value(self):
        total_value = sum(product.total_price() for product in self.inventory.values())
        print(f"The total inventory value is {total_value:,.2f} EUR\n")  
        return total_value # returning the total value
    
    def get_inventory_info(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        # Displaying the inventory in a readable and more beautiful format
        #print("\nCurrent Inventory:")
        #print("-" * 50)
        for product in self.inventory.values():
            product_info = product.get_product_info()
            print(product_info)
            #print(f"Name: {product_info['item_name']}")
            #print(f"Price per unit: {product_info['price_per_unit']:.2f} EUR")
            #print(f"Quantity: {product_info['quantity']}")
            #print(f"Total Price: {product_info['total_price']:.2f} EUR")
            #print("-" * 50)
           

    
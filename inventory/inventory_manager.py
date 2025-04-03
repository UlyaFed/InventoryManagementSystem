from product import Product

class InventoryManager():
    
    def __init__(self, ):
        self.inventory = {}
    
    def add_products(self, product):
        
        if product.item_name in self.inventory:
            print(f"Product {product.item_name} already exists in the inventory. Updating quantity.")
            self.inventory[product.item_name].update_quantity(product.quantity) # is it adding the new quantity
        else:
            self.inventory[product.item_name] = product
            print(f"Product {product.item_name} added to the inventory.")
              
    def remove_products(self, item_name):
        if item_name in self.inventory:
            self.inventory.pop(item_name)
            print(f"Product {item_name} removed from the inventory.")
        else:
            print(f"Product {item_name} not found in the inventory.")
        
    def update_quantity(self,item_name, qty_to_change): 
        if item_name in self.inventory:
            product = self.inventory[item_name]
            product.update_quantity(qty_to_change)
            print(f"Quantity of {item_name} updated to {product.quantity}.")
        else:
            print(f"Product {item_name} not found in the inventory.")
        
    
    def get_total_inventory_value(self):
        total_value = sum(product.total_price() for product in self.inventory.values())
        print(f"The total inventory value is {total_value:,.2f} EUR\n")

    def get_inventory_info(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        for product in self.inventory.values():
            print(product.get_product_info())
           

    
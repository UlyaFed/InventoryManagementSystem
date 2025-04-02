from product import Product

class InventoryManager():
    
    def __init__(self, ):
        self.inventory = {}
    
    def add_products(self, product):
        
        if product.item_name in self.inventory:
            print(f"Product {product.item_name} already exists in the inventory. Updating quantity.")
            self.inventory[product.item_name].update_quantity(product.quantity)
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
        
if __name__ == "__main__":
    

    manager = InventoryManager()
    product1 = Product("Laptop", 1200, 1)
    product2= Product("Mouse", 25, 5)
    product3 = Product("Keyboard", 19.99, 3)
    manager.add_products(product1)
    manager.add_products(product2)
    manager.add_products(product3)
    manager.update_quantity("Mouse", 10)
    manager.get_inventory_info()
    manager.remove_products("Mouse")
    manager.get_total_inventory_value()
    
    
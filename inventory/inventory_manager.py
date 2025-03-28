from product import Product


class InventoryManager:
        def __init__(self):
            self.inventory = {}
            
        def add_product(self,item_name, price_per_unit, quantity):
            if item_name in self.inventory:
                self.inventory[item_name].update_quantity(quantity)
            else:
                self.inventory[item_name] = Product(item_name, price_per_unit, quantity)
                
        
manager = InventoryManager()
manager.add_product("Laptop", 1200, 1)
manager.add_product("Laptop", 3600, 3)
print(manager.inventory["Laptop"].get_product_info())  


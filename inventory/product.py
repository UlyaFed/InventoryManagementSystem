class Product:
    
    def __init__(self, item_name, price_per_unit, quantity):
        self.item_name = item_name
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        self.total_price = self.price_per_unit * self.quantity
        
    def update_quantity(self, additional_quantity):
        self.quantity += additional_quantity
        self.total_price = self.price_per_unit * self.quantity


    def get_product_info(self):
        return f"Product - {self.item_name}, costs {self.total_price} euro for {self.quantity} units"


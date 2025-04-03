class Product:
    
    def __init__(self, item_name, price_per_unit:float, quantity:int):
        self.item_name = item_name
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        
    def update_quantity(self, new_quantity):
        self.quantity += new_quantity
        
    def total_price(self):
        return (self.price_per_unit or 0) * (self.quantity or 0) # 0 is used to avoid NoneType errors

    def get_product_info(self):
        return {
            "item_name": self.item_name,
            "price_per_unit": self.price_per_unit,
            "quantity": self.quantity,
            "total_price": self.total_price()
        }
        
    def __str__(self):
        return f"Product - {self.item_name}, costs {self.total_price()} euro for {self.quantity} units"
from product import Product
from inventory_manager import InventoryManager


def main():
    
    manager = InventoryManager()
    product1 = Product("Laptop", 1200, 1)
    product2= Product("Mouse", 25, 5)
    product3 = Product("Keyboard", 19.99, 3)
    product4 = Product("Laptop", 1200, 2)
    manager.add_products(product1)
    manager.add_products(product2)
    manager.add_products(product3)
    manager.update_quantity("Mouse", -2)
    manager.get_inventory_info()
    manager.remove_products("Mouse")
    manager.get_total_inventory_value()
    manager.add_products(product4)
    manager.get_inventory_info()
    print(manager.inventory)


if __name__ == "__main__":
    main()





from product import Product
from inventory_manager import InventoryManager

print( )
print("*"*50)
print(" Welcome to Inventory Manager tool")
print("*"*50)
print( )
print( )

def options_menu():
   
    print("*"*50)
    print( )
    print("You have the following options\n")
    print("1. Add a product to the inventory")
    print("2. Remove an product from inventory")
    print("3. Change quantity of a product ") 
    print("4. Overview of inventory") 
    print("5. View total value of inventory")
    print("6. Inventory Manager report")
    print("7. Exit 'Inventory Manager' program") 
    print( )
    print("*"*50)


#def run_program ():

def main():
    manager = InventoryManager()
    product = Product("Keyboard", 25.99, 8)

  

    while True: 
        options_menu()

        print("Choose an option: ")
        option = input("Enter your option: ")
        
        #CLS
        
        
            
        if option == "1": 
            print("\nAdd a product to the inventory\n")
            item_name = input("Enter the product name: ")
            product_price = float(input("Enter the product price per unit: "))
            product_quantity = int(input("Enter the product quantity: "))
            
            #we are creating a new product object, not overwriting it like was before.
            new_product = Product(item_name, product_price, product_quantity)
            manager.add_products(new_product)
            print(new_product.get_product_info())
            #product.item_name = item_name # change class attribute
            #product.price_per_unit = product_price # change class attribute 
            #product.quantity = product_quantity # change class attribute
            #manager.add_products(product)
            #print(product.get_product_info())
            
        elif option == "2":
            print("\nRemove a product from inventory\n")
            product_to_remove = input("Enter the product to remove: ")
            manager.remove_products(product_to_remove) # 
            
        elif option == "3": 
            item_name = input("Enter the product name: ")
            qty_to_change = int(input("Enter the quantity to change (use negative for reduction): ")) # for an easier understanding of how to reduce the quantity
            manager.update_inventory_quantity(item_name, qty_to_change)
            
        elif option == "4":
            manager.get_inventory_info()
            
        elif option == "5":
            manager.get_total_inventory_value()
            

        elif option == "6":
            print("\nInventory Manager Report\n")
            print("----------------------------")
            total_items = len(manager.inventory)
            #deleted_items = 0 # gelöschte Artikel weren nicht mehr aufgelistet
            total_value = sum(product.total_price() for product in manager.inventory.values())
            print(f"Total items in inventory: {total_items}")
            print(f"Total deleted items: {manager.deleted_items}") # using the deleted items counter from the inventory manager 
            print(f"Total inventory value: {total_value:.2f} EUR")
            print("----------------------------") 
            
        elif option == "7":
            print("see ya!")
            break
        else:
            print("Invalid choice, try again")
               
        
              
            
        

            
           
        

if __name__ == "__main__":
    main()








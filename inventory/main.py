from product import Product
from inventory_manager import InventoryManager
from inventory_dict import load_inventory, save_inventory, display_inventory 

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
    print("1. Get product info from inventory") 
    print("2. Add a product to the inventory")
    print("3. Remove an product from inventory")
    print("4. Change quantity of a product ") 
    print("5. Overview of inventory") 
    print("6. View total value of inventory")
    print("7. Inventory Manager report")
    print("8. Exit 'Inventory Manager' program") 
    print( )
    print("*"*50)


#def run_program ():

def main():
    manager = InventoryManager()
    product = Product("Keyboard", 25.99, 8)

  

    while True: 
        options_menu()

        print("Choose an option: ")
        option = (input("Enter your option: ")).strip()
        
        
        if option == "1":
            item_name = input("Enter the product name for inventory info: ")
            manager.product_in_inventory(item_name)
        
            
        elif option == "2": 
            print("\nAdd a product to the inventory\n")
            item_name = input("Enter the product name: ").strip().lower()
            product_price = float(input("Enter the product price per unit: "))
            product_quantity = int(input("Enter the product quantity: "))
            #we are creating a new product object, not overwriting it like was before.
            new_product = Product(item_name, product_price, product_quantity)
            product = new_product.get_product_info() 
            manager.add_products(product) 

            
        elif option == "3":
            print("\nRemove a product from inventory\n")
            product_to_remove = input("Enter the product to remove: ").strip().lower()
            manager.remove_products(product_to_remove) 
            print("\nList of {self.deleted_items} removed items:")  # Britta how we get the attribute?
            print(manager.removed_products) 
            
            
        elif option == "4": 
            item_name = input("Enter the product name: ").strip().lower()
            qty_to_change = int(input("Enter the quantity to change (use negative for reduction): ")) # for an easier understanding of how to reduce the quantity
            manager.update_inventory_quantity(item_name, qty_to_change)
            
            
        elif option == "5":
            manager.get_inventory_info()
            
            
        elif option == "6":
            manager.get_total_inventory_value()
            

        elif option == "7":
            print("\nInventory Manager Report\n")
            print("----------------------------")  
            manager.get_inventory_info()
            manager.get_total_inventory_value()
            
            
        elif option == "8":
            print()
            print("see ya!\n\n")
            break
        
        else:
            print("Invalid choice, try again")
            

if __name__ == "__main__":
    main()

               
        
              
            
        






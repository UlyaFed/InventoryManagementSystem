from product import Product
from inventory_manager import InventoryManager

def greeting():
    
    print("*"*50)
    print(" Welcome to Inventory Manager tool")
    print("*"*50)
    print( )
    print( )
    print( )

    
    print("You have the following options\n")
    print("1: Overview of inventory") 
    print("2: Add a product to the inventory")
    print("3: Remove an product from inventory")
    print("4: Change quantity of a product ") 
    print("5: View total value of inventory")
    print("6: Inventory Manager report")
    print("7: Exit 'Inventory Manager' program") #
    print( )
    print("*"*50)


#def run_program ():

def main():
    manager = InventoryManager()
    #product = Product(), #item_name, price_per_unit, quantity
    



    while True: 
        greeting()

        print("Choose an option: ")
        option = input("Enter your option: ")
        
        #CLS
        
        if option == "1":
            manager.get_inventory_info()
        elif option == "2":
            product_name = input("Enter the product name: ")
            product_price = float(input("Enter the product price per unit: "))
            product_quantity = int(input("Enter the product quantity: "))
            manager.add_products(product_name)
        elif option == "3":
            # elif option == "4":    
            # elif option == "5":   
            # elif option == "6":   
            # elif option == "7":
        
        else:
            print("Invalid choice, try again")
            
           
            




if __name__ == "__main__":
    main()





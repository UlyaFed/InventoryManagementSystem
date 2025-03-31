import json

# import sys
# import os

# # get absolute folderpath from folder above 
# folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "/home/dci-student/Dokumente/DCI/Python/excercises/projects/InventoryManagementSystem/"))
# sys.path.append(folder_path)

# from main import inventory

inventory = {"Laptop":{"product_name":"Laptop", "unit_price": 1000, "product_qty": 1 }}

inventory_json = json.dumps(inventory)
print(inventory_json)


print(inventory)

class Manager:
    manager_1 = "Alex"
    manager_2 = "Britta"
    manager_3 = "Uliana"
    
class UserRights:
    full_access = "admin"
    test_access = "tester"
    read_access = "user"

class InventoryManager(Manager, UserRights):
    global inventory
    removed_products = [] # empty list to track removed products from inventory
    
    def __init__(self, m_name, user_rights:str):
        self.m_name = m_name
        self.user_rights = user_rights
        self.product = {"product_name":"Laptop", "unit_price": 1000, "product_qty": 1 }
        
    def authorize_manager(self):
        name = input("Enter your username: ").strip().title()
        rights = input("Enter your user-rights: ").strip().lower()

        # check if name is in Manager_names and if rights are in UserRights
        if name in [Manager.manager_1, Manager.manager_2, Manager.manager_3] and rights in [UserRights.full_access, UserRights.test_access, UserRights.read_access]:
            if rights == UserRights.full_access:
                print("You are authorized to maintain the inventory")
                self.m_name = name
                self.user_rights = rights
            elif rights == UserRights.test_access:       
                print("You are authorized to test the inventory")
                self.m_name = name
                self.user_rights = rights
            elif rights == UserRights.read_access:       
                print("You are authorized to read the inventory")
                self.m_name = name
                self.user_rights = rights
            else: 
                print("Authorization failed, you are missing rights")
        else:
            print("Authorization failed, invalid username or rights")
        
        return 
    
    
    def add_products(self):
        print("\n##############################")
        print(f" ADD PRODUCT ")
        print("##############################\n")
        
        product_name = input("\nEnter the new product_name to add: ").strip().title()
        check_product_in_inventory = inventory.get(product_name, None)
        
        if check_product_in_inventory == None:
            print("Your product is new. Enter further product details.")
            unit_price = float(input("Unit_price: "))
            product_qty = int(input("Product quantity: "))
            self.product.update({"product_name": product_name, "unit_price": unit_price, "product_qty": product_qty})
            inventory.update({product_name : self.product})
            print(inventory)
        else: 
            print(f"The product {product_name} already exists, choose another product to add.")

      
    def remove_products(self):
        
        print("\n##############################")
        print(f" REMOVE PRODUCT ")
        print("##############################\n")
        
        product_to_remove = input("Enter product name to remove: ").strip().title()
        
        if inventory.get(product_to_remove): # checks if product to remove is in inventory
            confirmation = input(f"Confirm with 'Y' to remove the product {product_to_remove}: ").strip().upper()
            if confirmation == 'Y':  # Double check, if products should be deleted from inventory
                removed_item  = inventory.pop(product_to_remove) # deletes the inventory item with name "product_to_remove"                
                self.__class__.removed_products.append(removed_item) # fill a class list with removed products
                print(f"{product_to_remove} has been removed from the inventory.")
                print(f"List of removed items: {self.__class__.removed_products}")
            else: 
                return f"No item in the inventory will be deleted."   
        else:
            print(f"{product_to_remove} is not in the inventory.")
        
        
    def update_quantity(self):
        
        print("\n##############################")
        print(f" CHANGE PRODUCT QTY ")
        print("##############################\n")
          
        product_name = input("Enter the product to change: ").strip().title()
        qty_to_change = int(input("Enter a positive or negative value for change in quantity: "))
        check_product_in_inventory = inventory.get(product_name, None)
        
        if check_product_in_inventory != None:
            for product, product_details in inventory.items():
                if product == product_name:
                    x = product_details.get("product_qty") + qty_to_change
                    product_details["product_qty"] = x
        else:
            print("The product is not in the inventory.")       
 
    
    def get_total_inventory_value(self):
        
        print("\n##############################")
        print(f" INVENTORY TOTAL VALUE ")
        print("##############################\n")
        
        total_inventory_value = 0 # initializing the variable
        # looping over inventory products to sum the total price (unit_price * product_qty)
        total_inventory_value = sum([product["unit_price"] * product["product_qty"] for product in inventory.values()])
        print(f"The total inventory value is {total_inventory_value:,.2f} EUR.")

        
if __name__ == "__main__":
    InvM1 = InventoryManager("Britta", "admin")
    InvM1.authorize_manager()
    InvM1.add_products()
    InvM1.remove_products()
    InvM1.update_quantity()
    InvM1.get_total_inventory_value()
    print(f"Inventory status: {inventory}")

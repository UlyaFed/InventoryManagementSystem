class Manager:
    manager_1 = "Alex"
    manager_2 = "Britta"
    manager_3 = "Uliana"
    
class UserRights:
    full_access = "admin"
    test_access = "tester"
    read_access = "user"

class InventoryManager(Manager, UserRights):
    
    def __init__(self, m_name, user_rights:str):
        self.m_name = m_name
        self.user_rights = user_rights
        self.inventory = {"product_name":"Laptop", "price_": 1000, "product_qty": 1 }
        
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
        product_name = input("Enter the product_name: ").strip().title()
        
        if product_name not in self.inventory:
            self.inventory.append(product_name)
        else: 
            print("This product already exists, choose another name, if it is different.")
    
    
    def remove_products(self):
        product_to_remove = input("Enter product name to remove: ").strip().title()
        
        if product_to_remove in self.inventory:  # Check if the product exists first
            while True:  # Infinite loop until the user confirms or cancels
                confirmation = input(f"Confirm with 'Y' to remove the product {product_to_remove}: ").strip().upper()
                if confirmation == 'Y':  # If the user confirms
                    self.inventory.pop(product_to_remove)
                    print(f"{product_to_remove} has been removed from the inventory.")
                    break
                else:
                    print(f"Removal of {product_to_remove} cancelled.")
                    break
        else:
            print(f"{product_to_remove} is not in the inventory.")
        
    def update_quantity(self):
        if product_qty.
        
        
        
        
        
        


InvM1 = InventoryManager("Britta", "admin")
InvM1.authorize_manager()
        
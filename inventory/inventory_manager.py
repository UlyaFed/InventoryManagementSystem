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
        self.products = [{}]
        
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
    
    def add_products (self):


InvM1 = InventoryManager("Britta", "admin")
InvM1.authorize_manager()
        
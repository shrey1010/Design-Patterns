class MainCode:
    def api(self):
        print("API is giving Response,")
        
        
class Authentication:
    def __init__(self):
        self.main_code = MainCode()
        
    def authenticate(self,password):
        if password == "Shrey":
            self.main_code.api()
        else:
            print("Access Denied.")
            
auth = Authentication()
auth.authenticate("Shrey")
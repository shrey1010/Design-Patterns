class Burger:
    def __init__(self):
        self.bun = False
        self.patty = False
        self.cheese = False
        self.chicken = False
        self.onion = False
        self.mayo = False
        self.tomato = False
        
    def show(self):
        print("Your Burger Contains-")
        if self.bun:
            print("-Bun")
        if self.patty:
            print("-Patty")
        if self.cheese:
            print("-Cheese")
        if self.chicken:
            print("-Chicken")
        if self.onion:
            print("-Onion")
        if self.mayo:
            print("-Mayo")
        if self.tomato:
            print("-Tomato")
            
class BurgerBuilder(Burger):
    def add_bun(self):
        self.bun = True 
        return self
    def add_patty(self):
        self.patty = True 
        return self
    def add_cheese(self):
        self.cheese = True 
        return self
    def add_chicken(self):
        self.chicken = True 
        return self
    def add_onion(self):
        self.onion = True 
        return self
    def add_mayo(self):
        self.mayo = True 
        return self
    def add_tomato(self):
        self.tomato = True 
        return self
        
    def build(self):
        return self
        
builder = BurgerBuilder()
burger = (
    builder
    .add_bun()
    .add_patty()
    .add_tomato()
    .add_onion()
    .add_mayo()
    .build()
    )
    
burger.show()
            
        
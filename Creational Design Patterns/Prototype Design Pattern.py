from copy import deepcopy

class Robot:
    def __init__(self,name,color,features):
        self.name = name
        self.color = color 
        self.features = features
        
    def get_clone(self):
        return deepcopy(self)
    
    def show(self):
        print("Robot Attributes:")
        print(f"-{self.name}")
        print(f"-{self.color}")
        print(f"-{self.features}")

robo1 = Robot("shrey","Blue",["Hands","Legs","face"])
robo2 = robo1.get_clone()
robo2.color = "Red"
robo2.show()
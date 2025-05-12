from abc import ABC , abstractmethod


class RegularVanillaIcecream:
    def eat(self):
        print("Eating Vanilla Icecream")
        
        
class RegularChocolateIcecream:
    def eat(self):
        print("Eating Chocolate Icecream")
        
class VeganVanillaIcecream:
    def eat(self):
        print("Eating Vanilla Icecream")
        
        
class VeganChocolateIcecream:
    def eat(self):
        print("Eating Chocolate Icecream")        

class IcecreamFactory(ABC):
    @abstractmethod
    def get_chocolate_icecream(self):
        raise NotImplementedError
    @abstractmethod
    def get_vanilla_icecream(self):
        raise NotImplementedError
        
class VeganIcecreamFactory(IcecreamFactory):

    def get_chocolate_icecream(self):
        return VeganChocolateIcecream().eat()
    def get_vanilla_icecream(self):
        return VeganVanillaIcecream().eat()

class RegularIcecreamFactory(IcecreamFactory):

    def get_chocolate_icecream(self):
        return RegularChocolateIcecream().eat()
    def get_vanilla_icecream(self):
        return RegularVanillaIcecream().eat()           
            
get_regular_factory = RegularIcecreamFactory()
get_vegan_factory = VeganIcecreamFactory()

get_regular_factory.get_vanilla_icecream()
get_vegan_factory.get_chocolate_icecream()
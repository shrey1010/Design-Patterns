
class VanillaIceCream:
    def eat(self):
        print("You are eating Vanilla Ice Cream!")

class ChocolateIceCream:
    def eat(self):
        print("You are eating Chocolate Ice Cream!")

class StrawberryIceCream:
    def eat(self):
        print("You are eating Strawberry Ice Cream!")


class IceCreamFactory:
    def get_ice_cream(self, flavor):
        if flavor == "vanilla":
            return VanillaIceCream()
        elif flavor == "chocolate":
            return ChocolateIceCream()
        elif flavor == "strawberry":
            return StrawberryIceCream()
        else:
            print("Sorry, we don't have that flavor.")
            return None


factory = IceCreamFactory()

ice_cream1 = factory.get_ice_cream("chocolate")
ice_cream1.eat()

ice_cream2 = factory.get_ice_cream("vanilla")
ice_cream2.eat()

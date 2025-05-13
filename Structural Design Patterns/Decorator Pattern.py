class Coffee:
    def cost(self):
        return 50

    def description(self):
        return "Plain Coffee"


class CoffeeDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

    def description(self):
        return self.coffee.description()

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 10

    def description(self):
        return self.coffee.description() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 5

    def description(self):
        return self.coffee.description() + ", Sugar"


# Step 1: Start with plain coffee
my_coffee = Coffee()
my_coffee = MilkDecorator(my_coffee)
my_coffee = SugarDecorator(my_coffee)


print("Description:", my_coffee.description())
print("Total Cost:", my_coffee.cost())

class MealPreparation:
    def prepare_meal(self):
        self.boil_water()
        self.add_main_ingredient()
        self.add_flavoring()
        self.cook()

    def boil_water(self):
        print("Boiling water...")

    def add_main_ingredient(self):
        pass  # To be overridden

    def add_flavoring(self):
        pass  # To be overridden

    def cook(self):
        print("Cooking for 5 minutes...")


class Noodles(MealPreparation):
    def add_main_ingredient(self):
        print("Adding noodles.")

    def add_flavoring(self):
        print("Adding spicy masala.")

class Pasta(MealPreparation):
    def add_main_ingredient(self):
        print("Adding pasta.")

    def add_flavoring(self):
        print("Adding Italian herbs.")


print("Making noodles:")
noodle_meal = Noodles()
noodle_meal.prepare_meal()

print("\nMaking pasta:")
pasta_meal = Pasta()
pasta_meal.prepare_meal()

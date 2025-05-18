class TreeType:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self, x, y):
        print(f"Drawing {self.name} tree at ({x}, {y}) with color {self.color}")


class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color):
        key = (name, color)
        if key not in cls._tree_types:
            print(f"Creating new TreeType: {name}, {color}")
            cls._tree_types[key] = TreeType(name, color)
        return cls._tree_types[key]


class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.display(self.x, self.y)


class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color):
        tree_type = TreeFactory.get_tree_type(name, color)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw_forest(self):
        for tree in self.trees:
            tree.draw()


forest = Forest()

# Plant many trees — some share the same type
forest.plant_tree(1, 2, "Oak", "Green")
forest.plant_tree(3, 4, "Pine", "Dark Green")
forest.plant_tree(5, 6, "Oak", "Green")
forest.plant_tree(7, 8, "Oak", "Green")

# Draw all trees
forest.draw_forest()

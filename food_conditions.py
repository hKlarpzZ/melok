class Food:

    def __init__(self, name, ingredients, preparation, portions, img) -> None:
        if name is None:
            raise KeyError
        if ingredients is None:
            raise KeyError
        if preparation is None:
            raise KeyError
        if portions is None:
            self.portions = 1
        if img is None:
            self.img = ''
        self.name = name
        self.ingredients = ingredients
        self.preparation = preparation
# Added Shoes to the Invertory
class Buyable:
    def __init__(self, price, name, category):
        self.price = price
        self.name = name
        self.category = category


class ClothesForSale(Buyable):
    def __init__(self, price, name, size):
        super().__init__(price, name, "Clothing")
        self.size = size


class FoodForSale(Buyable):
    def __init__(self, price, name, weight):
        super().__init__(price, name, "Food")
        self.weight = weight


class GamesForSale(Buyable):
    def __init__(self, price, name, numPlayers, genre):
        super().__init__(price, name, "Clothing")
        self.numPlayers = numPlayers
        self.genre = genre

class ShoesForSale(Buyable):
    def __init__(self, price, name, size, brand, colour):
        super().__init__(price, name, "Shoes")
        self.size = size
        self.brand = brand
        self.colour = colour




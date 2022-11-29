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


class PerishableFoodForSale(Buyable):
    def __init__(self, price, name, weight, date):   # Date - Expiration Date of Food Item
        super().__init__(price, name, "Food")
        self.weight = weight
        self.date = date


class NonPerishableFoodForSale(Buyable):
    def __init__(self, price, name, weight):
        super().__init__(price, name, "Food")
        self.weight = weight


class ComputerGamesForSale:
    def __init__(self, price, name, specs):
        super().__init__(price, name, "Food")
        self.weight = weight

class ComputerGameSpecs(ComputerGamesForSale):
    def __init__(self, OS, Processor, Memory, GPU, DirectXVerision, NetworkStrength, DiskStorageSpace):
        super(Buyable, self).__init__(price, name, specs)
        self.OS = OS
        self.Proccesor = Processor
        self.Memory = Memory
        self.DirectXVerision = DirectXVerision
        self.NetworkStrength = NetworkStrength
        self. DiskStorageSpace = DiskStorageSpace


class BoardGamesForSale(Buyable):
    def __init__(self, price, name, NumberOfRequiredPlayersToPlay, genre):
        super().__init__(price, name, "Clothing")
        self.NumberOfRequiredPlayersToPlay = NumberOfRequiredPlayersToPlay
        self.genre = genre

class ShoesForSale(Buyable):
    def __init__(self, price, size, brand, colour):  # 4 parimeters - Price, Name, Brand, Colour
        super().__init__(price, name, "Shoes")
        self.size = size
        self.brand = brand
        self.colour = colour




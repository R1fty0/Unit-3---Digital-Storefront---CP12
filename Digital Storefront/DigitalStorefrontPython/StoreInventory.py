from Buyable import Buyable, ClothesForSale, FoodForSale, GamesForSale

# Add Shoes to Systems

class StoreInventory:

    def __init__(self):
        self.ClothingInventory = []
        self.FoodInventory = []
        self.GameInventory = []
        self.ShoesInventory = []
        self.initializeInventoryLists()

    def ReturnSuppyStatusOfFullInventory(self):
        return self.ClothingInventory + self.FoodInventory + self.GameInventory

    def RemoveItemFromInventory(self, item):
        if type(item) is ClothesForSale:
            self.ClothingInventory.remove(item)
        elif type(item) is FoodForSale:
            self.FoodInventory.remove(item)
        elif type(item) is GamesForSale:
            self.GameInventory.remove(item)

    def AddItemToInventory(self, item):
        if type(item) is ClothesForSale:
            self.ClothingInventory.append(item)
        elif type(item) is FoodForSale:
            self.FoodInventory.append(item)
        elif type(item) is GamesForSale:
            self.GameInventory.append(item)

    def AddMultipleItemsToInventory(self, item, num):
        if type(item) is ClothesForSale:
            for x in range(num):
                self.ClothingInventory.append(item)
        elif type(item) is FoodForSale:
            for x in range(num):
                self.FoodInventory.append(item)
        elif type(item) is GamesForSale:
            for x in range(num):
                self.GameInventory.append(item)

    def initializeInventoryLists(self):
        # Populate initial clothes list
        # Hoodies
        smallHoodie = ClothesForSale(59.99, 'Hoodie', 'small')
        self.ClothingInventory.append(smallHoodie)  # You can add this way, but it is more efficient to do as below ...
        self.ClothingInventory.append(ClothesForSale(59.99, 'Hoodie', 'medium'))
        self.ClothingInventory.append(ClothesForSale(59.99, 'Hoodie', 'large'))

        # Shoes
        self.ClothingInventory.append(ClothesForSale(99.99, 'Dress Shoes', '8'))
        self.ClothingInventory.append(ClothesForSale(9.99, 'Sandals', '5'))

        # Gloves
        gloves = ClothesForSale(13.49, 'Gloves', 'Medium')
        self.AddMultipleItemsToInventory(gloves, 3)


        # Populate initial food list
        # Perishable Food Items
        self.FoodInventory.append(FoodForSale(12.99, 'Pizza', 400))
        self.FoodInventory.append(FoodForSale(24.00, 'Lasagna', 1000))
        self.FoodInventory.append(FoodForSale(3.99, 'Spinach', 250))

        # Non-perishables
        self.FoodInventory.append(FoodForSale(1.49, 'Beans', 300))
        self.FoodInventory.append(FoodForSale(0.99, 'Noodles', 125))
        rice = FoodForSale(7.99, 'Rice', 2000)
        self.AddMultipleItemsToInventory(rice, 5)

        # Populate initial games list
        # Board Games
        self.GameInventory.append(GamesForSale(19.99, 'Monopoly', 4, 'Board Game'))
        self.GameInventory.append(GamesForSale(24.99, 'Scrabble', 2, 'Board Game'))

        # Computer Games
        self.GameInventory.append(GamesForSale(79.99, 'Breath of the Wild', 2, 'Video Game'))
        self.GameInventory.append(GamesForSale(59.99, 'Forza', 2, 'Video Game'))
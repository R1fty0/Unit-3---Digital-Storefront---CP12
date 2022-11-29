from Buyable import Buyable, ClothesForSale, PerishableFoodForSale, NonPerishableFoodForSale, ComputerGamesForSale, BoardGamesForSale, ShoesForSale


# Add Shoes to Systems
class StoreInventory:
    def __init__(self):
        self.ClothingInventory = []
        self.PerisableFoodInventory = []
        self.NonPerisableFoodInventory = []
        self.ComputerGamesInventory = []
        self.BoardGames = []
        self.ShoesInventory = []
        # self.AddItemsToInventoryLists()

        def ReturnTypesOfItemsInInventory():
            print("Need to Add Code Here")
            #  return self.ClothingInventory + self.FoodInventory + self.GameInventory

        def AddItemToInventory(self, item):
            if type(item) is ClothesForSale:
                self.ClothingInventory.append(item)
            elif type(item) is PerishableFoodForSale:
                self.PerisableFoodInventory.append(item)
            elif type(item) is NonPerishableFoodForSale:
                self.NonPerisableFoodInventory.append(item)
            elif type(item) is ComputerGamesForSale:
                self.ComputerGamesInventory.append(item)
            # elif type(item) is BoardGamesForSale:
               # self.GameInventory.append(item)
            # elif type(item) is ShoesForSale:
                #self.ShoesInventory.append(item)

        # def InitalizeOriginalItemsInInventory(self):





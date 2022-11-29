# Store Data Imports
from StoreInventory import StoreInventory
from UserFinances import UserBankAccount
from Buyable import Buyable, BoardGamesForSale, FoodForSale, ClothesForSale

# UI Imports
from UIText import BasicUI
from UIText import StartProgramDialogue
from UIText import MainMenuDialogue


# Initialize inventories
Inventory = StoreInventory()
myStuff = list()
myShoppingCart = list()

# Placeholder bank account
myBankAccount = UserBankAccount(1, 'placeholder')

# FUNCTIONS TO MANAGE MENUING SYSTEM IN MAIN SHOPPING PROGRAM

# I have switched the naming scheme of the project to Pastel Casing - easier to read in my opinion.

def ViewCatalog():
    print('Here is a list of all of the items currently for sale!')
    Item: Buyable
    for Item in Inventory.ReturnSuppyStatusOfFullInventory():
        print(Item.name)


def BuyItem():
    DesiredItem = input('Please type in the name of the Item you wish to buy!')

    # Holding variable for the desired Item, if found
    ItemUserWantsToBuy = None

    # Look through the full inventory to see if the Item is present
    # Convert both Item name and user input to lower case to prevent case issues!
    for Item in Inventory.ReturnSuppyStatusOfFullInventory():
        if Item.name.lower() == DesiredItem.lower():
            ItemUserWantsToBuy = Item
            break  # end loop early if a suitable Item is found

    # If a suitable Item was found, give the User the option to buy it!
    if ItemUserWantsToBuy is not None:
        print(f'We have {ItemUserWantsToBuy.name} in stock!')
        UserChoice = int(input('Type 1 to BUY NOW, 2 to place in your shopping cart, or any other key to cancel purchase.'))

        if UserChoice == 1:
            makePurchaseFromStore(ItemUserWantsToBuy)
        elif UserChoice == 2:
            print('We will hold onto this Item for you. Adding to shopping cart ... ')
            moveItemToShoppingCart(ItemUserWantsToBuy)
        else:
            print('Purchase cancelled! Sending you back to the storefront ... ')
    else:  # If user-entered Item is not found in the store inventory
        print('The Item you are looking for is sold out or does not exist. Sorry!')


def ReviewMyInventory():
    print('Here is a list of the items you now own: ')
    for item in myStuff:
        print(item.name)


def ReviewUserFinances():
    myBankAccount.balanceReport()


def ReviewMyShoppingCart():
    if len(myShoppingCart) > 0:
        print('Here are all of the items being held in your shopping cart: ')
        for item in myShoppingCart:
            print(item.name)

        # Check to see if the user wants to purchase anything currently in their shopping cart
        userChoice = int(input('Would you like to purchase any held items now? 1 for YES or any other key for NO'))

        if userChoice == 1:
            buyItemInShoppingCart()
        else:
            print('Leaving shopping cart as is and returning to the storefront ... ')

    else:  # If cart is empty
        print('Your shopping cart is empty! Nothing to see here ... ')


def buyItemInShoppingCart():
    userChoice = input('Type in the name of the item you want to buy from the shopping cart: ')

    # Compare user requested name with cart entry names and offer a purchasing offer if there is a match
    itemInCart: Buyable
    for itemInCart in myShoppingCart:
        if itemInCart.name.lower() == userChoice.lower():
            makePurchaseFromShoppingCart(itemInCart)
        else:
            print('Item could not be found in shopping cart ... ')


def removeItemFromShoppingCart(item):
    UserChoice = input('Which item would you like to remove from your shopping cart?')

    # Compare user requested name with cart entry names and remove item if found
    ItemInCart: Buyable
    for ItemInCart in myShoppingCart:
        if ItemInCart.name.lower() == UserChoice.lower():
            print(f'You have removed {ItemInCart.name} from your shopping cart!')
            moveItemFromShoppingCartToInventory(ItemInCart)
        else:
            print('We could not find the item you are looking for in your shopping cart. Nothing was removed.')


def moveItemToShoppingCart(item):
    myShoppingCart.append(item)
    Inventory.RemoveItemFromInventory(item)


def moveItemFromShoppingCartToInventory(item):
    Inventory.AddItemToInventory(item)
    myShoppingCart.remove(item)


def makePurchaseFromStore(item):
    # If you can afford the item, buy it and remove it from the store
    if myBankAccount.CanUserAffordItem(item.price):
        myBankAccount.makePurchase(item.price)
        print(f'Purchase complete! You now own {item.name}')
        myStuff.append(item)
        Inventory.RemoveItemFromInventory(item)
    else:
        print('You can\'t afford this item ... ')


def makePurchaseFromShoppingCart(item):
    # If you can afford the item, buy it and remove it from the store
    if myBankAccount.CanUserAffordItem(item.price):
        myBankAccount.makePurchase(item.price)
        print(f'Purchase complete! You now own {item.name}')
        myStuff.append(item)
        myShoppingCart.remove(item)
    else:
        print('You can\'t afford that item ... ')


def MainMenu():
    while True:
        print(BasicUI.Border)
        
        for MenuText in MainMenuDialogue.Dialogue:
            print(MenuText)

        UserChoice = int(input(MainMenuDialogue.MenuPrompt))

        VerifyMenuMenuChoice(UserChoice)  # Verifies the User's Choice


def VerifyMenuMenuChoice(UserChoice):
    if UserChoice == 1:
        ViewCatalog()
    elif UserChoice == 2:
        BuyItem()
    elif UserChoice == 3:
        ReviewMyShoppingCart()
    elif UserChoice == 4:
        ReviewMyInventory()
    elif UserChoice == 5:
        ReviewUserFinances()
    elif UserChoice == 6:
        print("YOUR CONTENT HERE!")
    elif UserChoice == 7:
        print('Thanks for shopping! Now exiting program ... ')
         # break
    else:
        print('Incorrect input! Please select an option again.')

def StartProgram():
    for Text in StartProgramDialogue.Dialogue:
        print(Text)

    UserDeposit = input(StartProgramDialogue.DepositPrompt)   # Asks the User how much money they would like to deposit in their account
    print(BasicUI.Border)

    global myBankAccount
    myBankAccount = UserBankAccount(UserDeposit)
    StillShopping = True
    MainMenu()


# Starts Program
StartProgram()




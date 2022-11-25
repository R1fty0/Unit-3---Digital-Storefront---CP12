from StoreInventory import StoreInventory
from UserFinances import UserBankAccount
from Buyable import Buyable, GamesForSale, FoodForSale, ClothesForSale

# Initialize inventories
Inventory = StoreInventory()
myStuff = list()
myShoppingCart = list()

# Placeholder bank account
myBankAccount = UserBankAccount(1, 'placeholder')

# FUNCTIONS TO MANAGE MENUING SYSTEM IN MAIN SHOPPING PROGRAM

# I have switched the naming scheme of the project to Pastel Casing - easier to read in my opinion.

# Question - Is the syntax style similar to C# intentional or a mistake - if statements with a br


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
    itemInCart: Buyable
    for itemInCart in myShoppingCart:
        if itemInCart.name.lower() == UserChoice.lower():
            print(f'You have removed {itemInCart.name} from your shopping cart!')
            moveItemFromShoppingCartToInventory(itemInCart)
        else:
            print('Item could not be found in your shopping cart. Nothing was removed.')


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
        print("\n****************************************************** ")
        print("Please choose from one of the following menu options: ")
        print("1. View catalog of items to buy")
        print("2. Buy an item")
        print("3. View your cart of held items")
        print("4. Review the items you already own")
        print("5. View the status of your financials")
        print("6. YOUR CUSTOM IDEA HERE??")
        print("7. Exit program")

        userChoice = int(input())

        if userChoice == 1:
            ViewCatalog()
        elif userChoice == 2:
            BuyItem()
        elif userChoice == 3:
            ReviewMyShoppingCart()
        elif userChoice == 4:
            ReviewMyInventory()
        elif userChoice == 5:
            ReviewUserFinances()
        elif userChoice == 6:
            print("YOUR CONTENT HERE!")
        elif userChoice == 7:
            print('Thanks for shopping! Now exiting program ... ')
            break
        else:
            print('Incorrect input! Please select an option again.')

def StartProgram():
    print('Welcome to the Storefront!')
    print('Before you begin shopping, please set up a bank account.')
    deposit = input('How much do you want to deposit into your account?: ')
    global myBankAccount
    myBankAccount = UserBankAccount(deposit)
    StillShopping = True
    MainMenu()


# Starts Program
StartProgram()







def CheckPassword():
    passEntry = input('Please enter your password to confirm your identity: ')
    if passEntry == Password:
        return True
    else:
        print('Incorrect password!')
        return False


class UserBankAccount:

    def __init__(self, initialDeposit, password=None):
        self.Balance = float(initialDeposit)
        if password is None:
            self.SetPassword()

    def SetPassword(self):
        global Password
        Password = input('Please enter a password for your account: ')
        confirmPassword = input('Please input your password one more time to confirm it!: ')
        if Password != confirmPassword:
            print('Your passwords to not match ... ')
            self.SetPassword()
        else:
            print('Password set! Your account is now ready!')

    # Returns true if you have more balance than cost, false if you don't
    def CanUserAffordItem(self, Amount):
        if float(Amount) <= self.Balance:
            return True
        else:
            return False

    def makePurchase(self, Amount):
        if CheckPassword():
            if Amount <= self.Balance:
                self.Balance -= Amount
                print(f'{Amount} spent from your account.')
                print(f'You now have ${self.Balance} remaining.')
                return True
            else:
                print('You do not have enough funds left to afford this item.')
                return False
        else:
            return False

    def balanceReport(self):
        print(f'You have $ {self.Balance} left in your account.')

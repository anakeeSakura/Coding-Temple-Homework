#Workshop of the Day: Python OOP Bank Program Walkthrough



''' Create a BankAccount class: '''

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def  deposit(self, amount):
        amount = float(amount)
        if(amount > 0):
            self.balance += amount
            print(f"${amount}. added to your account! New balance is ${self.balance}")
        else:
            print('Deposit amount muct be greater than zero!')

    def withdrawal(self, amount):
        amount  = float(amount)
        if (amount > 0):
            if (self.balance >= amount):
                self.balance -= amount
                print(f'You withdrew ${amount:.2f} ! Your remaining balance is:{self.balance:.2f}')
            else:
                    print('Insufficient funds')
        else:
            print('Withdrawal amount must be greater than zero!')

    def check_balance(self):
        print(f'Account Holder: {self.account_holder}, Current Balance: ${self.balance:.2f}')

class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder):
        if (account_holder not in self.accounts):
            new_account = BankAccount(account_holder)
            self.accounts[account_holder] =  new_account
            print(f'Account created for {account_holder}!')
        else:
            print(f'Account already exists for {account_holder}')

    def get_account(self,  account_holder):
        if (account_holder in self.accounts):
            account =  self.accounts[account_holder]
            return account
        else:
            print(f'Account holder {account_holder} not found')


'''Create a CLI also known as runner'''
def runner():
    bank = Bank()
    while True:
        print('''
              ********* Bank Menu  *********

              1. Create Account
              2. Deposit Money
              3. Withdrawal Money
              4. Check Balance
              5. Exit
              ''')
        choice = input('What would you like to do today? (Choose a number)')
        if choice == '1':
            name = input('What is the name of the Account Holder?: ')
            bank.create_account(name)
        elif  (choice == '2'):
            name = input('What is the name of the Account Holder?: ')
            account = bank.get_account(name)
            if account:
                amount = input('How much would yuou like to  deposit? ')
                account.deposit(amount)
        elif (choice ==  '3'):
            name = input('What is the name of the Account Holder?: ')
            account = bank.get_account(name)
            if account:
                amount = input('How much would you like to  withdraw? ')
                account.withdrawal(amount)
        elif  (choice == '4'):
            name = input('What is the name of the Account Holder?: ')
            account = bank.get_account(name)
            if account:
                account.check_balance()
        elif  (choice == '5'):
            print('Than you for Banking with us! Goodbye')
            break
        else:
            print('Invalid choice. Please choose a valid option')

runner()





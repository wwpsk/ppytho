class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'На рахунок {self.account_number} внесено {amount} одиниць.')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'З рахунку {self.account_number} знято {amount} одиниць.')
        else:
            print(f'Недостатньо коштів на рахунку {self.account_number}.')

    def transfer(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.deposit(amount)
            print(f'З рахунку {self.account_number} переказано {amount} одиниць на рахунок {other_account.account_number}.')
        else:
            print(f'Недостатньо коштів на рахунку {self.account_number} для здійснення переказу.')

account1 = BankAccount('001', 1000)
account2 = BankAccount('002', 500)

account1.deposit(200)
account1.withdraw(150)
account1.transfer(account2, 300)

account2.deposit(1000)
account2.transfer(account1, 700)
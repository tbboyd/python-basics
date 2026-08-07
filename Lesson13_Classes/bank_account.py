class BankAccount:

    def __init__(self, owner, balance, ):

        self.name = owner
        self.amount = balance

        pass

    def show_balance(self):
        print('Name:', self.name)
        print('Balance: $', self.amount)

trystan = BankAccount('trystan', 500)

trystan.show_balance()
'''Accont class definition'''
from decimal import Decimal

class Account:
    """Account class for maintaining bank account balance"""

    def __init__(self, name, balance):
        """Initializes an Account object"""

        # if balance is less than zero, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00')

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money to the account"""

        if amount < Decimal('0.00'):
            raise ValueError('Amount must be positive')

        self.balance += amount





account1 = Account('John Green', Decimal(50.00))
print(account1.balance)
account1.balance = Decimal('-1000')
print(account1.balance)



# for x in range(4):
#     for y in range (3):
#         print(f'{x}, {y}')
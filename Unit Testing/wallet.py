import pytest
# imple cash processor for the wallet

class Wallet:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount   

    # Processing the amount to be added to the wallet
    def add_cash(self, value):
        self.balance += value

    # Processing the amount to be withdrawn from the wallet
    def spend_cash(self,value):
        if value > self.balance:
            raise InsufficientAmount("Not enough cash in the wallet{}".format(value))
        else:
            self.balance -= value
        
class InsufficientAmount(Exception):
    pass


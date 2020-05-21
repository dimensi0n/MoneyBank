from src.models.payment import Payment as payment
import sqlite3

class MoneyBank:

    """ 
    Initiate MoneyBank machine program
    > pieces are the pieces inside the moneybank
    """
    def __init__(self, pieces = [], bills = []):
        self.available_pieces = pieces
        self.available_bills = bills
        self.database = sqlite3.connect('database.db')

    """
    Return how much money you have to give back
    > given_pieces is an array of given pieces, has to be upper than price
    > price is the price of the object the customer wants to buy
    """
    def giveBack(self, given_pieces = [], given_bills = [], price = 0):
        pieces = self.available_pieces + given_pieces
        bills = self.available_bills + given_bills
        toGiveBack = sum(given_pieces) + sum(given_bills) - price
        if toGiveBack == 0:
            return 0, []
        solution_bills = []
        solution_pieces = []

        for bill in bills:
            if bill <= toGiveBack:
                solution_bills.append(bill)
                toGiveBack -= bill

        for piece in pieces:
            if piece <= toGiveBack:
                solution_pieces.append(piece)
                toGiveBack -= piece

        return round(toGiveBack, 2), solution_bills, solution_pieces
            
    """
    Add money to the MoneyBank machine and return how much money you have to give back
    > given_pieces is an array of given pieces, has to be upper than price
    > price is the price of the object the customer wants to buyi
    It returns an array, the first value is the returned pieces, the second is the difference if there is no combination to get exact returned value
    """
    def pay(self, given_pieces = [], given_bills = [], price = 0):
        Payment = payment(price, self.database)
        Payment.create()
        sumOfGivenMoney = sum(given_pieces) + sum(given_bills)
        if sumOfGivenMoney == price:
            self.available_pieces = self.available_pieces + given_pieces
            self.available_bills = self.available_bills + given_bills
            # The price is correct you do not have to give money back to the customer
            return 0;
        elif sumOfGivenMoney > price:
            moneyReturned = self.giveBack(given_pieces, given_bills ,price)
            self.available_pieces = self.available_pieces + given_pieces
            self.available_bills = self.available_bills + given_bills
            #return [moneyReturned, sum(moneyReturned) - price]
            return moneyReturned
        else:
            # Return -1 if the customer did not give enough money to buy the object
            return -1
    
    """
    Get the gain of today
    It returns an array of sql entries
    """
    def getGainOfToday(self):
        Payment = payment(database=self.database)
        return Payment.getGainOfToday()

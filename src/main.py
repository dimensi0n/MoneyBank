
class MoneyBank:

    """ 
    Initiate MoneyBank machine program
    > pieces are the pieces inside the moneybank
    """
    def __init__(self, pieces):
        self.available_pieces = pieces

    """
    Return how much money you have to give back
    > given_money is an array of given pieces, has to be upper than price
    > price is the price of the object the customer wants to buy
    """
    def giveBack(self, given_money, price):
        pieces = self.available_pieces + given_money
        toGiveBack = sum(given_money) - price
        if toGiveBack == 0:
            return 0, []
        solution = []
        for money in pieces:
            if money <= toGiveBack:
                solution.append(money)
                toGiveBack -= money

        return round(toGiveBack, 2), solution
            
    """
    Add money to the MoneyBank machine and return how much money you have to give back
    > given_money is an array of given pieces, has to be upper than price
    > price is the price of the object the customer wants to buyi
    It returns an array, the first value is the returned pieces, the second is the difference if there is no combination to get exact returned value
    """
    def pay(self, given_money, price):
        sumOfGivenMoney = sum(given_money)
        if sumOfGivenMoney == price:
            self.available_pieces = self.available_pieces.extend(given_money)
            # The price is correct you do not have to give money back to the customer
            return 0;
        elif sumOfGivenMoney > price:
            self.available_pieces.extend(given_money)
            moneyReturned = self.giveBack(given_money, price)
            #return [moneyReturned, sum(moneyReturned) - price]
            return moneyReturned
        else:
            # Return -1 if the customer did not give enough money to buy the object
            return -1


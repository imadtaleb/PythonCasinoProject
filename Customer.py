# -------------------------------------------------------------------------------------------------------------------- #
# TSE Python Project
#
# Authors: Imad Taleb & Vincent Fargal
# Date:    29/01/2017
#
# Description:
# This script describes the different kind of customers a casino has.
# -------------------------------------------------------------------------------------------------------------------- #

# Import modules
import random
random.seed(3456)

# -------------------------------------------------------------------------------------------------------------------- #
# Customer
# ---------------------------------------------------------


class Customer(object):
    """Customer of a casino"""
    def __init__(self, budget):
        self.budget = budget

    def tip(self):
        """Tip a barman"""
        tip = random.randint(0, 20)
        self.budget = self.budget - tip
        return tip

    def buy_drink(self):
        """Buy a drink if 60$ in the pocket"""
        if self.budget > 60:
            self.budget = self.budget - 20
            return self.budget


# -------------------------------------------------------------------------------------------------------------------- #
# Returning Customer
# ---------------------------------------------------------


class ReturningCustomer(Customer):
    """A returning customer"""
    def __init__(self):
        budget = random.randint(100, 300)
        super(ReturningCustomer, self).__init__(budget)

    def bet_money(self, min_bet):
        """Bets the minimum amount if enough money - update budget"""
        if self.budget >= min_bet:
            self.bet = min_bet
            self.budget = self.budget - self.bet
        else:
            self.bet = 0
        return self.bet

    def __str__(self):
        """In order to print the customer's type"""
        return self.__class__.__name__


# -------------------------------------------------------------------------------------------------------------------- #
# One-Time Customers: a regular one and a bachelor
# ---------------------------------------------------------


class OneTimeCustomer(Customer):
    """A one-time customer"""
    def __init__(self):
        budget = random.randint(200, 300)
        super(OneTimeCustomer, self).__init__(budget)

    def bet_money(self):
        """Bets 1/3 of his budget amount if enough money - update budget"""
        self.bet = random.randint(0, round((1/3) * self.budget))
        self.budget = self.budget - self.bet
        return self.bet

    def __str__(self):
        """In order to print the customer's type"""
        return self.__class__.__name__


class Bachelor(Customer):
    """A special kind of one-time customer: bachelor"""
    def __init__(self):
        budget = random.randint(200, 500)
        super(Bachelor, self).__init__(budget)

    def bet_money(self):
        """Bets the minimum amount if enough money - update budget"""
        self.bet = random.randint(0, self.budget)
        self.budget = self.budget - self.bet
        return self.bet

    def __str__(self):
        """In order to print the customer's type"""
        return self.__class__.__name__


# End of script

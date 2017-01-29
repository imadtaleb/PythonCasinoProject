# -------------------------------------------------------------------------------------------------------------------- #
# TSE Python Project
#
# Authors: Imad Taleb & Vincent Fargal
# Date:    29/01/2017
#
# Description:
# After creating Roulette and Craps games we thought it was better implementing a class Table with games inherited from
# this parent class.
# This script describes the relationship between these 3 classes.
# -------------------------------------------------------------------------------------------------------------------- #

# Import modules
from itertools import product
import random
random.seed(3456)


# -------------------------------------------------------------------------------------------------------------------- #
# Table: a table on which games are played in a casino
# ---------------------------------------------------------


class Table(object):
    """A table on which players play a game in a casino"""

    def __init__(self, bet_range, min_bet_choice, croupier, n_customers):
        """These arguments are set to null values and will be changed afterwards"""
        self.bet_range = bet_range
        self.min_bet = random.choice(min_bet_choice)
        self.croupier = croupier
        self.customers = n_customers
        self.bets = []
        self.bet_amounts = []

    def set_bets(self):
        for _ in range(self.customers):
            self.bets.append(random.randint(self.bet_range[0], self.bet_range[1]))
        return self.bets

    def set_bet_amounts(self):
        for _ in range(self.customers):
            self.bet_amounts.append(random.randint(0, self.min_bet * 10))  # Don't know how to link it to customers
        return self.bet_amounts

    def aboveminimum(self):
        """A simplified version of the aboveminimum functions in the Roulette and Craps games"""
        out_list = [bet >= self.min_bet for bet in self.bet_amounts]
        return out_list

    def simulategame(self):
        """ Needed here to call it in the simulateround method
        Takes bets and bet_amounts and returns amount won by casino and each player
        This will be filled by subclasses methods."""
        self.gains = []
        return self.gains

# -------------------------------------------------------------------------------------------------------------------- #
# A Roulette assigned to a table
# ---------------------------------------------------------


class Roulette(Table):
    """A first kind of game assigned to a table: a Roulette for which we can bet from 0 to 36"""

    def __init__(self, croupier, n_customers):
        super(Roulette, self).__init__((0, 36), [50, 100, 200], croupier, n_customers)

    def spinthewheel(self):
        """Spinning the wheel and providing the result depending on the customers' bets"""
        result = random.randint(0, 36)
        print("Spinning the wheel...\nThe ball lands on %s" % result)

        # Are there winners? compare bets to the result of the spin
        self.results = []
        for item in self.bets:
            if item == result:
                self.results.append(True)
            else:
                self.results.append(False)

        winners = self.results.count(True)
        if winners == 1:
            print("There is one correct bet.")
        elif winners > 1:
            print("There are %s correct bets" % winners)
        else:
            print("No winners this round.")
        return self.results

    def simulategame(self):
        """SimulateGame: takes bets and bet_amounts and returns amount won by casino and each player"""
        self.gains = []
        consumer_gains = []  # List of customer gains that will be provided in the gains list returned
        casino_gains = []    # List of casino gains that will be summed up to get the total amount won by the casino

        above = self.aboveminimum()  # Get the lists of amounts above the minimum
        spin = self.spinthewheel()  # Get the list of results of the spin

        for index, item in enumerate(spin):
            if item is False:
                # If the bet is wrong, the casino wins and the player looses
                casino_gains.append(self.bet_amounts[index])
                consumer_gains.append(0)
            else:
                # If the bet is good, we need to check if the amount is above the minimum
                if above[index] is False:
                    # If not the casino wins
                    casino_gains.append(self.bet_amounts[index])
                    consumer_gains.append(0)
                else:
                    # Otherwise, the player wins 30 times the amount he bet
                    casino_gains.append(0)
                    consumer_gains.append(self.bet_amounts[index] * 30)

        self.gains.append(sum(i for i in casino_gains))
        self.gains.append(consumer_gains)
        return self.gains


# -------------------------------------------------------------------------------------------------------------------- #
# A Craps assigned to a table
# ---------------------------------------------------------

class Craps(Table):
    """A first kind assigned to a table: a Craps for which we can bet from 0 to 12"""

    def __init__(self, croupier, n_customers):
        super(Craps, self).__init__((1, 12), [0, 25, 50], croupier, n_customers)

    def dices(self):
        """Resulting sum of rolling 2 dices"""
        self.sum = random.randint(1, 6) + random.randint(1, 6)
        return self.sum

    def rollthedices(self):
        """Rolling the dices and providing the result depending on the customers' bets"""
        self.result = self.dices()
        print("Throwing the dices...\nThe sum of the two dices is %s" % self.result)

        # Are there winners?
        self.results = []
        for item in self.bets:
            if item == self.result:
                self.results.append(True)
            else:
                self.results.append(False)

        winners = self.results.count(True)
        if winners == 1:
            print("There is one winner.")
        elif winners > 1:
            print("There are %s winners" % winners)
        else:
            print("There is no winner.")
        return self.results

    def probability(self, bet):
        """Function computing the probability that a particular number appears """

        self.nbbetapp = 0
        for i in product(range(1, 7), repeat=2):
            self.diceSum = 0
            for j in i:
                self.diceSum += j
            if self.diceSum == bet:
                self.nbbetapp += 1
        odds = self.nbbetapp / 36
        return odds

    def simulategame(self):
        """Function simulating the whole game and printing consumers and casino gains """

        consumer_gains = []
        casino_gains = []
        self.gains = []

        above = self.aboveminimum()

        dice = self.rollthedices()

        for index, item in enumerate(dice):
            if item is False:
                casino_gains.append(round(0.1 * self.bet_amounts[index]))
                consumer_gains.append(0)
            else:
                if above[index] is False:
                    casino_gains.append(round(0.1 * self.bet_amounts[index]))
                    consumer_gains.append(0)
                else:
                    casino_gains.append(0)
                    consumer_gains.append(self.bet_amounts[index] * round(0.9 / self.probability(self.bets[index])))

        self.gains.append(sum(i for i in casino_gains))
        self.gains.append(consumer_gains)
        return self.gains


# End of script #

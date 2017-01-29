# -------------------------------------------------------------------------------------------------------------------- #
# TSE Python Project
#
# Authors: Imad Taleb & Vincent Fargal
# Date:    29/01/2017
#
# Description:
# This script corresponds to the first attempt to write a Craps function following the instructions in Part 1 of
# the exam ppt.
# The goal is to output the casino and the customer gains when two dices are thrown.
# This game is refined, simplifying the AboveMinimum function and adding the Table abstraction, in script "Tables.py".
# -------------------------------------------------------------------------------------------------------------------- #

# Import useful libraries - module - functions

import random
# random.seed(3456)  # This is used to fixed the random generator so we can test the output
from itertools import product  # This is used to when computing probability of obtaining a particular number

# -------------------------------------------------------------------------------------------------------------------- #
# Define useful functions for the game
# ---------------------------------------------------------


class Craps(object):
    """A Dice game"""

    def __init__(self, min_amount):
        self.min = min_amount


    def AboveMinimum(self, bet_amounts):
        """Function determining whether the bet is above the minimum or not """

        self.out_list = []
        for index, item in enumerate(bet_amounts):
            if item < self.min:
                self.out_list.append(False)
            else:
                self.out_list.append(True)
        return self.out_list


    def Dices(self):
        """Function summing up the results of throwing two dices """

        self.a = random.randint(1,6) + random.randint(1,6)
        return self.a


    def RollTheDices(self, bets):
        """Function providing results of craps game depending on bets """

        self.result = self.Dices()
        print("Throwing the dices...\nThe sum of the two dices is %s" % self.result)

    # Are there winners?
        self.results = []
        for item in bets:
            if item == self.result:
                self.results.append(True)
            else:
                self.results.append(False)

        winners = self.results.count(True)
        if winners == 1:
            print("There is one correct bet.")
        elif winners > 1:
            print("There are %s correct bets" % winners)
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


    def SimulateGame(self, bets, bet_amounts):
        """Function simulating the whole game and printing consumers and casino gains """

        consumer_gains = []
        casino_gains = []
        self.gains = []

        above = self.AboveMinimum(bet_amounts)

        dice = self.RollTheDices(bets)

        for index, item in enumerate(dice):
            if item is False:
                casino_gains.append(round(0.1 * bet_amounts[index]))
                consumer_gains.append(0)
            else:
                if above[index] is False:
                    casino_gains.append(round(0.1 * bet_amounts[index]))
                    consumer_gains.append(0)
                else:
                    casino_gains.append(0)
                    consumer_gains.append(bet_amounts[index] * round(0.9 / self.probability(bets[index])))

        self.gains.append(sum(i for i in casino_gains))
        self.gains.append(consumer_gains)
        return self.gains


# End of script #



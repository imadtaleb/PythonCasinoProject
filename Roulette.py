# -------------------------------------------------------------------------------------------------------------------- #
# TSE Python Project
#
# Authors: Imad Taleb & Vincent Fargal
# Date:    29/01/2017
#
# Description:
# This script corresponds to the first attempt to write a Roulette function following the instructions in Part 1 of
# the exam ppt.
# The goal is to output the casino and the customer gains when a wheel is spin.
# This game is refined, simplifying the AboveMinimum function and adding the Table abstraction, in script "Tables.py".
# -------------------------------------------------------------------------------------------------------------------- #

# Import useful module to simulate the roulette
import random
random.seed(3456)  # This is used to fixed the random generator so we can test the output
# print([random.randint(1,10) for p in range(0,5)])


# -------------------------------------------------------------------------------------------------------------------- #
# Define a Roulette module and functions for the game
# ---------------------------------------------------------

class Roulette(object):
    """A Roulette game"""

    def __init__(self, min_amount):
        self.min = min_amount

    def AboveMinimum(self, bet_amounts):
        """AboveMinimum: takes a list of bet amounts and returns a list of booleans [True, False] if
        amount >= min or not"""
        self.out_list = []
        for index, item in enumerate(bet_amounts):
            if item < self.min:
                self.out_list.append(False)
            else:
                self.out_list.append(True)
        return self.out_list

    def SpinTheWheel(self, bets):
        """Spinning the wheel and providing the result"""
        result = random.randint(0, 36)
        print("Spinning the wheel...\nThe ball lands on %s" % result)

        # Are there winners? compare bets to the result of the spin
        self.results = []
        for item in bets:
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

    def SimulateGame(self, bets, bet_amounts):
        """SimulateGame: takes bets and bet_amounts and returns amount won by casino and each player"""

        consumer_gains = []  # List of consumer gains that will be provided in the gains list returned
        casino_gains = []    # List of casino gains that will be summed up to get the total amount won by the casino
        self.gains = []

        above = self.AboveMinimum(bet_amounts)  # Get the lists of amounts above the minimum
        spin = self.SpinTheWheel(bets)  # Get the list of results of the spin

        for index, item in enumerate(spin):
            if item is False:
                # If the bet is wrong, the casino wins and the player looses
                casino_gains.append(bet_amounts[index])
                consumer_gains.append(0)
            else:
                # If the bet is good, we need to check if the amount is above the minimum
                if above[index] is False:
                    # If not the casino wins
                    casino_gains.append(bet_amounts[index])
                    consumer_gains.append(0)
                else:
                    # Otherwise, the player wins 30 times the amount he bet
                    casino_gains.append(0)
                    consumer_gains.append(bet_amounts[index] * 30)

        self.gains.append(sum(i for i in casino_gains))
        self.gains.append(consumer_gains)
        return self.gains


# End of script #

# -------------------------------------------------------------------------------------------------------------------- #
# TSE Python Project
#
# Authors: Imad Taleb & Vincent Fargal
# Date:    29/01/2017

# Description:
# Simulation for the Craps and Roulette games using both the standard script and the Table class. One should bare
# in mind to put "import Roulette" as comment when needed.
# NOTICE THAT SCRIPT SHOULD BE RUN BY SECTIONS
# -------------------------------------------------------------------------------------------------------------------- #

# Import modules and functions
import Roulette
import Craps
import random
from collections import Counter
import numpy as np
from matplotlib import pyplot as plt

# -------------------------------------------------------------------------------------------------------------------- #
# Simulation of the Roulette game
# ---------------------------------------------------------


"""
Although we will provide simulations with predetermined vectors of bets and bet amounts, one could have asked
potential users to give their bets and their bet amounts, while checking if the bets are within 0 and 36 and if the
bet amounts are above the minimum value
This has been applied to the Roulette game but could have been provided for the Craps game
"""


# # Parameters of the game
# NumberPlayers = 2
# MinBet = 100
#
# # List of bets of each player
# bets = []
# bet_amounts = []
#
# for i in range(0, NumberPlayers):
#     print("Player %s: " % (i+1))
#
#     # Ask which number each player want to bet on
#     while True:
#         try:
#             a = int(input("On which number do you want to bet? "))
#             if a in range(0, 37):
#                 bets.append(a)
#                 break
#             else:
#                 print("Sorry, you must choose a number between 0 and 36 (both included). ")
#         except ValueError:
#             print("Sorry, you must choose a number between 0 and 36 (both included). ")
#
#     # Ask how much money they want to bet
#     while True:
#         try:
#             b = int(input("How much do you want to bet (in $)? "))
#             if b >= MinBet:
#                 bet_amounts.append(b)
#                 break
#             else:
#                 print("Sorry, you need to bet %s$ or more. " % MinBet)
#         except ValueError:
#             print("Sorry, you must bet an amount of money (in $). ")
#
# print(bets)
# print(bet_amounts)
#
# table1 = Roulette.Roulette(MinBet)
# print(table1.SimulateGame(bets, bet_amounts))


"""
Simulation with vectors of bets and bet amounts using Roulette class
"""
amounts1 = [10, 85, 120, 65, 150, 122]
bets1 = [10, 24, 36, 0, 11, 24]
table1 = Roulette.Roulette(100)
print(table1.SimulateGame(bets1, amounts1))
print(table1.SimulateGame(bets1, amounts1))

# -------------------------------------------------------------------------------------------------------------------- #
# Simulation of the Craps game
# ---------------------------------------------------------

"""
Simulation with vectors of bets and bet amounts
"""
table2 = Craps.Craps(50)
print(table2.SimulateGame(bets1, amounts1))
print(table2.SimulateGame(bets1, amounts1))


# -------------------------------------------------------------------------------------------------------------------- #
# Simulation of the Craps game without the seed :
# PUT "import Roulette" AS COMMENT SO AS NOT TO IMPORT THE SEED !!!
# ---------------------------------------------------------


"""
1000 throws of 2 dices with a plot of the distribution of results
"""

# #  1000 dice throws
# dicethrows = []
# for i in range(0, 1000):
#     dicethrows.append(table2.Dices())

# # Plots of dice throws
# labels, values = zip(*Counter(dicethrows).items())
# indexes = np.arange(len(labels))
# width = 1
# plt.bar(indexes, values, width)
# plt.xticks(indexes + width * 0.5, labels)
# plt.show()

"""
1000 simulations to check the 90% / 10% distribution of the gains
"""

# Running 1000 Craps simulations
# casino_gains = []
# customer_gains = []
# casino_share = []
# customer_share = []
# table2 = Craps.Craps(50)
#
#
# for i in range(0, 1000):
#
#     betted_amounts = [random.randint(50, 200) for j in range(10)]  # created lists
#     bets = [table2.Dices() for k in range(10)]
#
#     result = table2.SimulateGame(bets, betted_amounts)
#
#     casino_gains.append(result[0])
#     customer_gains.append(sum(result[1]))
#
#     casino_share.append(sum(casino_gains)/(sum(casino_gains)+sum(customer_gains)))
#     customer_share.append(sum(customer_gains) / (sum(casino_gains)+(sum(customer_gains))))
#
#
# print(round(sum(casino_share)/len(casino_share), 1))
#
# print(round(sum(customer_share)/len(customer_share), 1))


# -------------------------------------------------------------------------------------------------------------------- #
# Simulation of Roulette and Craps games using Table.py
# ---------------------------------------------------------

"""Testing the Table class functions"""
# table = Table.Roulette(1, 5)
# print(table.min_bet)
# print(table.set_bets())
# print(table.set_bet_amounts())
# print(table.aboveminimum())
# print(table.simulategame())

# print("-----------")

# table = Table.Craps(1, 5)
# print(table.min_bet)
# print(table.set_bets())
# print(table.set_bet_amounts())
# print(table.aboveminimum())
# print(table.simulategame())

# End of script #

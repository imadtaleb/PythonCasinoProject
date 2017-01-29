# -------------------------------------------------------------------------------------------------------------------- #
# TSE Python Project
#
# Authors: Imad Taleb & Vincent Fargal
# Date:    29/01/2017
#
# Description:
# This script describes the different kind of employees a casino has.
# They both get a fixed and a variable wage
# -------------------------------------------------------------------------------------------------------------------- #


class Employee(object):
    """Employee of a casino"""
    def __init__(self, fixed_wage):
        self.fixed_wage = fixed_wage


# -------------------------------------------------------------------------------------------------------------------- #
# Two different kind of employees: croupiers and barmen
# ---------------------------------------------------------


class Croupier(Employee):
    """A first kind of employee: a croupier"""
    def __init__(self, fixed_wage):
        super(Croupier, self).__init__(fixed_wage)
        self.variable_wage = []

    def calculate_commission(self, casino_gains):
        commission = 0.005 * casino_gains
        self.variable_wage.append(commission)
        return self.variable_wage

    def calculate_wage(self):
        self.wage = self.fixed_wage + sum(self.variable_wage)
        return self.wage


class Barman(Employee):
    """A second kind of employee: a barman"""
    def __init__(self, fixed_wage):
        super(Barman, self).__init__(fixed_wage)
        self.tips = []

    def calculate_tip(self, tip):
        self.tips.append(tip)
        return self.tips

    def calculate_wage(self):
        self.wage = self.fixed_wage + sum(self.tips)
        return self.wage


# End of script

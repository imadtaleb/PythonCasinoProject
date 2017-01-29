# -------------------------------------------------------------------------------------------------------------------- #
# TSE Python Project
#
# Authors: Imad Taleb & Vincent Fargal
# Date:    29/01/2017
#
# Description:
# This script corresponds to a trial to implement the full casino. The main feature should ghave been the Simulate
# evening method that is supposed to run three rounds of games and assign wages and print gains.
# -------------------------------------------------------------------------------------------------------------------- #

# Import modules
import Table2
import Employee
import Customer
import random
random.seed(3456)


# -------------------------------------------------------------------------------------------------------------------- #
# A Casino
# ---------------------------------------------------------


class Casino(object):
    """A casino"""

    def __init__(self, n_roulette, n_craps, n_barmen, empl_wage, casino_cash, n_customers, p_R_customer,
                 p_bachelor, free_endowment):
        self.n_roulette = n_roulette
        self.n_craps = n_craps
        self.n_barmen = n_barmen
        self.empl_wage = empl_wage
        self.casino_cash = casino_cash
        self.n_customers = n_customers
        self.p_R_customer = p_R_customer
        self.p_bachelor = p_bachelor
        self.free_endowment = free_endowment

    def customer_mix(self):
        self.customers = []

        # Define number of customers of each category
        returning_customers = round(self.n_customers * self.p_R_customer)
        bachelor_customers = round(self.n_customers * self.p_bachelor)
        one_time_customers = self.n_customers - returning_customers - bachelor_customers

        # Create customers depending on category
        for _ in range(returning_customers):
            ret_c = Customer.ReturningCustomer()
            self.customers.append(ret_c)
        for _ in range(bachelor_customers):
            b_c = Customer.Bachelor()
            self.customers.append(b_c)
        for _ in range(one_time_customers):
            ot_c = Customer.OneTimeCustomer()
            self.customers.append(ot_c)
        return self.customers

    def setup_tables(self):
        """This function should assign a croupier, customers and a game played"""
        assigned_table = []
        self.tables = []

        # assign a table to each customer
        for _ in self.customers:
            assigned_table.append(random.randint(1, self.n_roulette + self.n_craps))

        # get list of lists of customers assigned to each table
        customer_list = [[] for _ in range(self.n_roulette + self.n_craps)]
        for i in range(0, self.n_customers):
            print(assigned_table[i])
            j = assigned_table[i]
            customer_list[j-1].append(self.customers[i])

        # Create tables with their croupier and customers
        for i in range(0, self.n_roulette):
            self.tables.append(Table2.Roulette(Employee.Croupier(self.empl_wage), customer_list[i]))
        for j in range(self.n_roulette, self.n_roulette + self.n_craps):
            self.tables.append(Table2.Craps(Employee.Croupier(self.empl_wage), customer_list[j]))

        return customer_list, self.tables

    def simulate_round(self):
        """Simulate games on each table of the casino"""
        self.setup_tables()
        outcomes_list = []
        for table in self.tables:
            outcomes_list.append(table.simulategame())
            print(table.simulategame())
        return outcomes_list

    #    ...

    # def SimulateEvening(self):
    #     """This function simulates an entire evening where:
    #     - A new set of customers is determined with the percentages roughly matching the ones mentioned during setup.
    #     - 3 game rounds are played on all tables. Every round all customers are randomly distributed over all tables.
    #     - Customers go get drinks about 5 times where they get one of the random barmen available and tip him.
    #     - The casino gets money from winning games and the sold drinks (suppose the drinks are pure profit).
    #     - The casino pays the one time fee for bachelors, customers winning games and wages are paid per evening"""


# End of script

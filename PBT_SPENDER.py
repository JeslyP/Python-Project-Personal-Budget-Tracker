import matplotlib as plt
from matplotlib import category
    """ This module is used to calculate the budget of a person based on their income and expenses. """

    
def input_income():
    return float(input ("Enter the amount of your monthly income: "))


def input_expenses():
    expenses  = []
    category = ['Transportation', 'Food', 'Utilities', 'Entertainment', 'Miscellaneous']
    for catrgory in category:
        expenses.append(float(input(f"Enter the amount you spend on {category}: ")))
        return expenses
    
def calculate_budget(income, expenses):
    total_expenses = sum(expenses)
    balance = income - total_expenses
    return balance

sd
import matplotlib as plt
from matplotlib import category
    
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

def display_spending(expenses)
    labels = expenses.keys()
    sizes = expenses.values()

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Monthly Expenses Distruibution")
    plt.show()


def main():
    print ("Welcome to the Personal Budget Tracker")
    income = input_income()
    expenses = input_expenses()
    remaining_budget = calculate_budget(income, expenses)

    print(f"Your remaining budget is ${remaining_budget}")
    display_spending(expenses)

if __name__ == "__main__":
    main()
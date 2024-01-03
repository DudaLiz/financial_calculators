# This is the Capstone Project One of my Hyperion Dev Bootcamp - C5.
# This code creates user-friendly investment and home loan calculators using control structures if - elif - else.
# The user inputs the investment or loan data.
# The program outputs how much they will gain from the investment after a number of years or pay towards the loan monthly.

import math

import colorama  # added use of colours to improve readability for the user.
from colorama import Fore
colorama.init(autoreset=True)

# defined functions at the start of the code so formulas are clear and easily accesible.
def simple_interest_investment(principal, rate, time):
    return int(principal * (1 + rate * time))

def compound_interest_investment(principal, rate, time):
    return principal * math.pow((1+rate),time)

def bond_repayment(value, rate, time):
    return (rate*value)/(1 - (1 + rate)**(-time))

# Gave the company a fictional name for now and created friendly outputs for the user.
print(Fore.MAGENTA + "\nWelcome to Tiny Finances! We are here to help you take care of your future.\n")
print("Please use the calculators below to simulate how much you'll earn on your investment or pay on your home loan.")

print(Fore.BLUE + "\nInvestment - Will calculate the amount of interest you'll earn on your investment.\n")
print(Fore.GREEN + "Bond - Will calculate the amount you'll have to pay monthly on a home loan.\n")

# Added .lower to allow for all forms of capitalization.
user_input = input("Enter either 'Investment' or 'Bond' from the menu above to proceed: ").lower()

if user_input == "investment":
    principal_amount = float(input("Please enter the amount of money you wish to deposit (enter only numbers): "))
        
    annual_interest_rate = float(input("Please enter the interest rate of your chosen investment plan (do not enter the percentage sign): "))
    # Divided annual rate by 100 to transform it into a decimal.
    annual_interest_rate = float(annual_interest_rate) / 100
   
    time_in_years = float(input("How many years do you plan to invest for: "))
    
    interest = input("Would you like simple or compound interest? ").lower()
    
    if interest == "simple":
        result = int(simple_interest_investment(principal_amount,annual_interest_rate,time_in_years))
    elif interest == "compound":
        result = compound_interest_investment(principal_amount, annual_interest_rate, time_in_years)
    # Error message in red with extra tip to check spelling so user can identify the possible issue.    
    else:
        print(Fore.RED + "Invalid entry.\nPlease enter 'simple' or 'compound'.\nCheck your spelling.")

    print(f"The total amount after {time_in_years} years will be: {result:.2f}")

elif user_input == "bond":
    house_value = float(input("Please enter the present value of the home: "))
    annual_interest_rate = (input("Please enter the annual interest rate you pay on your loan (do not enter the percentage sign): "))
    annual_interest_rate = float(annual_interest_rate) / 100  
    
    time_in_months = int(input("In how many months do you plan to pay back your home loan? "))

    # Divided annual_interest_rate by 12 to get monthly interest rate.
    result_bond_repayment = bond_repayment(house_value, annual_interest_rate/12, time_in_months)
    print(f"The monthly bond repayment will be: {result_bond_repayment:.2f}")

else:
    print(Fore.RED + "You've entered an invalid response.\nPlease enter either Investment or Bond.\nCheck that your spelling is correct.")

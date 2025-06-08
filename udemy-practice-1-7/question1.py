# 1. Compound Interest Calculation
# Ask the user for the interest rate, principal, and number of years they are investing.
# Output the final amount earned.
# Use the formula:
# final amount = principal * (1 + interest_rate) ^ years

def main():
    print("Welcome to the Compound Interest Calculator!")

    rate = float(input("What is your interest rate? "))
    princ = float(input("what is your principal? "))
    yrs = int(input("How many years will you be investing? "))

    final = princ * (1 + rate)**yrs

    print(f"Your total after compounding interest will be: ${final:,.2f}")



main()
def main():
    desired = float(input("What is your desired amount of money? "))
    years = int(input("How long do you have to invest? "))
    rate = float(input("What is your current interest rate? "))

    necessary = desired / (1.0 + rate)**years

    print(f"You need to invest ${necessary:,.2f} to reach your goal")

main()
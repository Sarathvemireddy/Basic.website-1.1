principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time in years: "))
rate = float(input("Enter the rate of interest: "))
compound_interest = principal * (pow((1 + rate / 100), time)) - principal
print("The compound interest is:", compound_interest)

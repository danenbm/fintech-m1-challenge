# coding: utf-8
import csv
from pathlib import Path


"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
print("Part 1: Automate the Calculations")

loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# Use the `len` function to calculate the total number of loans in the list.
num_loans = len(loan_costs)
# Print the number of loans from the list.
print(f"Number of loans in the list: {num_loans}")

# What is the total of all loans?
# Use the `sum` function to calculate the total of all loans in the list.
total_val_all_loans = sum(loan_costs)
# Print the total value of the loans.
print(f"Total value of all loans in the list: ${total_val_all_loans:.2f}")

# What is the average loan amount from the list?
# Using the sum of all loans and the total number of loans, calculate the average loan price.
average_loan_amount = total_val_all_loans / num_loans
# Print the average loan amount
print(f"The average loan amount is: ${average_loan_amount:.2f}")


"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""
print("\nPart 2: Analyze Loan Data")

# Given the following loan data, we will calculate the present value for the loan.
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
# Print the Future Value and Remaining Months on the loan
print(f"Specific loan future value: ${future_value:.2f}")
print(f"Specific loan remaining months: ${remaining_months}")

# Use a minimum required return of 20% as the discount rate.
annual_discount_rate = 0.20
# Use the formula for Present Value (monthly version) to calculate a "fair value" of the loan.
present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
loan_price = loan.get("loan_price")
if present_value >= loan_price:
    print(f"The loan is worth its cost.  Its present value is ${present_value:.2f} and its price is ${loan_price:.2f}")
else:
    print(f"The loan is too expensive at ${present_value:.2f} and thus not worth ${loan_price:.2f}") 

# NOTE: The given loan above is worth its cost.  Its present value is $861.77 and its price is $500.00.

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""
print("\nPart 3: Perform Financial Calculations")

# Given the following new loan data, we will calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# This function calculates present value (monthly version of formula).
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months

    return present_value

# Use an `annual_discount_rate` of 0.2 for this new loan calculation.
annual_discount_rate = 0.20
# Use the function to calculate the present value of the new loan.
present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)
print(f"The present value of the loan is: {present_value}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""
print("\nPart 4: Conditionally filter lists of loans")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list to store inexpensive loans.
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    cost = loan.get("loan_price")
    if cost <= 500:
        inexpensive_loans.append(loan)

# Print the `inexpensive_loans` list
print("Inexpensive loans: ", inexpensive_loans)


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""
print("\nPart 5: Save the results")

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
print("Writing inexpensive loans to a CSV file...", end =" ")
with open(output_path, 'w', newline='') as output_file:
    # Create a csvwriter
    csvwriter = csv.writer(output_file)
    # Write the header to the CSV file
    csvwriter.writerow(header)

    # For each loan in the inexpensive loans list, write the
    # loan values to a row.
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())

print("DONE!")
''' this method calculates how much money we can make on an investment
Parameters:
principal: decimal - the starting money
interest_rate: decimal - rate per year
years: int - the amount of time you are investing money

Return:
float - the value of the investment after X number of years
'''


def calculate_apr(principal, interest_rate, years):
    "loops through to calculate total after each each year"
    for i in range(years+1):
        "variable to hold total amount of money and will be returned"
        total = principal * (1 + interest_rate) ** i

    "checks if any parameters are invalid and outputs false if so"
    if isinstance(total, float):
        print(total)
    else:
        print("False")


"to test function"
calculate_apr(500, .03, 65)
calculate_apr(200, .01, 50)

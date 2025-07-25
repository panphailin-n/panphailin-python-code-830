"""
Personel Finance Calculator
Student : [Panphailin Nukhunthod]
Date :[21/7/2568]
Purpose:Calculator monthly budget amd savings
"""

Monthly_income = float(input("User Monthly_income in THB :"))
rent_cost= float(input("Mounthly rent : "))
food_budget = int(input("Mounthly food budget in THB :"))
transportation_cost = float(input("Mounthly transportation expenses :"))
entertainment_budget = int(input("Mounthly entretainment budget :"))
emergency_fund_percent = float(input("Percentage to save for emergency(e.g.,10.5) :"))
investment_percent = float(input("Percentage to invest(e.g.,15.0) :"))

Total_Fixed=rent_cost+transportation_cost
Total_Variable=food_budget+entertainment_budget
Total_Expenses=Total_Fixed+Total_Variable
Remaining_income=Monthly_income-Total_Expenses
Emergency_Fund_Amount=Monthly_income*(emergency_fund_percent/100)
investment_Amount = Monthly_income * (investment_percent / 100)
Available_savings=Remaining_income-Emergency_Fund_Amount-investment_Amount
Expense_ratio=(Total_Expenses/Monthly_income)*100

print("")
print("===MOUNTHY BUDGET REPORT===")
print(f"Income :{Monthly_income:.2f}THB")
print(f"Fixed Expenses : {Total_Fixed:.2f}THB")
print(f"Variable Expenses :{Total_Variable:.2f}THB")
print(f"Total Expenses : {Total_Expenses:.2f}THB")
print(f"Remaining Income :{Remaining_income:.2f}THB")
print("")

print("===SAVINGS BREAKDOWN===")
print(f"Emergency Fund ({emergency_fund_percent}%): {Emergency_fund_Amount:.2f}THB")
print(f"Investment ({investment_percent}%):{investment_Amount:.2f}THB")
print(f"Available for Savings:{Available_savings:.2f}THB")
print("")

print("===ANALYSIS===")
print(f"Expense Ratio:{Expense_ratio:.2f}%")
print("")




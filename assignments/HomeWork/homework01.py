
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

result_add1 = rent_cost + transportation_cost
print(f"Total Fixed Expenses:   {rent_cost} + {transportation_cost} = {result_add1}")

result_add2= food_budget + entertainment_budget
print(f"Total Variable Expenses :    {food_budget} + {entertainment_budget} = {result_add2}")

result_add3= result_add1 + result_add2
print(f"Total  Expenses :    {result_add1} + {result_add2} = {result_add3}")

result_sub1 = Monthly_income -result_add3
print(f"Remaining Income:    {Monthly_income} - {result_add3} = {result_sub1}")

result_mul1 = Monthly_income * (emergency_fund_percent/100)
print(f" Investment Amount  : {Monthly_income} * {emergency_fund_percent/100} = {result_mul1}")

result_mul2 = Monthly_income * (investment_percent/100)
print(f"Emergency fund Amount : {Monthly_income} * {investment_percent/100} = {result_mul2}")

result_sub2 = result_sub1 -emergency_fund_percent -investment_percent
print(f"Available for Savings:    {result_sub1} - {emergency_fund_percent}-{investment_percent}= {result_sub2}")

result_div = (result_add3 /Monthly_income)*100
print(f"Expense Ratio:       {result_add3} / {Monthly_income} = {result_div}")

print("===MOUNTHY BUDGET REPORT===")
print("Income :",Monthly_income,"THB")
print("Fixed Expenses : ",result_add1,"THB")
print("Variable Expenses :",result_add2,"THB")
print("Total Expenses : ",result_add3,"THB")
print("Remaining Income :",result_sub1,"THB")

print("===SAVINGS BREAKDOWN===")
print("Emergency Fund (10%): ",result_mul2,"THB")
print("Investment (15%):",result_mul1,"THB")
print("Available for Savings: ",result_sub2,"THB")

print("===ANALYSIS===")
print("Expense Ratio:",result_div")



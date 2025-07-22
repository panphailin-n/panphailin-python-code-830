"""
# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")
"""
balance = 1000
pin = 1234
entered_pin = int(input("Enter PIN :"))
if entered_pin == pin:
    print("PIN accepted")
    while True :
        print("\n 1.Cheak Balance")
        print("2.Withdraw")
        print("3.Deposit")
        print("4.Exit")
        
        choice = int(input("Choose option"))
        if choice == "1":
            print("You balance =",balance)
        if choice =="2":
            amount=float(input("Whithdraw amount :"))
            if amount < 0:
                print("Cannot windraw amount: ")
            else:
            balance = balance-amount
            print("Please cllect your money, and your balance now =",balance)
        if choice=="3":
            amount=float(input("Deposit amount:"))
            if amount <0:
                print("Cannot deposit less than 0")
            else:
            balance=balance-amount
            print("Your balance now =",balance)
        if choice =="4":
            break
        else :
            print("Errror")
            continue
    

    else:
        print("Invaid PIN")       


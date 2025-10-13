

class BankAccount:
    def __init__(self, name, account_number, balance):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance
        self.__transaction_history = []

    def Deposit(self, amount):
        self.__balance += amount
        self.__transaction_history.append(f"Deposit: +${amount}")

    def Withdrawal(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrawal: -${amount}")
            return True
        self.__transaction_history.append(f"Failed Withdrawal: -${amount} (Insufficient funds)")
        return False

    def bankFees(self):
        fee = self.__balance * 0.05
        self.__balance -= fee
        self.__transaction_history.append(f"Bank Fee (5%): -${fee:.2f}")

    def display(self):

        print("=== Account Information ===")
        print(f"Account Name   : {self.__name}")
        print(f"Account Number : {self.__account_number}")
        print(f"Current Balance: ${self.__balance:.2f}")

        print("\n=== Transaction History ===")
        for transaction in self.__transaction_history:
            print(transaction)

    

account = BankAccount("Panphailin", "141930", 35000)
account.Withdrawal(10000)
account.bankFees()
account.Deposit(2000)
account.display()

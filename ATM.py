# Creating  a fully functional ATM interface 

import random

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        return random.randint(10000000, 99999999)

    def check_balance(self):
        print(f"Your account balance is {self.balance:.2f}Cr")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount:.2f}Rs deposited successfully.")
            self.check_balance()
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount:.2f}Rs withdrawn successfully.")
                self.check_balance()
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")


def main():
    atm = ATM(1000)  # Initial balance of Rs 1000

    print("Welcome to the ATM!")
    print(f"Your Account Number: {atm.account_number}")

    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                amount = float(input("Enter the deposit amount: Rs"))
                atm.deposit(amount)
            elif choice == 3:
                amount = float(input("Enter the withdrawal amount: Rs"))
                atm.withdraw(amount)
            elif choice == 4:
                print("Thank you for using the ATM!")
                break
            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
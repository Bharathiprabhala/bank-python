import random

class BankAccount:
    accounts = {}  # Class-level dictionary to store all accounts
    MIN_BALANCE = 500

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = random.randint(10000, 99999)
        self.transactions = []

        # Ensure unique account number
        while self.account_number in BankAccount.accounts:
            self.account_number = random.randint(10000, 99999)

        BankAccount.accounts[self.account_number] = self
        self.transactions.append(f"Account opened with ₹{balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount:.2f}")
        print(f"₹{amount:.2f} deposited. New balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")

        if self.balance - amount < BankAccount.MIN_BALANCE:
            return f"Minimum balance of ₹{BankAccount.MIN_BALANCE:.2f} must be maintained."

        else:
            print("Insufficient balance.")

        self.balance -= amount
        self.transactions.append(f"Withdrew ₹{amount:.2f}")
        return f"₹{amount:.2f} withdrawn. New balance: ₹{self.balance:.2f}"

    def display_balance(self):
        print("\n--- Account Details ---")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Available Balance: ₹{self.balance:.2f}")
        

    @staticmethod
    def find_account(account_number, name):
        account = BankAccount.accounts.get(account_number)
        if account and account.name.lower() == name.lower():
            return account
        else:
            return None

# --- Main logic ---
def main():
    while True:
        print("\n======= Welcome to the Banking System =======")
        print("1. Create New Savings Account")
        print("2. Access Existing Account")
        print("3. Exit")
        choice = input("Enter choice (1, 2, or 3): ")

        if choice == '1':
            name = input("Enter your name: ").strip()
            try:
                deposit = float(input("Enter initial deposit amount (₹): "))
                if deposit < 0:
                    print("Deposit must be a non-negative amount.")
                    continue
                account = BankAccount(name, deposit)
                print(f"\n✅ Account created successfully!")
                print(f"Your account number is: {account.account_number}")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif choice == '2':
            name = input("Enter your name: ").strip()
            try:
                account_number = int(input("Enter your 5-digit account number: "))
                account = BankAccount.find_account(account_number, name)

                if account:
                    print("\n🔓 Access granted.")
                    while True:
                        print("\n--- Account Menu ---")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Display Balance")
                        print("4. Logout")
                        option = input("Choose an option: ")

                        if option == '1':
                            name = input("Enter your name: ").strip()
                            try:
                                deposit = float(input("Enter initial deposit amount (₹): "))
                                if deposit < BankAccount.MIN_BALANCE:
                                    print(f"Initial deposit must be at least ₹{BankAccount.MIN_BALANCE:.2f}")
                                    continue

                                account = BankAccount(name, deposit)
                                print("\n✅ Account created successfully!")
                                print(f"Your account number is: {account.account_number}")

                            except ValueError:
                                print("Invalid amount.")

                        elif option == '2':
                            try:
                                amt = float(input("Enter amount to withdraw: ₹"))
                                account.withdraw(amt)
                            except ValueError:
                                print("Invalid input. Please enter a number.")

                        elif option == '3':
                            account.display_balance()

                        elif option == '4':
                            print("Logging out. Returning to main menu...")
                            break
                        else:
                            print("Invalid option. Please try again.")
                else:
                    print("❌ Account not found or credentials mismatch.")
            except ValueError:
                print("Invalid account number format. Please enter a 5-digit number.")

        elif choice == '3':
            print("👋 Thank you for using the Banking System!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
    

import os
import json

filename = "bankdata.json"

class Account:
    last_acc_number = 0  # Class variable to keep track of last account number

    def __init__(self, account_number=None, name=None, dob=None, address=None, password=None, acc_type=None, balance=0):
        if account_number is None:
            Account.last_acc_number += 1
            self.account_number = Account.last_acc_number
        else:
            self.account_number = account_number
        self.name = name
        self.dob = dob
        self.address = address
        self.password = password
        self.acc_type = acc_type
        self.balance = balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "dob": self.dob,
            "address": self.address,
            "password": self.password,
            "acc_type": self.acc_type,
            "balance": self.balance
        }

    def credit(self, amount):
        self.balance += amount
        print(f"Your account has been credited with {amount}. New balance: {self.balance}")

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        else:
            self.balance -= amount
            print(f"Your account has been debited with {amount}. New balance: {self.balance}")
            return True

    @staticmethod
    def create_account():
        name = input("Enter your full name: ")
        dob = input("Enter your date of birth: ")
        address = input("Enter your current address: ")
        password = int(input("Enter the pin/password for your account: "))
        acc_type = input("Enter the type of account (Saving or Current): ")
        balance = int(input("Enter the balance to activate the account: "))
        return Account(name=name, dob=dob, address=address, password=password, acc_type=acc_type, balance=balance)

def save_accounts(accounts):
    with open(filename, "w") as f:
        json.dump([acc.to_dict() for acc in accounts], f, indent=2)

def load_accounts():
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        with open(filename, "w") as f:
            json.dump([], f)
        return []
    with open(filename, "r") as f:
        data = json.load(f)
        accounts = []
        max_acc_number = 0
        for acc_data in data:
            acc = Account(**acc_data)
            accounts.append(acc)
            if acc.account_number > max_acc_number:
                max_acc_number = acc.account_number
        Account.last_acc_number = max_acc_number
        return accounts

def find_account(accounts, acc_number, password=None):
    for acc in accounts:
        if acc.account_number == acc_number:
            if password is None or acc.password == password:
                return acc
    return None

def main():
    accounts = load_accounts()

    while True:
        print("\n******** WELCOME TO MISHIYAMA BANK ********")
        print("PRESS 1 FOR CREATING A NEW ACCOUNT")
        print("PRESS 2 FOR ACCESSING ACCOUNT DETAILS")
        print("PRESS 3 FOR CREDITING AMOUNT IN ACCOUNT")
        print("PRESS 4 FOR DEBITING AMOUNT FROM ACCOUNT")
        print("PRESS 5 FOR TRANSFERRING AMOUNT TO ANOTHER ACCOUNT")
        print("PRESS 6 TO EXIT THE DISPLAY SCREEN")

        try:
            user_input = int(input())
        except ValueError:
            print("Invalid input, enter a number between 1 and 6.")
            continue

        if user_input == 1:
            customer = Account.create_account()
            accounts.append(customer)
            save_accounts(accounts)
            print(f"Your account number is: {customer.account_number}")

        elif user_input == 2:
            try:
                login_accountno = int(input("Enter your account number: "))
                login_password = int(input("Enter your account password: "))
            except ValueError:
                print("Invalid input.")
                continue
            acc = find_account(accounts, login_accountno, login_password)
            if acc:
                print("\n--- ACCOUNT DETAILS ---")
                print(f"Account Number: {acc.account_number}")
                print(f"Name: {acc.name}")
                print(f"DOB: {acc.dob}")
                print(f"Address: {acc.address}")
                print(f"Account Type: {acc.acc_type}")
                print(f"Balance: {acc.balance}")
            else:
                print("Invalid account number or password.")

        elif user_input == 3:
            try:
                login_accountno = int(input("Enter your account number: "))
                amount = int(input("Enter the amount to be credited: "))
            except ValueError:
                print("Invalid input.")
                continue
            acc = find_account(accounts, login_accountno)
            if acc:
                acc.credit(amount)
                save_accounts(accounts)
            else:
                print("Account not found.")

        elif user_input == 4:
            try:
                login_accountno = int(input("Enter your account number: "))
                amount = int(input("Enter the amount to be debited: "))
            except ValueError:
                print("Invalid input.")
                continue
            acc = find_account(accounts, login_accountno)
            if acc:
                if acc.debit(amount):
                    save_accounts(accounts)
            else:
                print("Account not found.")

        elif user_input == 5:
            try:
                sender_account = int(input("Enter the sender's account number: "))
                receiver_account = int(input("Enter the receiver's account number: "))
                amount = int(input("Enter the amount to be transferred: "))
            except ValueError:
                print("Invalid input.")
                continue
            sender = find_account(accounts, sender_account)
            receiver = find_account(accounts, receiver_account)
            if sender and receiver:
                if sender.debit(amount):
                    receiver.credit(amount)
                    save_accounts(accounts)
            else:
                print("Account(s) not found.")

        elif user_input == 6:
            print("Thanks for using our service : )")
            break

        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()
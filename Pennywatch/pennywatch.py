#A simple expense tracker , to analyze your income and expense on different 

# importing all the necessary modules

import os
import numpy as np
import pandas as pd
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))  # Folder where the script is located
FILENAME = os.path.join(script_dir, 'tracker.csv')

#describing the header part 
header = ["Date", "Transaction Type", "Amount", "Category", "Description"]

#To check if the file exist in system and inserting the header in the empty csv file
if not os.path.exists(FILENAME)or os.path.getsize(FILENAME)==0:
    df = pd.DataFrame(columns=header)
    df.to_csv(FILENAME, index=False)
    print(f"{FILENAME} created with header: {', '.join(header)}")
else:
    print(f"Found existing {FILENAME}")


while True:
    # Making the user choice interface
    print("\n*******DAY TO DAY EXPENSE TRACKER*******")
    print("1: Add Todays transcation")
    print("2: View all transactions till date")
    print("3: View transcation based on Category")
    print("4: View summary stats")
    print("5: Exit")

    # To validate the user input
    try:
        user_input = int(input("Enter your choice: "))
    except ValueError:
        print(" Please enter a number between 1 and 5.")
        continue

    # To get user transactoins details
    # Date
    # Transcation type
    # Amount
    # A little bit of description

    if user_input == 1:
        print("\nEnter the transactions details \n")
        today_date = input("Enter date (DD-Month name-YYYY):")
        try:
            # To check a valid date
            datetime.strptime(today_date, '%d %b %Y')
        except:
            print("Invalid date, try again.")
            continue  # makes sure to reprompt us to the while loop again

        while True:
            transaction_type = input(f"Is it Income or Expense ? ").strip().capitalize()
            if transaction_type in ['Income', 'Expense']:
                break
            print("Invalid type , choose between Income or Expense only")
            continue

        while True:
            transaction_amount = int(input(f"Enter the {transaction_type} amount "))
            if transaction_amount > 0:
                break
            print("Negative cash doesn't count try again")
            continue

        transaction_category = input(f"Enter the category (eg:- Food , Salary , Transportation etc.) ")
        user_description = input(f"Enter your description for this transcation  ")

        transaction = {
            'Date': [today_date],
            'Transaction Type': [transaction_type],
            'Amount': [transaction_amount],
            'Category': [transaction_category],
            'Description': [user_description]
        }

        new_data = pd.DataFrame(transaction)
        new_data.to_csv(FILENAME, mode='a', header=False, index=False)
        print("Data has been updated")

#To view all the transaction till this date 
    elif user_input == 2:
     df = pd.read_csv(FILENAME)
     if df.empty:
        print("No transactions found.")
     else:
        choice = input("Do you want to see All or just the Last 10? (A or L ?) ").strip().lower()
        if choice == 'a':
            print("\nAll Transactions:\n")
            print(df.to_string(index=False))
        elif choice == 'l':
            print("\nLast 10 Transactions:\n")
            print(df.tail(10).to_string(index=False))
        else:
            print("Invalid choice. Showing all by default.")
            print(df.to_string(index=False))
    
#To view transaction based on category
    elif user_input == 3:
        df=pd.read_csv(FILENAME)
        if df.empty:
            print("No transaction found.")
        else:
            category_choice=input("Enter the category to filter the data ")
            filter_data=df[df['Category'].str.casefold()==category_choice]
            if filter_data.empty:
                print(f"No transaction found for {category_choice} ") 
            else:
                print(f"\n *******Transaction for the category {category_choice}******* \n")
                print(filter_data.to_string(index=False))   


#To give a brief summary to the user regarding his/her day to day income and expenses
    
    elif user_input == 4:
        df=pd.read_csv(FILENAME)
        print("\n *******TOTAL SUMMARY*******")
        total_income=df[df['Transaction Type']=='Income']['Amount'].sum()
        print(f"Your total income is :- {total_income}\n")
        total_expense=df[df['Transaction Type']=='Expense']['Amount'].sum()
        print(f"Your total expense is :- {total_expense}\n")
        total_balance=total_income-total_expense
        print(f"Current Balance as per the transactions is {total_balance}")
        average_expense=df[df['Transaction Type']=='Expense']["Amount"].mean()
        print(f"Your avergae expense is :- {average_expense}")
        max_expense_category = df[df['Transaction Type'] == 'Expense'].loc[lambda x: x['Amount'].idxmax()]
        print(f"Your highest expense is {max_expense_category['Amount']} in {max_expense_category['Category']} category")

    elif user_input == 5:
        break







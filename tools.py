from account import Account
from db import customer_db
import re
import hashlib


def register():
    while True:
        try:
            print("REGISTRATION\n\n")

            response = input('''
            Hello, you are about to register for a Hiit bank Account
            Enter y to continue or q to quit
            ''')

            assert response == 'y' or response == 'q', 'Invalid input'
            if response == 'q': return

            acc = Account()
            bvn_response = input("Please enter your BVN, or leave blank if you do not have one")

            if len(bvn_response) > 0:
                acc.set_bvn(bvn_response)

            acc.set_nin(input("NIN: "))
            acc.set_fname(input("First name: "))
            acc.set_lname(input("Last name: "))
            acc.set_phone_no(input("Phone no: "))
            acc.set_email(input("Email: "))
            acc.set_passcode(input("5 digit passcode: "))
            acc.set_pin(input("4 digit pin: "))
            acc.set_address(input("Residential Address: "))

            customer_db[acc.get_account_no()] = acc

            print(f"""
                User created successfully!!!
                Your Account Number is {acc.get_account_no()}
                Your BVN is {acc.get_bvn()}
                Address is {acc.get_address()}
                """)

            break

        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except Exception as ex:
            print(f"Other Exception: {ex}")


def login() -> Account:
    while True:
        try:
            email = input("Email address: ")

            pattern = "^[a-zA-Z0-9\\-\\.\\_]*@[a-zA-Z]*\\.(com|org|net)$"
            assert re.search(pattern, email) is not None, "Invalid email format"

            user_accounts_with_email = [account for account in customer_db.values() if account.get_email() == email]

            assert len(user_accounts_with_email) == 1, "This email address was not found"

            user_account = user_accounts_with_email[0]

            passcode = input("Enter passcode:")

            assert passcode == user_account.get_passcode(), "Invalid passcode provided"

            print("LOGIN SUCCESSFUL!")
            return user_account

        except AssertionError as e:
            print("Assertion Error: " + str(e))
        except Exception as e:
            print("Exception: " + str(e))


def deposit(user: Account):
    while True:
        try:
            response = input('''
            
            How much would you like to deposit: 
            Enter q to quit
            ''')

            if response == 'q' : return

            assert response.isnumeric(), "Invalid input only numbers allowed"

            amount = float(response)

            user.deposit(amount)

            return

        except AssertionError as e:
            print('Assertion Error: '+ str(e))
        except Exception as e:
            print('Exception: ' + str(e))

def withdraw(user: Account):
    while True:
        try:
            response = input('''

            How much would you like to withdraw: 
            Enter q to quit
            ''')
            if response == 'q': return
            assert response.isnumeric(), "Invalid input only numbers allowed"
            amount = float(response)
            user.withdraw(amount)
            return

        except AssertionError as e:
            print('Assertion Error: ' + str(e))
        except Exception as e:
            print('Exception: ' + str(e))

def transfer(user: Account):
    while True:
        try:
            response = input('''
                You are about to perform a transfer.
                Enter y to continue or q to quit
                        ''')

            assert response == 'y' or response == 'q', 'Invalid input'
            if response == 'q': return

            user_accounts = []
            while len(user_accounts) == 0:
                beneficiary_acc_no = input('''
                Enter beneficiary account number
                ''')

                if re.search('^[0-9]{10}$', beneficiary_acc_no) is None:
                    print('Invalid account number format')
                    continue

                if beneficiary_acc_no == user.get_account_no():
                    print('Cannot initiate transfer to your own account')
                    continue

                user_accounts = [account for account in customer_db.values() if account.get_account_no() == beneficiary_acc_no]

                if len(user_accounts) == 0:
                    print('User with this account number not found')

            beneficiary = user_accounts[0]
            print(f'''
            Transfer of funds to {beneficiary.get_fname()} {beneficiary.get_lname()}
            ''')

            amount = ''

            while amount.isnumeric() is False:
                amount = input('How much would you like to transfer')
                if amount.isnumeric() is False:
                    print("Invalid input only numbers allowed")
                    continue

            amount = float(amount)

            user.transfer(amount, beneficiary)
            print('TRANSFER SUCCESSFUL')
            return


        except AssertionError as e:
            print('Assertion Error: ' + str(e))
        except Exception as e:
            print('Exception: ' + str(e))
def balance(user: Account):
    print(f'''
    Balance: N{user.get_balance()}
    ''')
def account_no(user: Account):
    print(f'''
    Account No: {user.get_account_no()}
    ''')
def bvn(user: Account):
    print(f'''
    BVN: {user.get_bvn()}
    ''')
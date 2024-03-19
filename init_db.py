from account import Account
from db import customer_db

account1 = Account(fname="John", lname="Doe", email="john.doe@gmail.com",
                   passcode="12345", pin="1234")
account1.set_address("101 Spooner Street, Quahog")
account1.set_phone_no("+08000000000")
account1.deposit(5000.0)

account2 = Account(fname="Jane", lname="Smith", email="jane.smith@gmail.com",
                   passcode="54321", pin="4321")
account2.set_address("503 Cover Drive, Quahog")
account2.set_phone_no("-09010000000")
account2.deposit(10000.0)

customer_db[account1.get_account_no()] = account1
customer_db[account2.get_account_no()] = account2
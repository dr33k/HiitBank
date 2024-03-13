from account import Account

customers:dict = dict()

account1 = Account(fname="John", lname="Doe", email="john.doe@gmail.com", passcode="12345", pin="1234")
account1.set_address("101 Spooner Street, Quahog")
account1.set_phone_no("08000000000")

account2 = Account(fname="Jane", lname="Smith", email="jane.smith@gmail.com", passcode="54321", pin="4321")
account1.set_address("503 Cover Drive, Quahog")
account1.set_phone_no("09010000000")

customers[account1.get_account_no()] = account1
customers[account2.get_account_no()] = account2




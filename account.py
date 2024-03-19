import hashlib
import random
from db import customer_db
import re

class Account:

    def __init__(self, fname=None, lname=None, email=None, passcode=None, pin=None, bvn=None):
        self.__fname = fname
        self.__lname = lname
        self.__phone_no = None
        self.__email = email
        self.__pin = pin
        self.__passcode = passcode
        self.__address:str = None

        if bvn == None:
            self.__bvn = str(random.randint(10000000000, 99999999999))
        else:
            self.__bvn = bvn

        self.__balance = 0.0
        self.__account_no = "888" + str(random.randint(1000000, 9999999))
        self.__nin:str = None

    def get_fname(self):
        return self.__fname

    def set_fname(self, fname:str):
        assert type(fname) == str, "Only strings allowed for First name"
        assert re.search("^[a-zA-Z\\'\\-]*$", fname) is not None, "Only alphabets and (-,') allowed"

        self.__fname = fname

    def get_lname(self):
        return self.__lname

    def set_lname(self, lname:str):
        assert type(lname) == str, "Only strings allowed for Last name"
        assert re.search("^[a-zA-Z\\'\\-]*$", lname) is not None, "Only alphabets and (-,') allowed"

        self.__lname = lname

    def get_phone_no(self):
        return self.__phone_no

    def set_phone_no(self, phone:str):
        assert type(phone) == str, "Only strings allowed for Phone number"

        pattern = "^[\\+\\-][0-9]{11,15}$"
        assert re.search(pattern, phone) is not None, "Incorrect phone number format at least 11 and at most 15 numbers"
        self.__phone_no = phone

    def get_email(self):
        return self.__email

    def set_email(self, email:str):
        assert type(email) == str, "Only strings allowed for Email"

        pattern = "^[a-zA-Z0-9\\-\\.\\_]*@[a-zA-Z]*\\.(com|org|net)$"
        assert re.search(pattern, email) is not None, "Invalid email format"

        self.__email = email

    def set_pin(self, new_pin: str):
        assert type(new_pin) == str, "New Pin provided is not a string value"
        assert re.search("^[0-9]{4}$", new_pin) is not None, "Pin must contain only 4 digits"

        self.__pin = new_pin

    def get_passcode(self):
        return self.__passcode

    def set_passcode(self, new_passcode: str):
        assert type(new_passcode) == str, "New passcode provided is not a string value"
        assert re.search("^[0-9]{5}$", new_passcode) is not None, "Passcode must contain only 5 digits"

        self.__passcode = new_passcode

    def get_address(self):
        return self.__address

    def set_address(self, address:str):
        assert type(address) is str, "New address provided is not a string value"

        address = re.sub("[?#]", "", address)

        self.__address = address

    def get_bvn(self):
        return self.__bvn

    def set_bvn(self, bvn):
        assert type(bvn) is str
        pattern = "^[0-9]{10}$"

        assert re.search(pattern, bvn) is not None, "Incorrect BVN format"

        self.__bvn = bvn


    def get_balance(self):
        return self.__balance

    def get_account_no(self):
        return self.__account_no

    def get_nin(self):
        return self.__nin

    def set_nin(self, nin):
        assert type(nin) is str, "NIN provided is not a string value"

        pattern = "^[0-9]{11}$"
        assert re.search(pattern, nin) is not None, "Invalid NIN provided"

        self.__nin = nin


    def withdraw(self, amount: float) -> float:
        assert type(amount) == float, "Amount to withdraw must be a number"
        assert amount > 0, "Amount to must be a positive number"
        assert amount <= self.__balance, "Insufficient funds"

        self.__balance -= amount

        print(f"""
        Debit:
        Withdrawn N{amount} successfully!
        New Balance: N{self.__balance}
""")
        return self.__balance


    def deposit(self, amount:float)-> float:
        assert type(amount) == float, "Amount to be deposited must be a number"
        assert amount > 0, "Amount to deposit must be positive"

        self.__balance += amount

        print(f"""
        Credit:
        Deposited N{amount} successfully!
        New Balance: N{self.__balance}
""")
        return self.__balance

    def transfer(self, amount:float, beneficiary):
        assert beneficiary is not None, "404 User does not exist"

        self.withdraw(amount)
        beneficiary.deposit(amount)
        return self.__balance












from abc import ABC
from bank import rich_bank
from datetime import datetime


class User(ABC):
    def __init__(self, name, email, address, password):
        self.name = name
        self.email = email
        self.address = address
        self.password = password


class AccountHolder(User):
    def __init__(self, name, email, address, account_type, password):
        super().__init__(name, email, address, password)
        self.account_type = account_type
        self.balance = 0
        self.account_number = f"{datetime.now().year}" + (
            f"{rich_bank.total_accounts + 1:04}"
        )
        rich_bank.add_account(self)

    def make_deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(
            f" --- $ {deposit_amount} has been deposited to your account ---\n --- Current balance is {self.balance}"
        )

    def check_balance(self):
        print(self.balance)

    def __repr__(self):
        return f"\n An account has been created with the name of {self.name}, and account number {self.account_number}, {self.account_type}"


class Admin(User):
    def __init__(self, name, email, address, password):
        super().__init__(name, email, address, password)
        self.admin_id = f"{rich_bank.total_admins + 1:04}"
        rich_bank.add_admin(self)

    def __repr__(self):
        return f"An admin has been created with the name of {self.name}, and admin id {self.admin_id}"

from abc import ABC
from bank import rich_bank
from datetime import datetime
from current_time import current_time


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
        self.history = []
        self.account_number = f"{datetime.now().year}" + (
            f"{rich_bank.total_accounts + 1:04}"
        )
        rich_bank.add_account(self)

    def make_deposit(self, deposit_amount):
        self.balance += deposit_amount
        statement = f"${deposit_amount} has been deposited on {current_time()}"
        self.history.append(statement)
        print(
            f"\n --- ${deposit_amount} has been deposited to your account ---\n --- Current balance is ${self.balance} ---\n"
        )

    def make_withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount
        statement = f"${withdraw_amount} has been withdrawn on {current_time()}"
        self.history.append(statement)
        print(
            f"\n --- ${withdraw_amount} has been withdrawn from your account ---\n --- Current balance is ${self.balance} ---\n"
        )

    def get_transaction_history(self):
        print("\n --- Your Transaction History ---\n")
        for statement in self.history:
            print(f" - {statement}")
        print("")

    def check_balance(self):
        print(self.balance)

    def __repr__(self):
        return f"\n- An account has been created with the name of {self.name}\n- Account number: {self.account_number}\n- Account type: {self.account_type} account\n* Make sure to remember the ACCOUNT NUMBER and PASSWORD to login"


class Admin(User):
    def __init__(self, name, email, address, password):
        super().__init__(name, email, address, password)
        self.admin_id = f"{rich_bank.total_admins + 1:04}"
        rich_bank.add_admin(self)

    def get_users_list(self):
        rich_bank.see_account_holders_list()

    def __repr__(self):
        return f"\n- An admin has been created with the name of {self.name}\n- Admin Id: {self.admin_id}\n* Make sure to remember the ADMIN ID and PASSWORD to login"

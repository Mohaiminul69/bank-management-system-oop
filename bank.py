class Bank:
    def __init__(self):
        self.accounts = []
        self.admins = []
        self.__balance = 70000000

    def add_account(self, account):
        self.accounts.append(account)

    def add_admin(self, account):
        self.admins.append(account)

    def find_account(self, account_number):
        for acc_num in self.accounts:
            if account_number == acc_num.account_number:
                return acc_num
        return None

    def find_admin(self, admin_id):
        for admin in self.admins:
            if admin_id == admin.admin_id:
                return admin
        return None

    def see_account_holders_list(self):
        print("\n --- List of Account Holders ---\n")
        print(f" #\tName\tAccount Number\tBalance")
        for idx, account in enumerate(self.accounts):
            print(
                f" {idx+1}\t{account.name}\t{account.account_number}\t{account.balance}"
            )
        print("")

    @property
    def balance(self):
        return self.__balance

    def increase_balance(self, amount):
        self.__balance += amount

    def decrease_balance(self, amount):
        self.__balance -= amount

    @property
    def total_accounts(self):
        return len(self.accounts)

    @property
    def total_admins(self):
        return len(self.admins)


rich_bank = Bank()

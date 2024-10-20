class Bank:
    def __init__(self):
        self.accounts = []
        self.admins = []

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

    @property
    def total_accounts(self):
        return len(self.accounts)

    @property
    def total_admins(self):
        return len(self.admins)


rich_bank = Bank()

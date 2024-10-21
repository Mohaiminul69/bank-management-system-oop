from create_account import create_account


def admin_menu(admin):
    print(f"\n ### Welcome to Rich Bank Admin {admin.name} ###\n")
    while True:
        print(
            "--- Please select an options ---\n1) Create an account\n2) Delete an account\n3) See all user accounts\n4) Check total balance of bank\n5) Check total loan amount\n6) Manage bank loan policy\n7) Logout"
        )
        option = int(input("Please Choose an Option: "))

        if option == 1:
            create_account("account_holder", True)

        elif option == 2:
            withdraw_amount = int(input("\nEnter the amount you want to withdraw: "))
            while withdraw_amount > admin.balance:
                print(f"\n *** You cannot withdraw more than {admin.balance} ***\n")
                withdraw_amount = int(input("Enter the amount you want to withdraw: "))
            admin.make_withdraw(withdraw_amount)

        elif option == 3:
            admin.get_users_list()

        elif option == 4:
            balance = admin.get_total_balance_of_bank()
            print(f"\n --- Total Balance of Bank: ${balance} ---\n")

        elif option == 7:
            print("\n --- Thank you for banking with us. ---")
            return

        else:
            print("\n --- Invalid option, please choose between 1 and 3. ---")

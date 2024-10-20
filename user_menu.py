def user_menu(user):
    print(f"\n ### Wellcome to Rich Bank {user.name} ###\n")
    while True:
        print(
            "--- Please select an options ---\n1) Make a deposit\n2) Make a withdrawal\n3) Check Balance\n4) Check Transaction History\n5) Transfer to another account\n6) Take a Loan\n7) Logout"
        )
        option = int(input("Please Choose an Option: "))

        if option == 1:
            deposit_amount = int(input("\nEnter the amount you want to deposit: "))
            while deposit_amount < 1:
                print("\n *** You cannot deposit less than $1 ***\n")
                deposit_amount = int(input("Enter the amount you want to deposit: "))
            user.make_deposit(deposit_amount)

        elif option == 2:
            withdraw_amount = int(input("\nEnter the amount you want to withdraw: "))
            while withdraw_amount > user.balance:
                print(f"\n *** You cannot withdraw more than {user.balance} ***\n")
                withdraw_amount = int(input("Enter the amount you want to withdraw: "))
            user.make_withdraw(withdraw_amount)

        elif option == 3:
            print(
                f"\n --- Current Balance ---\n\n Your available balance is: ${user.balance}\n"
            )

        elif option == 4:
            user.get_transaction_history()

        elif option == 7:
            print("\n --- Thank you for banking with us. ---")
            return

        else:
            print("\n --- Invalid option, please choose between 1 and 3. ---")

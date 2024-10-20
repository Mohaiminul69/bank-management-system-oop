from users import AccountHolder, Admin


def create_account(user_type):
    name = input("\nEnter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Enter a password: ")
    confirmPassword = input("Confirm password: ")

    while password != confirmPassword:
        print("\n --- Please re enter password ---\n")
        password = input("Enter a password: ")
        confirmPassword = input("Confirm password: ")

    if user_type == "admin":
        account = Admin(name, email, address, password)
        print(account)
    else:
        print(
            "\n --- Please select an account type ---\n\n 1) Savings Account\n 2) Current Account\n"
        )

        account_type = ""
        while True:
            account_option = int(input("Choose account type: "))
            if account_option == 1:
                account_type = "savings"
                break
            elif account_option == 2:
                account_type = "current"
                break
            else:
                print("\n --- Invalid option, please choose between 1 and 2. ---\n")

        account = AccountHolder(name, email, address, account_type, password)
        print(account)
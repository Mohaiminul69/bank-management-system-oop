from bank import rich_bank
from user_menu import user_menu


def login(user_type):
    if user_type == "admin":
        print("\n --- Please enter your Admin Id and password to login ---\n")
        admin_id = input("Enter your admin id: ")
        admin = rich_bank.find_admin(admin_id)
        if admin == None:
            print(
                "\n --- Admin does not exist ---\n --- Please enter a valid admin id ---\n"
            )
        else:
            password = input("Enter your password: ")
            while admin.password != password:
                print("\n --- Sorry password did not match ---\n")
                password = input("Enter re enter password: ")
            print(admin.admin_id)
    else:
        print("\n --- Please enter your Account Number and password to login ---\n")
        account = None
        while account == None:
            account_number = input("Enter your account number: ")
            account = rich_bank.find_account(account_number)
            if account == None:
                print(
                    "\n --- Account does not exist ---\n --- Please enter a valid account number ---\n"
                )
                continue
            else:
                password = input("Enter your password: ")
                while account.password != password:
                    print("\n --- Sorry password did not match ---\n")
                    password = input("Enter re enter password: ")
                return user_menu(account)

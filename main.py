from account import Account
from make_account import makeaccount
from menu_input import *
from show_all_info import show_all_account_information
from deposit import *
from withdraw import *


account_list = []
num_of_accounts = 0

def main():
    """Main function to run the banking system."""
    while True:
        show_menu() # ok
        choice = menu_input() # ok
        print()

        if choice == 1:
            make_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            show_all_account_information()
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("Illegal selection..")
            print()

if __name == "__main":
    main()
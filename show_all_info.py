from account_list import account_list

def show_all_account_information():
    for ac in account_list:
        ac.show_account_information()
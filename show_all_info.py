from account_list import AccountList

def show_all_account_information():
    for ac in AccountList.account_list:
        ac.show_account_information()
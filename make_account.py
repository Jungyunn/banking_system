from account import Account

def make_account(account_list):
    print("[계좌 개설]")
    user_id = input("계좌 ID를 입력해주세요: ")
    user_name = input("이름을 입력해주세요: ")
    user_money = input("입금액을 입력해주세요: ")
    
    if user_money.isdecimal():
        user_money = int(user_money)
    
    account_list.append(Account(user_id, user_name, user_money))
    
    return account_list
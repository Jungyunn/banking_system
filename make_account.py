from account import Account
from account_list import account_list


def make_account():
    print("[계좌 개설]")
    user_id = input("계좌 ID를 입력해주세요: ")
    user_name = input("이름을 입력해주세요: ")
    user_money = int(input("입금액을 입력해주세요: "))
    
    account_list.append(Account(user_id, user_name, user_money))
    
    return account_list
from account_list import AccountList

def deposit_money():
    account_id = int(input("계좌ID: "))
    deposit_money = int(input("입금액: "))

    for i in range(len(AccountList.account_list)):
        if account_id == AccountList.account_list[i]:
            AccountList.account_list[i].balance -= deposit_money
            print("입금완료")
            return
    print("유효하지 않는 ID입니다.")